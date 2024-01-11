from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem
import math

class CustomTableView_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(732, 480)
        Form.setStyleSheet("QWidget{\n"
"    background:rgb(188, 206, 253);\n"
"    border-radius: 16px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: 0px;\n"
"    background:rgb(217, 217, 217);\n"
"    height: 4px;\n"
"    margin: 0px 0px 0 40px;\n"
"}       \n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(112, 112, 112);\n"
"    min-width: 32px;\n"
"}        \n"
"QScrollBar::add-line:horizontal {\n"
"    border: 0px;\n"
"    background: rgb(188, 206, 253);\n"
"    width: 64px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: 0px;\n"
"    background: rgb(188, 206, 253);\n"
"    width: 64px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: 0px;\n"
"    width: 4px;\n"
"    background:rgb(217, 217, 217);\n"
"    margin: 26px 0px 0px 0px;\n"
"}       \n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(112, 112, 112);\n"
"    min-height: 32px;\n"
"}        \n"
"QScrollBar::add-line:vertical {\n"
"    border: 0px;\n"
"    background: rgb(188, 206, 253);\n"
"    height: 64px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: 0px;\n"
"    background: rgb(188, 206, 253);\n"
"    height: 64px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QHeaderView{\n"
"    background-color: rgb(188, 206, 253);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(188, 206, 253);\n"
"    color: rgb(112, 112, 112);\n"
"    border: 0px;\n"
"    padding: 2px 4px 2px 4px;        \n"
"    font-size: 12px;\n"
"    font-family: Inter; \n"
"    font-weight: bold;\n"
"}\n"
"QTableCornerButton::section {\n"
"    background-color: rgb(188, 206, 253);\n"
"    border-top-left-radius: 16px;\n"
"}\n"
"\n"
"QTableWidget { \n"
"    background-color: #ffffff;\n"
"    border-width: 0px;\n"
"    border-top-left-radius: 16px;\n"
"}\n"
"\n"
"QLineEdit, QDateEdit, QComboBox, QTextEdit{\n"
"    background-color: #ffffff;\n"
"    padding-left: 16px;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding-left: 16px;\n"
"}\n"
"\n"
"QPushButton, QLabel {\n"
"    color: rgb(112, 112, 112);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #fff;\n"
"}\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.lb_page = QtWidgets.QLabel(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_page.sizePolicy().hasHeightForWidth())
        self.lb_page.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(True)
        self.lb_page.setFont(font)
        self.lb_page.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lb_page.setObjectName("lb_page")
        self.gridLayout.addWidget(self.lb_page, 1, 2, 1, 1)
        self.table = QtWidgets.QTableWidget(parent=Form)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.setDefaultDropAction(QtCore.Qt.DropAction.IgnoreAction)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setTextElideMode(QtCore.Qt.TextElideMode.ElideMiddle)
        self.table.setShowGrid(True)
        self.table.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.table.setCornerButtonEnabled(False)
        self.table.setRowCount(100)
        self.table.setColumnCount(10)
        self.table.setObjectName("table")
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.table, 0, 0, 1, 4)
        self.btn_prev = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_prev.sizePolicy().hasHeightForWidth())
        self.btn_prev.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(True)
        self.btn_prev.setFont(font)
        self.btn_prev.setObjectName("btn_prev")
        self.gridLayout.addWidget(self.btn_prev, 1, 0, 1, 1)
        self.btn_next = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_next.sizePolicy().hasHeightForWidth())
        self.btn_next.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(True)
        self.btn_next.setFont(font)
        self.btn_next.setObjectName("btn_next")
        self.gridLayout.addWidget(self.btn_next, 1, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: rgb(112, 112, 112);\n"
"background-color: rgb(188, 206, 253);\n"
"border: 0px;\n"
"padding: 0px;\n"
"margin: 0px;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 4)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 4)
        self.gridLayout.setRowStretch(0, 16)
        self.gridLayout.setRowStretch(1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lb_page.setText(_translate("Form", "/1"))
        self.btn_prev.setText(_translate("Form", "Prev"))
        self.btn_next.setText(_translate("Form", "Next"))
        self.lineEdit.setText(_translate("Form", "1"))


class CustomTableView(QtWidgets.QWidget):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.ui:CustomTableView_Form = CustomTableView_Form()
        self.ui.setupUi(self)
        self.data = []
        self.header = ['A','B','C','D','E','F','G','H','I','J','K']
        self.current_page = 1
        self.number_of_page = 1
        self.max_row_in_a_page = 100
        self.ui.table.setRowCount(self.max_row_in_a_page)
        self.setupSlot()
        self.set_content()
    
    def update_data(self, data: list, header):
        self.data = data
        self.header = header
        self.number_of_page = math.ceil(len(self.data)/self.max_row_in_a_page)
        if self.number_of_page < 1:
            self.number_of_page = 1
        self.current_page = 1
        self.set_content()
    
    def set_content(self):
        self.ui.table.clear()
        self.ui.lb_page.setText(f'/{self.number_of_page}')
        self.ui.lineEdit.setText(f'{self.current_page}')
        self.set_btn_state()
        start_content_index = (self.current_page - 1) * self.max_row_in_a_page
        vheader = [str(i) for i in range(start_content_index + 1, start_content_index + self.max_row_in_a_page + 1)]
        self.ui.table.setVerticalHeaderLabels(vheader)
        self.ui.table.setColumnCount(len(self.header))
        self.ui.table.setHorizontalHeaderLabels(self.header)
        size = len(self.data)
        for i in range(start_content_index, start_content_index + self.max_row_in_a_page):
            if i >= size:
                break
            for c_index, value in enumerate(self.data[i]):
                item = QTableWidgetItem()
                item.setData(0, str(value))
                self.ui.table.setItem(i - start_content_index, c_index, item)

    def setupSlot(self):
        self.ui.btn_next.clicked.connect(self.next_page)
        self.ui.btn_prev.clicked.connect(self.prev_page)
        self.ui.lineEdit.textChanged.connect(self.jump_to_page)
    
    def set_btn_state(self):
        if self.current_page == self.number_of_page:
            self.ui.btn_next.setEnabled(False)
        else:
            self.ui.btn_next.setEnabled(True)
        if self.current_page == 1:
            self.ui.btn_prev.setEnabled(False)
        else:
            self.ui.btn_prev.setEnabled(True)

    def next_page(self):
        self.current_page += 1
        self.set_content()
    
    def prev_page(self):
        self.current_page -= 1
        self.set_content()
    
    def jump_to_page(self):
        try:
            if self.ui.lineEdit.text() == '':
                self.current_page = 1
            else:
                self.current_page = int(self.ui.lineEdit.text())
        except:
            self.current_page = self.current_page
        finally:
            if self.current_page > self.number_of_page:
                self.current_page = self.number_of_page
            elif self.current_page < 1:
                self.current_page = 1
            else:
                self.current_page = self.current_page
        self.set_content()    

    def get_current_item(self):
        return self.ui.table.selectedItems()
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = CustomTableView()
    ui.show()
    ui.update_data([], ['a','b','c'])
    sys.exit(app.exec())
