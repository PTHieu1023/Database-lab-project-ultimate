from PyQt6.QtWidgets import *

from Backend.DataBaseHandle import DataBase
from UI.UI_Element_Controler import *
from UI.form_ui import Ui_main_screen
from popup import *

from detail_info import *

class SuperMarketManagerment(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_main_screen()
        self.ui.setupUi(self)
        self.general_view_controller = GeneralViewController(self)
        self.staff_view_controller = StaffViewController(self)
        self.customer_view_controller = CustomerViewControler(self)
        self.setupSlot()
        self.database: DataBase = None
    
    def setup_database(self, database):
        self.database = database
        self.general_view_controller.set_database(database=database)
        self.staff_view_controller.set_database(database=database)
        self.customer_view_controller.set_database(database=database)

    def setupSlot(self):
        cui = self.ui
        self.general_view_controller.setupSlot()
        cui.btn_order.toggled.connect(lambda:cui.stack_content_pages.setCurrentIndex(1))
        cui.btn_product.toggled.connect(lambda:cui.stack_content_pages.setCurrentIndex(2))
        self.customer_view_controller.setupSlot()
        self.staff_view_controller.setupSlot()

    
    def on_open_dashboard(self):
        pass


class Controller:
    def __init__(self, root, popup = None) -> None:
        self.root = root
        self.popup = popup
        self.ui: Ui_main_screen = self.root.ui
        self.database = None
    
    def set_database(self, database):
        self.database = database
        if self.popup:
            self.popup.set_database(database=database)

class GeneralViewController(Controller):
    def __init__(self, root, popup=None) -> None:
        super().__init__(root, popup)

    def setupSlot(self):
        self.ui.btn_dashboard.clicked.connect(self.on_open_view)
        self.ui.btn_exe_query.clicked.connect(self.on_exe_btn_clicked)


    def on_open_view(self):
        self.ui.stack_content_pages.setCurrentIndex(0)
    
    def on_exe_btn_clicked(self):
        query = self.ui.txt_query.toPlainText()
        header, values = self.database.select_query(query)
        if isinstance(header, list):
            update_table(self.ui.table_result, result=values, header=header)
            QMessageBox.information(self.root, "Information", f"Selected {len(values)}")
        elif header:
            QMessageBox.information(self.root, 'Information', values)
        else:
            QMessageBox.information(self.root, 'Error', values)


class StaffViewController(Controller):
    def __init__(self, root:SuperMarketManagerment) -> None:
        super().__init__(root, StaffWindow())
   
    def setupSlot(self):
        self.ui.btn_staff.toggled.connect(self.on_open_staff_view)
        self.ui.btn_add_staff.clicked.connect(lambda:self.popup.show_popup())
        self.popup.inserted_record.connect(self.on_open_staff_view)
        self.ui.table_staff.itemSelectionChanged.connect(self.view_detail_staff)
        self.ui.btn_del_staff.clicked.connect(self.delete_current_staff)
        self.ui.btn_update_staff.clicked.connect(self.update_current_staff)
        self.ui.txt_search_staff.textChanged.connect(self.on_open_staff_view)
    
    def get_current_staff_id(self):
        selected_rows = self.ui.table_staff.selectedItems()
        if not selected_rows:
            return None
        staff_id = selected_rows[0].text()
        return staff_id

    def on_open_staff_view(self):
        table = self.ui.table_staff
        filter_str = self.ui.txt_search_staff.text()
        filter_str.replace(' ', '')
        header, staff_list = self.database.select_query(f"""
            SELECT 
                s.staff_id as "ID", CONCAT_WS(' ', s.first_name, s.last_name) as "NAME", 
                r.role as "ROLE", s.salary AS "SALARY" 
            FROM 
                staff as s 
            LEFT JOIN 
                staff_role as r ON s.role = r.staff_role_id
            WHERE
                LOWER(CONCAT(s.first_name, s.last_name)) LIKE '%{filter_str}%';
            
        """)
        update_table(table=table, result=staff_list, header= header)
        table.setColumnWidth(0, 64)
        table.setColumnWidth(1, 256)
        table.setColumnWidth(2, 128)
        self.ui.stack_content_pages.setCurrentIndex(4)
        self.view_detail_staff()
    
    def view_detail_staff(self):
        staff_id = self.get_current_staff_id()
        if staff_id is None:
            self.ui.info_staff.setText('')
            return None
        title, info = self.database.select_query(f"""
            SELECT 
	            s.staff_id, concat_ws(' ', s.first_name, s.last_name) as fname, s.dob, s.telephone,
                r.role, s.salary, s.email, s.address, s.start_working_date, s.working_type, 
                s.end_working_date
            FROM staff as s LEFT JOIN staff_role as r ON r.staff_role_id = s.role
            WHERE s.staff_id = {staff_id}""")
        staff_info = dict(zip(title, info[0]))
        str_staff_info = export_data(staff_detail_format, staff_info)
        self.ui.info_staff.setText(str_staff_info)
    
    def update_current_staff(self):
        current_id = self.get_current_staff_id()
        if current_id is None:
            QMessageBox.information(self.root, "Information", "No staff selected.")
            return
        title, info = self.database.select_query(f"SELECT * FROM staff WHERE staff_id = {current_id}")
        staff_info = dict(zip(title, info[0]))
        # header = f'<html><head/><body><p align="center"><span style=" font-size:36pt;">Update - {current_id}</span></p></body></html>'
        self.popup.show_popup(staff_info=staff_info)

    def delete_current_staff(self):
        current_id = self.get_current_staff_id()
        if current_id is None:
            QMessageBox.information(self.root, "Information", "No staff selected.")
            return
        
        confirm_dialog = QMessageBox.question(self.root, 'Confirmation',f'Are you sure you want to delete staff {current_id}?', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)

        if confirm_dialog == QMessageBox.StandardButton.No:
            return
        suc, msg = self.database.delete_query('staff', staff_id = current_id)
        self.on_open_staff_view()
        if suc:
            QMessageBox.information(self.root, "Information", msg)
        else:
            QMessageBox.information(self.root, "Error", msg)

class CustomerViewControler(Controller):
    def __init__(self, root: SuperMarketManagerment) -> None:
        super().__init__(root=root, popup=CustomerWindow())
    
    def setupSlot(self):
        self.ui.btn_customer.toggled.connect(self.on_open_customer_view)
        self.ui.btn_add_customer.clicked.connect(lambda:self.popup.show_popup())
        self.popup.inserted_record.connect(self.on_open_customer_view)
        self.ui.table_customer.itemSelectionChanged.connect(self.view_detail)
        self.ui.btn_del_customer.clicked.connect(self.delete_current)
        self.ui.btn_update_customer.clicked.connect(self.update_current)
        self.ui.txt_search_customer.textChanged.connect(self.on_open_customer_view)

    def get_current_id(self):
        selected_rows = self.ui.table_customer.selectedItems()
        if not selected_rows:
            first_row_item = self.ui.table_customer.item(0, 0)
            if first_row_item:
                return first_row_item.text()
            else:
                return None
        cur_id = selected_rows[0].text()
        return cur_id

    def on_open_customer_view(self):
        table = self.ui.table_customer
        filter_str = self.ui.txt_search_customer.text()
        filter_str.replace(' ', '')
        header, result = self.database.select_query(f'SELECT customer_id as "ID", CONCAT_WS(\' \', first_name, last_name) as "NAME", telephone as "TEL", bonus_point as "POINT" FROM customer as c WHERE LOWER(CONCAT(c.first_name, c.last_name)) LIKE \'%{filter_str}%\';')
        update_table(table=table, result=result, header= header)
        table.setColumnWidth(0, 64)
        self.ui.stack_content_pages.setCurrentIndex(3)
        self.view_detail()

    def view_detail(self):
        id = self.get_current_id()
        if id is None:
            self.ui.info_customer.setText('')
            return None
        title, info = self.database.select_query(f"""
            SELECT
                c.customer_id,
                CONCAT_WS(' ', c.first_name, c.last_name) AS full_name,
                c.telephone,
                c.email,
                c.address,
                c.bonus_point,
                COUNT(b.bill_id) AS order_count,
                COALESCE(SUM(b.total_pay), 0) AS total_purchased
            FROM
                customer AS c
            LEFT JOIN (
                SELECT
                    bill.customer AS customer,
                    bill.bill_id AS bill_id,
                    SUM(bill_detail.price) AS total_pay
                FROM
                    bill
                JOIN bill_detail ON bill.bill_id = bill_detail.bill_id
                GROUP BY bill.bill_id
            ) AS b ON b.customer = c.customer_id
            WHERE c.customer_id = {id}
            GROUP BY
                c.customer_id
        """)
        info = dict(zip(title, info[0]))
        str_info = export_data(customer_format, info)
        self.ui.info_customer.setText(str_info)
    
    def delete_current(self):
        current_id = self.get_current_id()
        if current_id is None:
            QMessageBox.information(self.root, "Information", "No record selected.")
            return
        
        confirm_dialog = QMessageBox.question(self.root, 'Confirmation',f'Are you sure you want to delete this record {current_id}?', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)

        if confirm_dialog == QMessageBox.StandardButton.No:
            return
        suc, msg = self.database.delete_query('customer', customer_id = current_id)
        self.on_open_customer_view()
        if suc:
            QMessageBox.information(self.root, "Information", msg)
        else:
            QMessageBox.information(self.root, "Error", msg)


    def update_current(self):
        current_id = self.get_current_id()
        if current_id is None:
            QMessageBox.information(self.root, "Information", "No record selected.")
            return
        title, info = self.database.select_query(f"SELECT * FROM customer WHERE customer_id = {current_id}")
        info = dict(zip(title, info[0]))
        self.popup.show_popup(info = info)

class ProductViewControler(Controller):
    def __init__(self, root: SuperMarketManagerment) -> None:
        super().__init__(root=root, popup=CustomerWindow())
    
    def setupslot(self):
        self.ui.btn_customer.toggled.connect(self.on_open_customer_view)
        self.ui.btn_add_customer.clicked.connect(lambda:self.popup.show_popup())
        self.popup.inserted_record.connect(self.on_open_customer_view)
        self.ui.table_customer.itemSelectionChanged.connect(self.view_detail)
        self.ui.btn_del_customer.clicked.connect(self.delete_current)
        self.ui.btn_update_customer.clicked.connect(self.update_current)

    def get_current_id(self):
        pass

    def on_open_customer_view(self):
        pass

    def view_detail(self):
        pass
    
    def delete_current(self):
        pass

    def update_current(self):
        pass

class OrderViewControler(Controller):
    def __init__(self, root: SuperMarketManagerment) -> None:
        super().__init__(root=root, popup=CustomerWindow())
    
    def setupslot(self):
        self.ui.btn_customer.toggled.connect(self.on_open_customer_view)
        self.ui.btn_add_customer.clicked.connect(lambda:self.popup.show_popup())
        self.popup.inserted_record.connect(self.on_open_customer_view)
        self.ui.table_customer.itemSelectionChanged.connect(self.view_detail)
        self.ui.btn_del_customer.clicked.connect(self.delete_current)
        self.ui.btn_update_customer.clicked.connect(self.update_current)

    def get_current_id(self):
        pass

    def on_open_customer_view(self):
        pass

    def view_detail(self):
        pass
    
    def delete_current(self):
        pass

    def update_current(self):
        pass