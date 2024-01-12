from PyQt6.QtWidgets import *

from Backend.DataBaseHandle import DataBase
from Backend import QuerrySet
from UI.form_ui import Ui_main_screen
from popup import *

from Extentions.detail_info import *

class SuperMarketManagerment(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_main_screen()
        self.ui.setupUi(self)
        self.controllers = []
        self.general_view_controller = GeneralViewController(self)
        self.staff_view_controller = StaffViewController(self)
        self.customer_view_controller = CustomerViewControler(self)
        self.product_view_controller = ProductViewControler(self)
        self.order_view_controller = OrderViewControler(self)
        self.setupSlot()
        self.database: DataBase = None
    
    def setup_database(self, database):
        self.database = database
        for controler in self.controllers:
            controler.set_database(database)

    def setupSlot(self):
        for controler in self.controllers:
            controler.setupSlot()


class Controller:
    def __init__(self, root, popup = None) -> None:
        self.root: SuperMarketManagerment = root
        self.root.controllers.append(self)
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
            # update_table(self.ui.table_result, result=values, header=header)
            QMessageBox.information(self.root, "Information", f"Selected {len(values)}")
        elif header:
            QMessageBox.information(self.root, 'Information', values)
        else:
            QMessageBox.information(self.root, 'Error', values)


class StaffViewController(Controller):
    def __init__(self, root:SuperMarketManagerment) -> None:
        super().__init__(root, StaffWindow())
        self.header = []
        self.staff_list = []
   
    def setupSlot(self):
        self.ui.btn_staff.toggled.connect(self.on_open_view)
        self.ui.btn_add_staff.clicked.connect(lambda:self.popup.show_popup())
        self.popup.inserted_record.connect(self.on_open_view)
        # self.ui.table_staff.itemSelectionChanged.connect(self.view_detail_staff)
        self.ui.table_staff.ui.table.itemSelectionChanged.connect(self.view_detail_staff)
        self.ui.btn_del_staff.clicked.connect(self.delete_current_staff)
        self.ui.btn_update_staff.clicked.connect(self.update_current_staff)
        self.ui.txt_search_staff.textChanged.connect(self.set_list)
    
    def get_current_staff_id(self):
        selected_rows = self.ui.table_staff.get_current_item()
        if not selected_rows:
            return None
        staff_id = selected_rows[0].text()
        return staff_id

    def on_open_view(self):
        table = self.ui.table_staff
        filter_str = self.ui.txt_search_staff.text()
        filter_str.replace(' ', '')
        self.header, self.staff_list = self.database.select_query(QuerrySet.GET_ALL_STAFF)
        self.set_list()
        table.ui.table.setColumnWidth(0, 64)
        table.ui.table.setColumnWidth(1, 256)
        table.ui.table.setColumnWidth(2, 128)
        self.ui.stack_content_pages.setCurrentIndex(4)
        self.view_detail_staff()
    
    def view_detail_staff(self):
        staff_id = self.get_current_staff_id()
        if staff_id is None:
            self.ui.info_staff.setText('')
            return None
        title, info = self.database.select_query(QuerrySet.GET_DETAIL_STAFF_BY_ID.format(id = staff_id))
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
        self.on_open_view()
        if suc:
            QMessageBox.information(self.root, "Information", msg)
        else:
            QMessageBox.information(self.root, "Error", msg)

    def set_list(self):
        filter_str = self.ui.txt_search_staff.text().lower()
        filter_list = []
        if filter_str is None or filter_str == '':
            filter_list = self.staff_list
        else:
            filter_list = list(filter(lambda x: filter_str in str(x[1]).lower(), self.staff_list))
        self.ui.table_staff.update_data(data=filter_list, header= self.header)

class CustomerViewControler(Controller):
    def __init__(self, root: SuperMarketManagerment) -> None:
        super().__init__(root=root, popup=CustomerWindow())
        self.full_data = []
    
    def setupSlot(self):
        self.ui.btn_customer.toggled.connect(self.on_open_view)
        self.ui.btn_add_customer.clicked.connect(lambda:self.popup.show_popup())
        self.popup.inserted_record.connect(self.on_open_view)
        self.ui.table_customer.ui.table.itemSelectionChanged.connect(self.view_detail)
        self.ui.btn_del_customer.clicked.connect(self.delete_current)
        self.ui.btn_update_customer.clicked.connect(self.update_current)
        self.ui.txt_search_customer.textChanged.connect(self.set_list)

    def get_current_id(self):
        selected_rows = self.ui.table_customer.get_current_item()
        if not selected_rows:
            return None
        id = selected_rows[0].text()
        return id

    def on_open_view(self):
        table = self.ui.table_customer
        filter_str = self.ui.txt_search_customer.text()
        filter_str.replace(' ', '')
        self.header, self.full_data = self.database.select_query(QuerrySet.GET_ALL_CUSTOMER)
        self.set_list()
        table.ui.table.setColumnWidth(0, 64)
        table.ui.table.setColumnWidth(1, 160)
        table.ui.table.setColumnWidth(2, 96)
        table.ui.table.setColumnWidth(3, 160)
        self.ui.stack_content_pages.setCurrentIndex(3)
        self.view_detail()

    def view_detail(self):
        id = self.get_current_id()
        if id is None:
            self.ui.info_customer.setText('')
            return None
        title, info = self.database.select_query(QuerrySet.GET_DETAIL_CUSTOMER_BY_ID.format(id = id))
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
        self.on_open_view()
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

    def set_list(self):
        filter_str = self.ui.txt_search_customer.text()
        if filter_str is None or filter_str == '':
            self.ui.table_customer.update_data(data=self.full_data, header=self.header)
        filtered_list = list(filter(lambda x: filter_str.lower() in str(x[1]).lower(), self.full_data))
        self.ui.table_customer.update_data(data=filtered_list, header=self.header)

class ProductViewControler(Controller):
    def __init__(self, root: SuperMarketManagerment) -> None:
        super().__init__(root=root, popup=ProductWindow())
        self.full_data = []
    
    def setupSlot(self):
        self.ui.btn_product.toggled.connect(self.on_open_view)
        self.popup.inserted_record.connect(self.on_open_view)
        self.ui.table_product.ui.table.itemSelectionChanged.connect(self.view_detail)
        self.ui.btn_update_product.clicked.connect(self.update_current)
        self.ui.txt_search_product.textChanged.connect(self.set_list)

    def get_current_id(self):
        selected_rows = self.ui.table_product.get_current_item()
        if not selected_rows:
            return None
        id = selected_rows[0].text()
        return id

    def on_open_view(self):
        table = self.ui.table_product
        filter_str = self.ui.txt_search_product.text()
        filter_str.replace(' ', '')
        self.header, self.full_data = self.database.select_query(QuerrySet.GET_ALL_PRODUCT)
        self.set_list()
        table.ui.table.setColumnWidth(0, 64)
        table.ui.table.setColumnWidth(1, 192)
        table.ui.table.setColumnWidth(2, 96)
        table.ui.table.setColumnWidth(3, 96)
        self.ui.stack_content_pages.setCurrentIndex(2)
        self.view_detail()

    def view_detail(self):
        id = self.get_current_id()
        if id is None:
            self.ui.info_product.setText('')
            return None
        title, info = self.database.select_query(QuerrySet.GET_DETAIL_PRODUCT_BY_ID.format(id = id))
        info = dict(zip(title, info[0]))
        _, fb_list = self.database.select_query(QuerrySet.GET_PRODUCT_FEEDBACK_BY_ID.format(id = id))
        feedbacks = [product_feedback.format(customer = fb[6], customer_id = fb[2], create_time = fb[5], rating = fb[4], comment = fb[3]) for fb in fb_list]
        info['feedback'] = '\n'.join(feedbacks)
        str_info = export_data(product_format, info)
        self.ui.info_product.setText(str_info)
    
    def update_current(self):
        current_id = self.get_current_id()
        if current_id is None:
            QMessageBox.information(self.root, "Information", "No record selected.")
            return
        title, info = self.database.select_query(f"SELECT * FROM product WHERE product_id = {current_id};")
        info = dict(zip(title, info[0]))
        self.popup.show_popup(info = info)

    def set_list(self):
        filter_str = self.ui.txt_search_product.text()
        if filter_str is None or filter_str == '':
            self.ui.table_product.update_data(data=self.full_data, header=self.header)
        filtered_list = list(filter(lambda x: filter_str.lower() in str(x[1]).lower(), self.full_data))
        self.ui.table_product.update_data(data=filtered_list, header=self.header)


class OrderViewControler(Controller):
    def __init__(self, root: SuperMarketManagerment) -> None:
        super().__init__(root=root, popup=OrderWindow())
    
    def setupSlot(self):
        self.ui.btn_order.toggled.connect(self.on_open_view)
        self.ui.btn_add_order.clicked.connect(lambda:self.popup.show_popup())
        self.popup.inserted_record.connect(self.on_open_view)
        self.ui.table_order.ui.table.itemSelectionChanged.connect(self.view_detail)

    def get_current_id(self):
        selected_rows = self.ui.table_order.get_current_item()
        if not selected_rows:
            return None
        id = selected_rows[0].text()
        return id

    def on_open_view(self):
        table = self.ui.table_order
        filter_str = self.ui.txt_search_order.text()
        filter_str.replace(' ', '')
        self.header, self.full_data = self.database.select_query(QuerrySet.GET_ALL_ORDER)
        self.set_list()
        table.ui.table.setColumnWidth(0, 64)
        table.ui.table.setColumnWidth(1, 128)
        table.ui.table.setColumnWidth(2, 128)
        table.ui.table.setColumnWidth(3, 128)
        self.ui.stack_content_pages.setCurrentIndex(1)
        self.view_detail()

    def view_detail(self):
        id = self.get_current_id()
        if id is None:
            self.ui.info_product.setText('')
            return None
        title, info = self.database.select_query(QuerrySet.GET_DETAIL_ORDER_BY_ID.format(id = id))
        info = dict(zip(title, info[0]))
        _, pd_list = self.database.select_query(QuerrySet.GET_ORDER_DETAIL_BY_ID.format(id = id))
        products = [bill_detail.format(product_id = p[1], title = p[2], supplier = p[3], quantity = p[4], price =p[5]) for p in pd_list]
        info['detail'] = '\n'.join(products)
        str_info = export_data(order_format, info)
        self.ui.info_order.setText(str_info)

    def set_list(self):
        filter_str = self.ui.txt_search_product.text()
        if filter_str is None or filter_str == '':
            self.ui.table_order.update_data(data=self.full_data, header=self.header)
        filtered_list = list(filter(lambda x: filter_str.lower() in str(x[1]).lower(), self.full_data))
        self.ui.table_product.update_data(data=filtered_list, header=self.header)