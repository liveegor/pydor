# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login_Form.ui'
#
# Created: Thu Jun 26 16:30:42 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(399, 161)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/1403590507_van.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.postsComboBox = QtGui.QComboBox(self.centralwidget)
        self.postsComboBox.setObjectName(_fromUtf8("postsComboBox"))
        self.postsComboBox.addItem(_fromUtf8(""))
        self.postsComboBox.addItem(_fromUtf8(""))
        self.postsComboBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.postsComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.workersComboBox = QtGui.QComboBox(self.centralwidget)
        self.workersComboBox.setObjectName(_fromUtf8("workersComboBox"))
        self.horizontalLayout_2.addWidget(self.workersComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.exitPushButton = QtGui.QPushButton(self.centralwidget)
        self.exitPushButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/1403292146_Log Out.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitPushButton.setIcon(icon1)
        self.exitPushButton.setObjectName(_fromUtf8("exitPushButton"))
        self.horizontalLayout_3.addWidget(self.exitPushButton)
        self.refreshPushButton = QtGui.QPushButton(self.centralwidget)
        self.refreshPushButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/1403548171_Synchronize.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshPushButton.setIcon(icon2)
        self.refreshPushButton.setObjectName(_fromUtf8("refreshPushButton"))
        self.horizontalLayout_3.addWidget(self.refreshPushButton)
        self.loginPushButton = QtGui.QPushButton(self.centralwidget)
        self.loginPushButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("icons/1403297645_User.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loginPushButton.setIcon(icon3)
        self.loginPushButton.setObjectName(_fromUtf8("loginPushButton"))
        self.horizontalLayout_3.addWidget(self.loginPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Вход", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Должность:", None, QtGui.QApplication.UnicodeUTF8))
        self.postsComboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "Директор", None, QtGui.QApplication.UnicodeUTF8))
        self.postsComboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "Зав. гаражом", None, QtGui.QApplication.UnicodeUTF8))
        self.postsComboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "Диспетчер", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Сотрудник:", None, QtGui.QApplication.UnicodeUTF8))
        self.exitPushButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Выход</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.refreshPushButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Заново установить соединение</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.loginPushButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Войти</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

