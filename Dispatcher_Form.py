# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dispatcher_Form.ui'
#
# Created: Thu Jun 26 03:42:36 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(440, 521)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/1403297645_User.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_4 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.usualRadioButton = QtGui.QRadioButton(self.groupBox)
        self.usualRadioButton.setChecked(True)
        self.usualRadioButton.setObjectName(_fromUtf8("usualRadioButton"))
        self.buttonGroup = QtGui.QButtonGroup(Form)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.usualRadioButton)
        self.verticalLayout_2.addWidget(self.usualRadioButton)
        self.unusualRadioButton = QtGui.QRadioButton(self.groupBox)
        self.unusualRadioButton.setEnabled(True)
        self.unusualRadioButton.setChecked(False)
        self.unusualRadioButton.setObjectName(_fromUtf8("unusualRadioButton"))
        self.buttonGroup.addButton(self.unusualRadioButton)
        self.verticalLayout_2.addWidget(self.unusualRadioButton)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_4.addWidget(self.line)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.runTableWidget = QtGui.QTableWidget(Form)
        self.runTableWidget.setObjectName(_fromUtf8("runTableWidget"))
        self.runTableWidget.setColumnCount(4)
        self.runTableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.runTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.runTableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.runTableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.runTableWidget.setHorizontalHeaderItem(3, item)
        self.runTableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.runTableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.horizontalLayout.addWidget(self.runTableWidget)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.addPushButton = QtGui.QPushButton(Form)
        self.addPushButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/1403292182_Add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addPushButton.setIcon(icon1)
        self.addPushButton.setObjectName(_fromUtf8("addPushButton"))
        self.verticalLayout.addWidget(self.addPushButton)
        self.deletePushButton = QtGui.QPushButton(Form)
        self.deletePushButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/1403362103_Delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deletePushButton.setIcon(icon2)
        self.deletePushButton.setObjectName(_fromUtf8("deletePushButton"))
        self.verticalLayout.addWidget(self.deletePushButton)
        self.editPushButton = QtGui.QPushButton(Form)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("icons/1403292157_Edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editPushButton.setIcon(icon3)
        self.editPushButton.setObjectName(_fromUtf8("editPushButton"))
        self.verticalLayout.addWidget(self.editPushButton)
        self.refreshPushButton = QtGui.QPushButton(Form)
        self.refreshPushButton.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("icons/1403548171_Synchronize.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshPushButton.setIcon(icon4)
        self.refreshPushButton.setObjectName(_fromUtf8("refreshPushButton"))
        self.verticalLayout.addWidget(self.refreshPushButton)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.exitPushButton = QtGui.QPushButton(Form)
        self.exitPushButton.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("icons/1403292146_Log Out.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitPushButton.setIcon(icon5)
        self.exitPushButton.setObjectName(_fromUtf8("exitPushButton"))
        self.verticalLayout.addWidget(self.exitPushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Выберите, какие выезды отобразить:", None, QtGui.QApplication.UnicodeUTF8))
        self.usualRadioButton.setText(QtGui.QApplication.translate("Form", "Обычые выезды", None, QtGui.QApplication.UnicodeUTF8))
        self.unusualRadioButton.setText(QtGui.QApplication.translate("Form", "Выезды по болезни/поломке", None, QtGui.QApplication.UnicodeUTF8))
        self.runTableWidget.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Выезды</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        item = self.runTableWidget.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("Form", "ID", None, QtGui.QApplication.UnicodeUTF8))
        item = self.runTableWidget.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("Form", "Водитель", None, QtGui.QApplication.UnicodeUTF8))
        item = self.runTableWidget.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("Form", "Маршрут", None, QtGui.QApplication.UnicodeUTF8))
        item = self.runTableWidget.horizontalHeaderItem(3)
        item.setText(QtGui.QApplication.translate("Form", "Дата", None, QtGui.QApplication.UnicodeUTF8))
        self.addPushButton.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Добавить выезд</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.deletePushButton.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Удалить выезд</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.editPushButton.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Редактировать выезд</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.refreshPushButton.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Обновить записи</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.exitPushButton.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Выход</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

