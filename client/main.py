# PyQt5 Application

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from client.ui.main_window import Ui_MainWindow  # Import the generated UI class

class InventoryApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Connect PyQt5 signals and slots here

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InventoryApp()
    window.show()
    sys.exit(app.exec_())
