# Form implementation generated from reading ui file './UI/add_customer.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_customer_popup(object):
    def setupUi(self, customer_popup):
        customer_popup.setObjectName("customer_popup")
        customer_popup.resize(520, 640)
        customer_popup.setStyleSheet("QDialog{\n"
"    background-color: #ffffff;\n"
"    border: 4px solid rgb(14, 73, 243);\n"
"    border-radius: 16px;\n"
"}\n"
"QWidget{\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QLabel{\n"
"    padding-left: 8px;\n"
"}\n"
"\n"
"QLineEdit, QDateEdit, QComboBox{\n"
"    background-color: rgb(217, 217, 217);\n"
"    border-radius: 16px;\n"
"    padding-left: 16px;\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"    border: 2px solid rgb(14, 73, 243);\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(14, 73, 243);\n"
"    color: white;\n"
"    font-family: \'Inter Medium\', sans-serif;\n"
"    font-size: 16px;\n"
"    font-weight: normal;\n"
"      font-style: normal;\n"
"    border: 0px;\n"
"    padding: 8px auto;\n"
"    border-radius: 16px;\n"
"    width: 64px;\n"
"    margin: 0px 32px;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"    border: 0px;\n"
"}\n"
"QComboBox::on{\n"
"    border: 2px solid rgb(14, 73, 243);\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"    image: url(:/icon/icon/angle-arrow-down_icon.ico);\n"
"    width: 16px;\n"
"    margin-right: 16px;\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"    alternate-background-color: #fff;\n"
"    border: 2px solid rgb(14, 73, 243);\n"
"    border-bottom-left-radius: 16px;\n"
"    border-bottom-right-radius: 16px;\n"
"    padding: 0px 8px 16px 8px;\n"
"}\n"
"\n"
"\n"
"QDateEdit::drop-down {\n"
"    image: url(:/icon/icon/angle-arrow-down_icon.ico);\n"
"    width: 16px;\n"
"    margin-right: 16px;\n"
"}\n"
"\n"
"QDateEdit QCalendarWidget QToolButton {\n"
"    color: black;\n"
"}\n"
"\n"
" QDateEdit QCalendarWidget QAbstractItemView {\n"
"     background-color: white;\n"
"     border: 0px;\n"
"     selection-background-color: rgb(188, 206, 253);\n"
" }\n"
"\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(customer_popup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QLabel(parent=customer_popup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(9)
        self.header.setFont(font)
        self.header.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.header.setScaledContents(True)
        self.header.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.header.setObjectName("header")
        self.verticalLayout.addWidget(self.header)
        self.input_form = QtWidgets.QWidget(parent=customer_popup)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.input_form.setFont(font)
        self.input_form.setStyleSheet("")
        self.input_form.setObjectName("input_form")
        self.gridLayout = QtWidgets.QGridLayout(self.input_form)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_7 = QtWidgets.QWidget(parent=self.input_form)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_7 = QtWidgets.QLabel(parent=self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.txt_address = QtWidgets.QLineEdit(parent=self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_address.sizePolicy().hasHeightForWidth())
        self.txt_address.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_address.setFont(font)
        self.txt_address.setObjectName("txt_address")
        self.verticalLayout_7.addWidget(self.txt_address)
        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 1)
        self.gridLayout.addWidget(self.widget_7, 2, 0, 1, 3)
        self.widget_9 = QtWidgets.QWidget(parent=self.input_form)
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_9)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.gridLayout.addWidget(self.widget_9, 3, 1, 1, 1)
        self.widget_2 = QtWidgets.QWidget(parent=self.input_form)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.txt_first_name = QtWidgets.QLineEdit(parent=self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_first_name.sizePolicy().hasHeightForWidth())
        self.txt_first_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_first_name.setFont(font)
        self.txt_first_name.setObjectName("txt_first_name")
        self.verticalLayout_2.addWidget(self.txt_first_name)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.gridLayout.addWidget(self.widget_2, 0, 0, 1, 1)
        self.widget_8 = QtWidgets.QWidget(parent=self.input_form)
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.gridLayout.addWidget(self.widget_8, 3, 0, 1, 1)
        self.widget_6 = QtWidgets.QWidget(parent=self.input_form)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_6 = QtWidgets.QLabel(parent=self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.verticalLayout_6.setStretch(0, 1)
        self.gridLayout.addWidget(self.widget_6, 0, 2, 1, 1)
        self.widget_3 = QtWidgets.QWidget(parent=self.input_form)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.txt_last_name = QtWidgets.QLineEdit(parent=self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_last_name.sizePolicy().hasHeightForWidth())
        self.txt_last_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_last_name.setFont(font)
        self.txt_last_name.setObjectName("txt_last_name")
        self.verticalLayout_3.addWidget(self.txt_last_name)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.gridLayout.addWidget(self.widget_3, 0, 1, 1, 1)
        self.widget_10 = QtWidgets.QWidget(parent=self.input_form)
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.gridLayout.addWidget(self.widget_10, 3, 2, 1, 1)
        self.widget_5 = QtWidgets.QWidget(parent=self.input_form)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(parent=self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.txt_email = QtWidgets.QLineEdit(parent=self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_email.sizePolicy().hasHeightForWidth())
        self.txt_email.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_email.setFont(font)
        self.txt_email.setObjectName("txt_email")
        self.verticalLayout_5.addWidget(self.txt_email)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 1)
        self.gridLayout.addWidget(self.widget_5, 1, 1, 1, 2)
        self.widget_4 = QtWidgets.QWidget(parent=self.input_form)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(parent=self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.txt_tel = QtWidgets.QLineEdit(parent=self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_tel.sizePolicy().hasHeightForWidth())
        self.txt_tel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_tel.setFont(font)
        self.txt_tel.setObjectName("txt_tel")
        self.verticalLayout_4.addWidget(self.txt_tel)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.gridLayout.addWidget(self.widget_4, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.input_form)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=customer_popup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(48)
        self.buttonBox.setFont(font)
        self.buttonBox.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 6)
        self.verticalLayout.setStretch(2, 3)

        self.retranslateUi(customer_popup)
        QtCore.QMetaObject.connectSlotsByName(customer_popup)

    def retranslateUi(self, customer_popup):
        _translate = QtCore.QCoreApplication.translate
        customer_popup.setWindowTitle(_translate("customer_popup", "Customer"))
        self.header.setText(_translate("customer_popup", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">New Customer</span></p></body></html>"))
        self.label_7.setText(_translate("customer_popup", "Address"))
        self.label_2.setText(_translate("customer_popup", "First name"))
        self.label_6.setText(_translate("customer_popup", "Birthday"))
        self.label_3.setText(_translate("customer_popup", "Last name"))
        self.label_5.setText(_translate("customer_popup", "Email"))
        self.label_4.setText(_translate("customer_popup", "Telephone"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    customer_popup = QtWidgets.QDialog()
    ui = Ui_customer_popup()
    ui.setupUi(customer_popup)
    customer_popup.show()
    sys.exit(app.exec())
