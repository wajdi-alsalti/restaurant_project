from PyQt5 import QtCore, QtGui, QtWidgets, uic
from a3_sell_window import Ui
import sys


class main_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(main_window, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('mainwidget.ui', self)  # Load the .ui file

        self.buying_btn.clicked.connect(lambda: self.open_sell_window())
        self.show()

    def open_sell_window(self):
        self.open_sellWindow = Ui()
        self.open_sellWindow.show()
        self.destroy()


# app = QtWidgets.QApplication(sys.argv)
# manager = QtWidgets.QMainWindow()
# ui = main_window()
# sys.exit(app.exec_())
