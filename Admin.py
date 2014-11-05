#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import Admin_Form
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

# For report plot
import matplotlib.pyplot as plt



class Admin (QtGui.QWidget, Admin_Form.Ui_Form):

    # Attributes
    cursor = None

    # Constructor
    def __init__ (self):

        QtGui.QWidget.__init__(self)
        Admin_Form.Ui_Form.setupUi(self, self)

        # Set pretty column width
        self.workersTableWidget.setColumnWidth(0, 50)
        self.workersTableWidget.setColumnWidth(2, 80)
        self.workersTableWidget.setColumnWidth(3, 210)

        # Connections init
        self.exitPushButton.clicked.connect(self.onExit)
        self.refreshPushButton.clicked.connect(self.displayWorkers)
        self.workersComboBox.currentIndexChanged.connect(self.displayWorkers)
        self.reportPushButton.clicked.connect(self.showReport)


    # When exit button has been clicked
    def onExit (self):
        self.workersTableWidget.setRowCount(0)
        self.close()



    # Display dispatchers or garage managers
    # in the table
    def displayWorkers (self):

        index = self.workersComboBox.currentIndex()

        try:
            # Get em ... 
            self.cursor.execute(Stuff.SQL_GetWorkers[index])
            result = self.cursor.fetchall()

             # ... and display
            self.workersTableWidget.setRowCount(0)
            self.workersTableWidget.setRowCount(len(result))

            for i in range(len(result)):
                for j in range(4):
                    item = QtGui.QTableWidgetItem(str(result[i][j]).decode('utf8'))
                    self.workersTableWidget.setItem(i, j, item)

        except cx_Oracle.Error, error:
            QtGui.QMessageBox.critical(self, u'Ошибка', str(error).decode('utf8'))



    def showReport (self):
        try:
            # Get em ... 
            self.cursor.execute(Stuff.SQL_Report)
            result = self.cursor.fetchall()
        except cx_Oracle.Error, error:
            QtGui.QMessageBox.critical(self, u'Ошибка', str(error).decode('utf8'))
        else:
            result.sort()
            months = [int(row[0]) - 0.4 for row in result]
            distance = [row[1] for row in result]
            print distance, months
            for i in range(1, len(distance)):
                distance[i] += distance[i - 1]
                print distance[i]
            plt.bar(months, distance, color='green')
            plt.show()



    # Receive data from Login class
    def receiveLoginData (self, employee, id, name, connection, cursor):

        if employee != 'admin':
            return

        self.cursor = cursor
        self.setWindowTitle(name)
        self.show()
        self.displayWorkers()



# Call if this is main module
# (not included)
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    w = Admin()
    w.show()
    app.exec_()