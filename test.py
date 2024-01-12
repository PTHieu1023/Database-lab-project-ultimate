from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget,QPushButton
from PyQt6.QtCore import Qt, pyqtSlot

class BillTableWidget(QTableWidget):
    def __init__(self):
        super().__init__()

        self.setColumnCount(5)
        self.setHorizontalHeaderLabels(['Product ID', 'Product Title', 'Quantity', 'Price/Unit', 'Total Price'])

        # Set up the signals for cell changes
        self.itemChanged.connect(self.handleItemChange)

    @pyqtSlot(QTableWidgetItem)
    def handleItemChange(self, item):
        if item.column() == 0 or item.column() == 2:  # Check if the change is in the product_id or quantity column
            row = item.row()
            product_id_item = self.item(row, 0)
            quantity_item = self.item(row, 2)

            if product_id_item is not None and quantity_item is not None:
                product_id = product_id_item.text()
                quantity = quantity_item.text()

                # Perform your calculations here based on product_id and quantity
                # For example, update price/unit and total price columns

                # Example: Update price/unit (column 3) and total price (column 4)
                price_per_unit = 10  # Replace this with your logic to get the actual price per unit
                total_price = int(quantity) * price_per_unit

                self.setItem(row, 3, QTableWidgetItem(str(price_per_unit)))
                self.setItem(row, 4, QTableWidgetItem(str(total_price)))

    def clearCurrentRow(self):
        current_row = self.currentRow()
        self.setItem(current_row, 0, QTableWidgetItem(''))  # Clear the content of the specified cell
        self.setItem(current_row, 1, QTableWidgetItem(''))  # Clear the content of the specified cell
        self.setItem(current_row, 3, QTableWidgetItem(''))  # Clear the content of the specified cell
# Example usage
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Bill Table')
        self.setGeometry(100, 100, 800, 600)

        self.tableWidget = BillTableWidget()
        self.tableWidget.setRowCount(5)  # Set the number of rows as needed

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

        # Example button to clear the current row
        clearButton = QPushButton('Clear Current Row', self)
        clearButton.clicked.connect(self.tableWidget.clearCurrentRow)
        layout.addWidget(clearButton)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
