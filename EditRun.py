#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import EditRun_Form
from PyQt4 import QtCore, QtGui
import Stuff
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


class EditRun (QtGui.QWidget, EditRun_Form.Ui_Form):

    # Signals
    runAdded = QtCore.pyqtSignal()


    def __init__ (self):
        ''' Constructor without args '''
        # Constructors of superclasses
        QtGui.QWidget.__init__(self)
        EditRun_Form.Ui_Form.setupUi(self, self)
        # Init Qt connections
        self.cancelPushButton.clicked.connect(self.onExit)
        self.okPushButton.clicked.connect(self.insertOrUpdateRun)
        # Set current date
        self.dateEdit.setDate(QtCore.QDate.currentDate())


    def clearWidgets(self):
        '''  Sets default values for all widgets '''
        self.idSpinBox.setValue(0)
        self.busComboBox.clear()
        self.routeComboBox.clear()
        self.driverComboBox.clear()
        self.dateEdit.setDate(QtCore.QDate.currentDate())


    def onExit (self):
        ''' Runs, when cancel button clicked '''
        self.clearWidgets()
        self.close()


    def receiveLoginData (self, goal, dispId, runId, connection, cursor):
        ''' Slot, receives connection, IDs and goal (update, insert)
            from Dispatcher class '''
        self.goal    = goal
        self.dispId  = dispId
        self.runId   = runId
        self.conn    = connection
        self.cursor  = cursor
        # Window title depends on goal
        if goal == 'insert':
            self.setWindowTitle(u'Добавить выезд')
        elif goal == 'update':
            self.setWindowTitle(u'Редактировать выезд')
        # Prepare form for showing
        self.prepareForm()
        self.show()


    def prepareForm(self):
        ''' Prepares form, adding values from database 
            into widgets '''
        try:
            # Fill bus combo box with buses
            self.cursor.execute(Stuff.SQL_GetBuses)
            result = self.cursor.fetchall()
            for number in result:
                self.busComboBox.addItem(number[0].decode('utf8'))
            # Fill route combo box
            self.cursor.execute(Stuff.SQL_GetRoutes)
            result = self.cursor.fetchall()
            for number in result:
                self.routeComboBox.addItem(str(number[0]))
            # Fill driver combo box
            self.cursor.execute(Stuff.SQL_GetDrivers)
            result = self.cursor.fetchall()
            self.driversIds = []
            for driver in result:
                self.driversIds.append(driver[1])
                self.driverComboBox.addItem(driver[0].decode('utf8'))
            # Disable / enable spin box depending on goal
            if self.goal == 'insert':
                self.idSpinBox.setEnabled(True)
            elif self.goal == 'update':
                self.idSpinBox.setValue(self.runId)
                self.idSpinBox.setEnabled(False)
                # Fill widgets with chosen run
                self.cursor.execute(Stuff.SQL_GetRuns_2 % (self.runId))
                result = self.cursor.fetchall()
                a = result[0][3]
                self.dateEdit.setDate(QtCore.QDate(a.year, a.month, a.day))
                index = self.busComboBox.findText(result[0][0].decode('utf8'))
                self.busComboBox.setCurrentIndex(index)
                index = self.routeComboBox.findText(str(result[0][1]))
                self.routeComboBox.setCurrentIndex(index)
                index = self.driversIds.index(result[0][2])
                self.driverComboBox.setCurrentIndex(index)
        except cx_Oracle.Error, error:
            QtGui.QMessageBox.about(self, 'Error', str(error).decode('utf8'))


    def insertOrUpdateRun(self):
        ''' Insert run or update it depending on goal '''
        # Read values from widgets
        v = {}
        v['runId']     = self.idSpinBox.value()
        v['date']   = self.dateEdit.date().toString('dd.MM.yy').toUtf8().data()
        v['bus']    = self.busComboBox.currentText().toUtf8().data()
        v['route']  = self.routeComboBox.currentText().toUtf8().data()
        v['drivId'] = self.driversIds [self.driverComboBox.currentIndex()]
        # Insert
        if self.goal == 'insert':
            try:
                SQL = Stuff.SQL_InsertRun % ( v['runId'], self.dispId, v['bus'], \
                    v['date'], v['route'], v['drivId'] )
                self.cursor.execute(SQL)
                self.conn.commit()
            except cx_Oracle.Error, error:
                QtGui.QMessageBox.about(self, 'Error', str(error).decode('utf8'))
            else: 
                self.clearWidgets()
                self.runAdded.emit()
                self.close()
       # Update
        elif self.goal == 'update':
            try:
                SQL = Stuff.SQL_UpdateRun % (self.dispId, v['bus'], \
                    v['date'], v['route'], v['drivId'], v['runId'])
                self.cursor.execute(SQL)
                self.conn.commit()
            except cx_Oracle.Error, error:
                QtGui.QMessageBox.about(self, 'Error', str(error).decode('utf8'))
            else: 
                self.clearWidgets()
                self.runAdded.emit()
                self.close()


# Call if this is main module
# (not included)
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    w = EditRun()
    # Connecting to database
    try:
        conn = cx_Oracle.connect (Stuff.login, Stuff.password, Stuff.server + '/' + Stuff.SID)
        cursor = conn.cursor()
        print 'Oracle DB Version: ', conn.version
        print 'Encoding: ', conn.encoding
    except cx_Oracle.Error, error:
        QtGui.QMessageBox.critical(None, u'Ошибка', str(error).decode('utf8'))

    w.receiveLoginData('update', 1, 0, conn, cursor)
    app.exec_()