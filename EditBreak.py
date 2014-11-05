#!/usr/bin/python
# -*- coding: utf-8 -*-


import Stuff
import sys
import EditBreak_Form
from PyQt4 import QtCore, QtGui


# Russian support for client
import os
os.environ['NLS_LANG'] = 'Russian.AL32UTF8'


# Good module import
try:
    import cx_Oracle
except ImportError, info:
    print "Import Error:", info
    sys.exit()
if cx_Oracle.version < '3.0':
    print "Very old version of cx_Oracle :", cx_Oracle.version
    sys.exit()



class EditBreak (QtGui.QWidget, EditBreak_Form.Ui_Form):

    goal = ''
    GMID = 0
    break_id = 0
    conn = None
    cursor = None

    breakAdded = QtCore.pyqtSignal()



    # Constructor
    def __init__ (self):
        QtGui.QWidget.__init__(self)
        EditBreak_Form.Ui_Form.setupUi(self, self)

        # Connections Init
        self.okPushButton.clicked.connect(self.insert)
        self.cancelPushButton.clicked.connect(self.onCancel)




    # Clear values of all widgets
    def clearWidgets (self):
        self.breaksWhatTextEdit.clear()
        self.descriptionTextEdit.clear()
        self.sparePartsTextEdit.clear()
        self.worksTextEdit.clear()
        self.idSpinBox.setValue(0)
        self.costsSpinBox.setValue(0)
        self.dateEdit.clear()
        self.busComboBox.clear()



    # Insert or update breaks
    def insert (self):

        v = {}
        v['id'] =  self.idSpinBox.value()
        v['date']   = self.dateEdit.date().toString('dd.MM.yy').toUtf8().data()
        v['costs']  = self.costsSpinBox.value()
        v['descr']  = self.descriptionTextEdit.toPlainText().toUtf8().data()
        v['breaks'] = self.breaksWhatTextEdit.toPlainText().toUtf8().data()
        v['spares'] = self.sparePartsTextEdit.toPlainText().toUtf8().data()
        v['works']  = self.worksTextEdit.toPlainText().toUtf8().data()
        v['bus']    = self.busComboBox.currentText().toUtf8().data()

        # Insert
        if self.goal == 'insert':
            try:
                self.cursor.callproc('INSERTBREAK', [v['id'], self.GMID, v['bus'], \
                    v['date'], v['descr'], v['breaks'], v['costs'], v['spares'], \
                    v['works']])
                self.conn.commit()
            except cx_Oracle.Error, error:
                QtGui.QMessageBox.about(self, 'Error', str(error).decode('utf8'))
            else: 
                self.clearWidgets()
                self.breakAdded.emit()
                self.close()
       
       # Update
        elif self.goal == 'update':
            try:
                SQL = Stuff.SQL_UpdateBreak % (self.GMID, v['bus'], \
                    v['date'], v['descr'], v['breaks'], v['costs'], v['spares'], \
                    v['works'],  v['id'])
                self.cursor.execute(SQL)
                self.conn.commit()
            except cx_Oracle.Error, error:
                QtGui.QMessageBox.about(self, 'Error', str(error).decode('utf8'))
            else: 
                self.clearWidgets()
                self.breakAdded.emit()
                self.close()



    def onCancel (self):
        self.clearWidgets()
        self.close()



    # Fill widgets with values from DB
    def prepareForm (self):

        try:
            # Fill bus combo box with buses
            self.cursor.execute(Stuff.SQL_GetBuses)
            result = self.cursor.fetchall()
            for number in result:
                self.busComboBox.addItem(number[0].decode('utf8'))

            # Disable / enable spin box depending on goal
            if self.goal == 'insert':
                self.idSpinBox.setEnabled(True)
                self.dateEdit.setDate(QtCore.QDate.currentDate())

            elif self.goal == 'update':
                self.idSpinBox.setValue(self.break_id)
                self.idSpinBox.setEnabled(False)

                # Fill widgets with chosen break
                self.cursor.execute(Stuff.SQL_GetBreaks_2 % (self.break_id))
                result = self.cursor.fetchall()

                a = result[0][3]
                self.dateEdit.setDate(QtCore.QDate(a.year, a.month, a.day))
                self.costsSpinBox.setValue(result[0][6])
                index = self.busComboBox.findText(result[0][2].decode('utf8'))
                self.busComboBox.setCurrentIndex(index)
                self.breaksWhatTextEdit.setText(result[0][5].decode('utf8'))
                if result[0][4]:
                    self.descriptionTextEdit.setText(result[0][4].decode('utf8'))
                else: self.descriptionTextEdit.setText('')
                self.sparePartsTextEdit.setText(result[0][7].decode('utf8'))
                self.worksTextEdit.setText(result[0][8].decode('utf8'))

        except cx_Oracle.Error, error:
            QtGui.QMessageBox.about(self, 'Error', str(error).decode('utf8'))



    def receiveLoginData (self, goal, GMID, break_id, connection, cursor):
        ''' Принимает данные '''

        self.conn = connection
        self.cursor = cursor
        self.GMID = GMID
        self.goal = goal
        self.break_id = break_id

        if goal == 'insert':
            self.setWindowTitle(u'Добавить поломку')
        elif goal == 'update':
            self.setWindowTitle(u'Редактировать поломку')

        # Prepare
        self.prepareForm()
        self.show()


# Call if this is main module
# (not included)
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    w = EditBreak()

    try:
        conn = cx_Oracle.connect (Stuff.login, Stuff.password, Stuff.server + '/' + Stuff.SID)
        cursor = conn.cursor()
        print 'Oracle DB Version: ', conn.version
        print 'Encoding: ', conn.encoding
    except cx_Oracle.Error, error:
        QtGui.QMessageBox.critical(None, u'Ошибка', str(error).decode('utf8'))

    w.receiveLoginData('insert', 1, 51, conn, cursor)
    app.exec_()