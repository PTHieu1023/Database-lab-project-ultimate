from UI.pop_up_staff import Ui_Dialog
from UI.customer_popup import Ui_customer_popup
from UI.supplyment_popup import Ui_SupplyProduct
from UI.add_order_popup import Ui_add_order_popup

from Backend.DataBaseHandle import DataBase

from PyQt6.QtWidgets import QDialog, QWidget, QDialogButtonBox, QMessageBox, QTableWidgetItem
from PyQt6.QtCore import QDate, pyqtSignal,pyqtSlot, QDateTime
from datetime import date, datetime

class AddRecordDialog(QDialog):

    inserted_record  = pyqtSignal()

    def __init__(self, parent: QWidget, ui: object) -> None:
        super().__init__(parent)
        self.cur_id = -1
        self.database: DataBase = None
        self.ui = ui
        self.isConfirm = False
        self.ui.setupUi(self)
        self.ok_button: QDialogButtonBox.StandardButton = self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Ok)
        self.cancel_button: QDialogButtonBox.StandardButton = self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Cancel)

        self.customStyle()
        self.setupSlot()
    
    def set_database(self, database: DataBase):
        if database:
            self.database = database
        else:
            raise Exception("Database is not connected")
    
    def customStyle(self):
        # Apply custom font styles
        if self.ok_button is not None:
            self.ok_button.setStyleSheet("""
                QPushButton{
                    background-color: #4CAF50; 
                }
                QPushButton:hover {
                    color: #4CAF50;
                    background-color: rgb(217, 217, 217);
                }
            """)

        if self.cancel_button is not None:
            self.cancel_button.setStyleSheet("""
                QPushButton {
                    background-color: #FF4500;
                }
                QPushButton:hover {
                    color: #FF4500;
                    background-color: rgb(217, 217, 217);
                }
            """)

    def setupSlot(self):
        self.ok_button.clicked.connect(self.on_ok_button_clicked)
        self.cancel_button.clicked.connect(self.on_cancle_button_clicked)

    def on_ok_button_clicked(self):
        print('confirmed')
        suc, msg = self.query_data()
        if suc is None:
            self.cur_id = -1
            return
        if suc:
            QMessageBox.information(None, "Success", msg)
        else:
            QMessageBox.information(None, "Error", msg)
        self.cur_id = -1
        self.inserted_record.emit()
        self.close()
    
    def on_cancle_button_clicked(self):
        self.cur_id = -1
        self.close()

    def query_data(self):
        return False, 'No found object'

class StaffWindow(AddRecordDialog):
    def __init__(self, parent=None):
        super().__init__(parent, Ui_Dialog())
    
    def set_database(self, database: DataBase):
        super().set_database(database)
        self.get_role_list()

    def get_role_list(self):
        _,roles = self.database.select_query('select sr.staff_role_id, sr.role from staff_role as sr;')
        self.roles_dict = {role_str: index for index, role_str in roles}
        self.ui.txt_role.clear()
        self.ui.txt_role.addItems(self.roles_dict.keys())

    def show_popup(self, staff_info = None):
        header = f'<html><head/><body><p align="center"><span style=" font-size:36pt;">{"New Staff" if staff_info is None else "Update - " + str(staff_info["staff_id"])}</span></p></body></html>'
        self.ui.header.setText(header)
        if staff_info is None:
            self.cur_id = -1
            staff_info = {
                'first_name':'',
                'last_name':'',
                'dob': date(2000, 1, 1),
                'telephone': '',
                'email': '',
                'address': '',
                'start_working_date': datetime.now().date(),
                'salary': '',
                'role': 1,
                'working_type': 'FULLTIME'
            }
        else:
            self.cur_id = staff_info['staff_id']
        self.ui.txt_first_name.setText(staff_info['first_name'])
        self.ui.txt_last_name.setText(staff_info['last_name'])
        self.ui.txt_dob.setDate(QDate.fromString(staff_info['dob'].strftime('%Y-%m-%d'), 'yyyy-MM-dd'))
        self.ui.txt_tel.setText(str(staff_info['telephone']))
        self.ui.txt_email.setText(staff_info['email'])
        self.ui.txt_address.setText(staff_info['address'])
        self.ui.txt_hiredate.setDate(QDate.fromString(staff_info['start_working_date'].strftime('%Y-%m-%d'), 'yyyy-MM-dd'))
        self.ui.txt_salary.setText(str(staff_info['salary']))
        self.ui.txt_role.setCurrentIndex(staff_info['role']-1)
        self.ui.txt_working_type.setCurrentIndex(0 if staff_info['working_type'] == 'PARTTIME' else 1)
        self.exec()

    def import_form(self):
        return {
            'first_name': self.ui.txt_first_name.text(), 
            'last_name': self.ui.txt_last_name.text(), 
            'dob': self.ui.txt_dob.text(), 
            'role':self.roles_dict[self.ui.txt_role.currentText()], 
            'salary': self.ui.txt_salary.text(),
            'telephone': self.ui.txt_tel.text(), 
            'email': self.ui.txt_email.text(), 
            'address': self.ui.txt_address.text(),
            'start_working_date': self.ui.txt_hiredate.text(),
            'working_type': self.ui.txt_working_type.currentText()
        }

    def query_data(self):
        suc = msg = None
        confirm_dialog = QMessageBox.question(None, 'Confirm', 'Do you want to continue ?',  QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if confirm_dialog == QMessageBox.StandardButton.No:
                return suc, msg
        if self.cur_id == -1:
            suc, msg = self.database.insert_query('staff', self.import_form())
        else:
            update_form = self.import_form()
            suc, msg = self.database.update_query('staff', self.cur_id, update_form)
        return suc, msg
    
class CustomerWindow(AddRecordDialog):
    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent, Ui_customer_popup())

    def set_database(self, database: DataBase):
        return super().set_database(database)
    
    def show_popup(self, info = None):
        header = f'<html><head/><body><p align="center"><span style=" font-size:36pt;">{"New Customer" if info is None else "Update - " + str(info["customer_id"])}</span></p></body></html>'
        self.ui.header.setText(header)
        if info is None:
            self.cur_id = -1
            info = {
                'first_name':'',
                'last_name':'',
                'telephone': '',
                'email': '',
                'address': '',
            }
        else:
            self.cur_id = info['customer_id']
        self.ui.txt_first_name.setText(info['first_name'])
        self.ui.txt_last_name.setText(info['last_name'])
        self.ui.txt_tel.setText(str(info['telephone']))
        self.ui.txt_email.setText(info['email'])
        self.ui.txt_address.setText(info['address'])
        self.exec()

    def import_form(self):
        data = {}
        if self.ui.txt_first_name.text() != '':
            data['first_name'] = self.ui.txt_first_name.text()
        if self.ui.txt_last_name.text() != '':
            data['last_name'] = self.ui.txt_last_name.text()
        if self.ui.txt_tel.text() != '':
            data['telephone'] = self.ui.txt_tel.text()
        if self.ui.txt_email.text() != '':
            data['email'] = self.ui.txt_email.text()
        if self.ui.txt_address.text() != '':
            data['address'] = self.ui.txt_address.text()
        return data
    
    def query_data(self):
        suc = msg = None
        confirm_dialog = QMessageBox.question(None, 'Confirm', 'Do you want to continue ?',  QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if confirm_dialog == QMessageBox.StandardButton.No:
                return suc, msg
        if self.cur_id == -1:
            suc, msg = self.database.insert_query('customer', self.import_form())
        else:
            update_form = self.import_form()
            suc, msg = self.database.update_query('customer', self.cur_id, update_form)
        return suc, msg
    
class ProductWindow(AddRecordDialog):
    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent, Ui_SupplyProduct())
        self.ui: Ui_SupplyProduct

    def set_database(self, database: DataBase):
        return super().set_database(database)
    
    def show_popup(self, info = None):
        self.cur_id = info['product_id']
        self.ui.txt_title.setText(str(info['title']))
        self.ui.txt_suplier.setText(str(info['supplier']))
        self.ui.txt_price.setText('')
        self.ui.txt_quantity.setText('')
        self.ui.created_time.setDateTime(QDateTime.currentDateTime())
        self.exec()

    def import_form(self):
        data = {}
        data['product_id'] = self.cur_id
        data['price_all'] = self.ui.txt_price.text()
        data['quantity'] = self.ui.txt_quantity.text()
        data['supplied_time'] = self.ui.created_time.time().toString("hh:mm:ss")
        data['date'] = self.ui.created_time.date().toString("yyyy-MM-dd")
        return data

    def query_data(self):
        suc = msg = None
        confirm_dialog = QMessageBox.question(None, 'Confirm', 'Do you want to continue ?',  QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if confirm_dialog == QMessageBox.StandardButton.No:
                return suc, msg
        if self.cur_id > 0:
            update_form = self.import_form()
            suc, msg = self.database.insert_query('supply_history', update_form)
        return suc, msg
    
class OrderWindow(AddRecordDialog):
    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent, Ui_add_order_popup())
        self.table_header = ['ID', 'Title', 'Price Unit', 'Quantity', 'Total']
        self.ui: Ui_add_order_popup
        self.ui.tableWidget.setColumnWidth(0, 32)
        self.ui.tableWidget.setColumnWidth(1, 96)
        self.ui.tableWidget.setColumnWidth(2, 48)
        self.ui.tableWidget.setColumnWidth(3, 48)
        self.setupSlot()
    
    def set_database(self, database: DataBase):
        return super().set_database(database) 
    
    def show_popup(self):
        self.ui.txt_cus_id.setText('')
        self.ui.txt_saler.setText('')
        self.ui.created_time.setDateTime(QDateTime.currentDateTime())
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setHorizontalHeaderLabels(self.table_header)
        self.ui.txt_discount.setText('0')
        self.ui.txt_paid.setText('0')
        _, list_prod = self.database.select_query("select product_id, title, output_price from product")
        self.products = {}
        for product in list_prod:
            self.products[product[0]] = {
                'title': product[1],
                'output_price': product[2] 
            }
        self.exec()
    
    def import_form(self):
        data = {}
        data['create_time'] = self.ui.created_time.time().toString("hh:mm:ss")
        data['customer'] = self.ui.txt_cus_id.text()
        data['saler'] = self.ui.txt_saler.text()
        data['discount'] = self.ui.txt_discount.text()
        data['customer_paid'] = self.ui.txt_paid.text()
        data['day'] = self.ui.created_time.date().toString("yyyy-MM-dd")
        return data
    
    def query_data(self):
        suc = msg = None
        confirm_dialog = QMessageBox.question(None, 'Confirm', 'Do you want to continue ?',  QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if confirm_dialog == QMessageBox.StandardButton.No:
                return suc, msg
        update_form = self.import_form()
        suc, msg = self.database.insert_query('bill', update_form)
        if not suc:
            return suc, msg
        added_bill_id = int(msg.split('-')[1])
        detail_table = self.ui.tableWidget
        bill_details = []
        for row in range(100):
            try:
                detail_str = f'({added_bill_id},{int(detail_table.item(row, 0).text())},{int(detail_table.item(row, 3).text())},{int(detail_table.item(row, 4).text())})'
                bill_details.append(detail_str)
            except:
                continue
        bill_details = ',\n'.join(bill_details)
        bill_details += ';'
        query = f'INSERT INTO bill_detail (bill_id, product_id, quantity, price) VALUES \n{bill_details}'
        suc, msg = self.database.query(query=query)
        return suc, msg

    @pyqtSlot(QTableWidgetItem)
    def handleItemChange(self):
        item = self.ui.tableWidget.selectedItems()[0]
        self.ui.tableWidget.itemChanged.disconnect(self.handleItemChange)

        row = item.row()
        if row > 0 and (self.ui.tableWidget.item(row-1, 0) is None or self.ui.tableWidget.item(row-1, 0)) == '':
            self.clearCurrentRow(row)
            self.ui.tableWidget.itemChanged.connect(self.handleItemChange)
            return
        product_id_item = self.ui.tableWidget.item(row, 0)
        if product_id_item is None or product_id_item.text() == '':
            self.clearCurrentRow(row)
            self.ui.tableWidget.itemChanged.connect(self.handleItemChange)
            return
        quantity_item = self.ui.tableWidget.item(row, 3)

        if quantity_item is None or quantity_item.text() == '':
            self.ui.tableWidget.setItem(row, 3,QTableWidgetItem('1'))
            quantity_item = self.ui.tableWidget.item(row, 3)

        product_id = int(product_id_item.text())
        quantity = quantity_item.text()

        price_per_unit = int(self.products[product_id]['output_price'])

        total_price = int(quantity) * price_per_unit
        self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(self.products[product_id]['title']))
        self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(price_per_unit)))
        self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(total_price)))
        total = 0
        for i in range(100):
            try:
                total += int(self.ui.tableWidget.item(i, 4).text())
            except:
                break
        self.ui.txt_total.setText(f'Total: {total}')
        self.ui.tableWidget.itemChanged.connect(self.handleItemChange)
    
    def clearCurrentRow(self, row):
        for i in range(5):
            self.ui.tableWidget.setItem(row, i, QTableWidgetItem(''))

    def setupSlot(self):
        super().setupSlot()
        self.ui.tableWidget.itemChanged.connect(self.handleItemChange)
