#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import Dispatcher_Form
from PyQt4 import QtCore, QtGui
import Stuff
import EditRun
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


class Dispatcher (QtGui.QWidget, Dispatcher_Form.Ui_Form):

    # Attributes
    conn = None
    cursor = None
    ID = None
    # Qt signal
    sendLoginData = QtCore.pyqtSignal(str, int, int, cx_Oracle.Connection, \
        cx_Oracle.Cursor)


    def __init__ (self):
        ''' Conctructor without args '''
        QtGui.QWidget.__init__(self)
        Dispatcher_Form.Ui_Form.setupUi(self, self)
        # Set pretty column width
        self.runTableWidget.setColumnWidth(0, 50)
        self.runTableWidget.setColumnWidth(2, 80)
        self.runTableWidget.setColumnWidth(2, 80)
        # Edit run window
        self.editRun = EditRun.EditRun()
        # Init connections
        self.exitPushButton.clicked.connect(self.onExit)
        self.usualRadioButton.clicked.connect(self.displayRuns)
        self.unusualRadioButton.clicked.connect(self.displayRuns)
        self.refreshPushButton.clicked.connect(self.displayRuns)
        self.deletePushButton.clicked.connect(self.deleteRun)
        self.addPushButton.clicked.connect(self.insertRun)
        self.editPushButton.clicked.connect(self.updateRun)
        self.sendLoginData.connect(self.editRun.receiveLoginData)
        self.editRun.runAdded.connect(self.displayRuns)

    
    def onExit (self):
        '''Action for exit button'''
        self.runTableWidget.setRowCount(0)
        self.close()


    def displayRuns (self):
        ''' Show runs, added by logged in dispatcher '''
        # Lets know, what kind of runs need to
        # be displayed
        index = 1
        if self.usualRadioButton.isChecked():
            index = 0
        try:
            # Get em ... 
            self.cursor.execute(Stuff.SQL_GetRuns[index] % (self.ID))
            result = self.cursor.fetchall()
             # ... and display
            self.runTableWidget.setRowCount(0)
            self.runTableWidget.setRowCount(len(result))
            for i in range(len(result)):
                for j in range(4):
                    item = QtGui.QTableWidgetItem(str(result[i][j]).decode('utf8'))
                    self.runTableWidget.setItem(i, j, item)
        except cx_Oracle.Error, error:
            QtGui.QMessageBox.about(self, 'Error', str(error).decode('utf8'))


    def deleteRun (self):

        i  = self.runTableWidget.currentRow()
        ID = int(self.runTableWidget.item(i, 0).text().toUtf8().data())

        try:
            self.cursor.execute(Stuff.SQL_DeleteRun % (ID))
            self.conn.commit()

        except cx_Oracle.Error, error:
            QtGui.QMessageBox.about(self, 'Error', str(error).decode('utf8'))

        self.displayRuns()


    def receiveLoginData (self, employee, ID, name, connection, cursor):

        if employee != 'dispatcher':
            return

        self.ID = ID
        self.setWindowTitle(u'Диспетчер: ' + name)
        self.conn = connection
        self.cursor = cursor

        self.displayRuns()
        self.show()


    def insertRun (self):
        self.sendLoginData.emit('insert', self.ID, None, self.conn, self.cursor)


    def updateRun (self):
        row = self.runTableWidget.currentRow()
        item = self.runTableWidget.item(row, 0)
        if not item:
            return
        runId = item.text().toUtf8().data()
        runId = int(runId)
        self.sendLoginData.emit('update', self.ID, runId, self.conn, self.cursor)


# Call if this is main module
# (not included)
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    w = Dispatcher()

    conn = None
    cursor = None
    try:
        conn = cx_Oracle.connect (Stuff.login, Stuff.password, Stuff.server + '/' + Stuff.SID)
        cursor = conn.cursor()
        print 'Oracle DB Version: ', conn.version
        print 'Encoding: ', conn.encoding
    except cx_Oracle.Error, error:
        QtGui.QMessageBox.critical(self, u'Ошибка', str(error).decode('utf8'))

    w.receiveLoginData('dispatcher', 2, "Who's know?", conn,  cursor)
    app.exec_()