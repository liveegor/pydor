# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GM_Form.ui'
#
# Created: Thu Jun 26 19:09:51 2014
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
        MainWindow.resize(463, 356)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/1403297645_User.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.breaksTableWidget = QtGui.QTableWidget(self.centralwidget)
        self.breaksTableWidget.setObjectName(_fromUtf8("breaksTableWidget"))
        self.breaksTableWidget.setColumnCount(4)
        self.breaksTableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.breaksTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.breaksTableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.breaksTableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.breaksTableWidget.setHorizontalHeaderItem(3, item)
        self.breaksTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.breaksTableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.horizontalLayout.addWidget(self.breaksTableWidget)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.addPushButton = QtGui.QPushButton(self.centralwidget)
        self.addPushButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/1403292182_Add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addPushButton.setIcon(icon1)
        self.addPushButton.setObjectName(_fromUtf8("addPushButton"))
        self.verticalLayout.addWidget(self.addPushButton)
        self.deletePushButton = QtGui.QPushButton(self.centralwidget)
        self.deletePushButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/1403362103_Delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deletePushButton.setIcon(icon2)
        self.deletePushButton.setObjectName(_fromUtf8("deletePushButton"))
        self.verticalLayout.addWidget(self.deletePushButton)
        self.editPushButton = QtGui.QPushButton(self.centralwidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("icons/1403292157_Edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editPushButton.setIcon(icon3)
        self.editPushButton.setObjectName(_fromUtf8("editPushButton"))
        self.verticalLayout.addWidget(self.editPushButton)
        self.refreshPushButton = QtGui.QPushButton(self.centralwidget)
        self.refreshPushButton.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("icons/1403548171_Synchronize.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshPushButton.setIcon(icon4)
        self.refreshPushButton.setObjectName(_fromUtf8("refreshPushButton"))
        self.verticalLayout.addWidget(self.refreshPushButton)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.exitPushButton = QtGui.QPushButton(self.centralwidget)
        self.exitPushButton.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("icons/1403292146_Log Out.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitPushButton.setIcon(icon5)
        self.exitPushButton.setObjectName(_fromUtf8("exitPushButton"))
        self.verticalLayout.addWidget(self.exitPushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Заведующий гаражом", None, QtGui.QApplication.UnicodeUTF8))
        self.breaksTableWidget.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Поломки</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        item = self.breaksTableWidget.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("MainWindow", "ID", None, QtGui.QApplication.UnicodeUTF8))
        item = self.breaksTableWidget.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("MainWindow", "Номер автобуса", None, QtGui.QApplication.UnicodeUTF8))
        item = self.breaksTableWidget.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("MainWindow", "Дата поломки", None, QtGui.QApplication.UnicodeUTF8))
        item = self.breaksTableWidget.horizontalHeaderItem(3)
        item.setText(QtGui.QApplication.translate("MainWindow", "Что сломалось", None, QtGui.QApplication.UnicodeUTF8))
        self.addPushButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Добавить поломку</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.deletePushButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Удалить поломку</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.editPushButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Редактировать поломку</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.refreshPushButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Обновить записи</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.exitPushButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Выход</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

