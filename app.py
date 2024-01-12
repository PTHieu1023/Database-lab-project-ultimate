import sys
from PyQt6.QtWidgets import QApplication
from main_screen import SuperMarketManagerment

from Backend.DataBaseHandle import DataBase

class App:
    def __init__(self) -> None:
        self.db = DataBase()
        self.app = QApplication(sys.argv)
        self.main_window = SuperMarketManagerment()
        self.main_window.setup_database(self.db)
        self.main_window.show()
        self.app.aboutToQuit.connect(self.db.log_out)
        
    def run(self):
        sys.exit(self.app.exec())

App().run()