#!/usr/bin/python
# -*- coding: utf-8 -*-

import Stuff
import sys
import GM_Form
import EditBreak
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



class GM (QtGui.QMainWindow, GM_Form.Ui_MainWindow):

    # Attributes
    conn = None
    cursor = None
    ID = 0
    editBreak = None
    sendLoginData = QtCore.pyqtSignal(str, int, int, cx_Oracle.Connection, \
        cx_Oracle.Cursor)



    # Constructor
    def __init__ (self):

        QtGui.QMainWindow.__init__(self)
        GM_Form.Ui_MainWindow.setupUi(self, self)

        self.editBreak = EditBreak.EditBreak()
	
        # Init connections
        self.exitPushButton.clicked.connect(self.onExit)
        self.addPushButton.clicked.connect(self.addBreak)
        self.editPushButton.clicked.connect(self.updateBreak)
        self.refreshPushButton.clicked.connect(self.displayBreaks)
        self.deletePushButton.clicked.connect(self.deleteBreak)
        self.sendLoginData.connect(self.editBreak.receiveLoginData)
        self.editBreak.breakAdded.connect(self.displayBreaks)

        # Set pretty column width
        self.breaksTableWidget.setColumnWidth(0, 50)
        self.breaksTableWidget.setColumnWidth(1, 80)



    # Displaying breaks in table
    def displayBreaks (self):

        try:
            # Get em ...
            self.cursor.numbersAsStrings = True
            self.cursor.execute(Stuff.SQL_GetBreaks % (self.ID))
            result = self.cursor.fetchall()

            # ... and display
            self.breaksTableWidget.setRowCount(0)
            self.breaksTableWidget.setRowCount(len(result))

            for i in range(len(result)):
                for j in range(4):
                    item = QtGui.QTableWidgetItem(str(result[i][j]).decode('utf8'))
                    self.breaksTableWidget.setItem(i, j, item)

            self.cursor.numbersAsStrings = False

        except cx_Oracle.Error, error:
            QtGui.QMessageBox.about(self, 'Error', str(error).decode('utf8'))



    # Do this after exit button clicked
    def onExit (self):

        self.breaksTableWidget.setRowCount(0)
        self.close()



    def addBreak (self):
        self.sendLoginData.emit('insert', self.ID, None, self.conn, self.cursor)



    def updateBreak (self):
        row = self.breaksTableWidget.currentRow()
        item = self.breaksTableWidget.item(row, 0)
        if not item:
            return
        break_id = int(item.text().toUtf8().data())

        self.sendLoginData.emit('update', self.ID, break_id, self.conn, self.cursor)




    def receiveLoginData (self, employee, ID, name, connection, cursor):

        if employee != 'gm':
            return

        self.ID = ID
        self.setWindowTitle(u'Заведующий гаражом: ' + name)
        self.conn = connection
        self.cursor = cursor

        self.displayBreaks()
        self.show()


    def deleteBreak (self):
        i  = self.breaksTableWidget.currentRow()
        ID = int(self.breaksTableWidget.item(i, 0).text().toUtf8().data())

        try:
            self.cursor.callproc('DELETEBREAK', [ID])
            self.conn.commit()
        except cx_Oracle.Error, error:
            QtGui.QMessageBox.about(self, 'Error', str(error).decode('utf8'))

        self.displayBreaks()



# Call if this is main module
# (not imported)
if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    w = GM()
    w.show()
    app.exec_()