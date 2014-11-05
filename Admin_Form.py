# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin_Form.ui'
#
# Created: Tue Jul  1 03:51:21 2014
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
        Form.resize(553, 379)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/1403297645_User.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.reportPushButton = QtGui.QPushButton(Form)
        self.reportPushButton.setObjectName(_fromUtf8("reportPushButton"))
        self.horizontalLayout_2.addWidget(self.reportPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.workersComboBox = QtGui.QComboBox(Form)
        self.workersComboBox.setObjectName(_fromUtf8("workersComboBox"))
        self.workersComboBox.addItem(_fromUtf8(""))
        self.workersComboBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.workersComboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.workersTableWidget = QtGui.QTableWidget(Form)
        self.workersTableWidget.setObjectName(_fromUtf8("workersTableWidget"))
        self.workersTableWidget.setColumnCount(4)
        self.workersTableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.workersTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.workersTableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.workersTableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.workersTableWidget.setHorizontalHeaderItem(3, item)
        self.workersTableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.horizontalLayout_3.addWidget(self.workersTableWidget)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.refreshPushButton = QtGui.QPushButton(Form)
        self.refreshPushButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/1403548171_Synchronize.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshPushButton.setIcon(icon1)
        self.refreshPushButton.setObjectName(_fromUtf8("refreshPushButton"))
        self.verticalLayout.addWidget(self.refreshPushButton)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.exitPushButton = QtGui.QPushButton(Form)
        self.exitPushButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/1403292146_Log Out.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitPushButton.setIcon(icon2)
        self.exitPushButton.setObjectName(_fromUtf8("exitPushButton"))
        self.verticalLayout.addWidget(self.exitPushButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Administator", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Сведения о пробеге автобуса: ", None, QtGui.QApplication.UnicodeUTF8))
        self.reportPushButton.setText(QtGui.QApplication.translate("Form", "Показать", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Выберите работников: ", None, QtGui.QApplication.UnicodeUTF8))
        self.workersComboBox.setItemText(0, QtGui.QApplication.translate("Form", "Диспетчеры", None, QtGui.QApplication.UnicodeUTF8))
        self.workersComboBox.setItemText(1, QtGui.QApplication.translate("Form", "Заведующие гаражом", None, QtGui.QApplication.UnicodeUTF8))
        item = self.workersTableWidget.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("Form", "ID", None, QtGui.QApplication.UnicodeUTF8))
        item = self.workersTableWidget.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("Form", "ФИО", None, QtGui.QApplication.UnicodeUTF8))
        item = self.workersTableWidget.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("Form", "Зарплата", None, QtGui.QApplication.UnicodeUTF8))
        item = self.workersTableWidget.horizontalHeaderItem(3)
        item.setText(QtGui.QApplication.translate("Form", "Оформлено поломок/выездов", None, QtGui.QApplication.UnicodeUTF8))
        self.refreshPushButton.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Обновить записи</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.exitPushButton.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Выход</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

