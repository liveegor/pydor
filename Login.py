#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import Login_Form
from PyQt4 import QtCore, QtGui
import Stuff

from Admin import Admin
from Dispatcher import Dispatcher
from GM import GM

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
    print "Very old version of cx_Oracle :",cx_Oracle.version
    sys.exit()



class Login (QtGui.QMainWindow, Login_Form.Ui_MainWindow):

    # Attributes
    gmNames   = []
    gmIds     = []
    dispNames = []
    dispIds   = []

    conn = None
    cursor = None

    admin = None
    disp  = None
    gm    = None

    sendLoginData = QtCore.pyqtSignal(str, int, str, cx_Oracle.Connection, \
        cx_Oracle.Cursor)



    # Constructor
    def __init__ (self):
        QtGui.QMainWindow.__init__(self)
        Login_Form.Ui_MainWindow.setupUi(self, self)

        # Connect to database
        self.connectToDB()

        # Windows for users
        self.admin = Admin()
        self.disp  = Dispatcher()
        self.gm    = GM()

        # Init connections
        self.exitPushButton.clicked.connect(self.onExit)
        self.postsComboBox.currentIndexChanged.connect(self.changeWorkers)
        self.loginPushButton.clicked.connect(self.onLogin)
        self.sendLoginData.connect(self.admin.receiveLoginData)
        self.sendLoginData.connect(self.disp.receiveLoginData)
        self.sendLoginData.connect(self.gm.receiveLoginData)
        self.refreshPushButton.clicked.connect(self.connectToDB)

        # But first ... let me know employees names
        self.readNames()
        self.changeWorkers()



    # Connect and read names of employes
    def readNames (self):

        # If connection not established,
        # it's not possible to login
        if not self.conn:
            return
        try:
			# get GM names
            self.cursor.execute(Stuff.SQL_GetGms)
            result = self.cursor.fetchall()
            self.gmIds   = []
            self.gmNames = []
            for i in range(len(result)):
                self.gmIds.append(result[i][0])
                self.gmNames.append(result[i][1].decode('utf8'))

            # get dispatchers names
            self.cursor.execute(Stuff.SQL_GetDisps)
            result = self.cursor.fetchall()
            self.dispIds   = []
            self.dispNames = []
            for i in range(len(result)):
                self.dispIds.append(result[i][0])
                self.dispNames.append(result[i][1].decode('utf8'))

        except cx_Oracle.Error, error:
            QtGui.QMessageBox.about(self, 'Error', str(error).decode('utf8'))



    # Before exit 
    def onExit (self):
        if self.cursor:
            self.cursor.close()
    	if self.conn:
    		self.conn.close()
    	self.close()



    # Change names of workers in combo box
    def changeWorkers (self):

    	choice = self.postsComboBox.currentIndex()
    	self.workersComboBox.clear()

    	# Director chosen
    	if choice == 0:
    		self.workersComboBox.addItem(u'Логинов А.В.')

    	# GM chosen
    	if choice == 1:
    		for name in self.gmNames:
    			self.workersComboBox.addItem(name)

    	# Dispatcher chosen
    	if choice == 2:
    		for name in self.dispNames:
    			self.workersComboBox.addItem(name)



    def onLogin (self):

        # If connection not established,
        # it's not possible to login
        if not self.conn:
            QtGui.QMessageBox.critical(self, u'Ошибка', u'Соединение не установлено!')
            return

        # Get employe's name and ID
        choice = self.postsComboBox.currentIndex()
        
        if choice == 0:
            self.sendLoginData.emit('admin', 0, u'Логинов А.В.', self.conn, self.cursor)

        elif choice == 1:
            i = self.workersComboBox.currentIndex()
            ID = self.gmIds[i]
            name = self.gmNames[i]
            self.sendLoginData.emit('gm', ID, name, self.conn, self.cursor)

        elif choice == 2:
            i = self.workersComboBox.currentIndex()
            ID = self.dispIds[i]
            name = self.dispNames[i]
            self.sendLoginData.emit('dispatcher', ID, name, self.conn, self.cursor)



    # Connetcs to Oracle db
    # Login data in Stuff module
    def connectToDB (self):

        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

        try:
            self.conn = cx_Oracle.connect (Stuff.login, Stuff.password, Stuff.server + '/' + Stuff.SID)
            self.cursor = self.conn.cursor()
            print 'Oracle DB Version: ', self.conn.version
            print 'Encoding: ', self.conn.encoding
            self.readNames()

        except cx_Oracle.Error, error:
            QtGui.QMessageBox.critical(self, u'Ошибка', str(error).decode('utf8'))
            self.conn = None



# Call if this is main module
# (not included)
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    w = Login()
    w.show()
    app.exec_()