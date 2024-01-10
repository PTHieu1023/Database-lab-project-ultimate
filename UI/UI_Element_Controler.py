from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem

def update_table(table: QTableWidget, result, header):
    table.clear()
    if len(result) > 0:
        table.setRowCount(len(result))
    else:
        table.setRowCount(1)
    table.setColumnCount(len(header))

    table.setHorizontalHeaderLabels(header)

    # Batch update
    table.setUpdatesEnabled(False)

    for row_num, row_data in enumerate(result):
        for col_num, col_data in enumerate(row_data):
            item = QTableWidgetItem()
            item.setData(0, str(col_data))  # 0 represents the role for displaying text
            table.setItem(row_num, col_num, item)

    table.setUpdatesEnabled(True)
    table.resizeColumnsToContents()

