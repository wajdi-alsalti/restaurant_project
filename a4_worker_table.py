import sqlite3
import sys
from PyQt5 import QtGui, QtWidgets, uic, QtCore

class Table(QtWidgets.QMainWindow):
    def __init__(self):
        super(Table, self).__init__()
        uic.loadUi('a4_worker_table.ui',self)
        self.tableWidget.setHorizontalHeaderLabels(['Name', 'Phone', 'Email'])
        self.tableWidget.setColumnWidth(0,200)
        self.tableWidget.setColumnWidth(1,200)
        self.tableWidget.setColumnWidth(2,200)
        self.loaddata()

        self.show()

    def loaddata(self):
        conn = sqlite3.connect('saling.db')
        c = conn.cursor()

        # how many row we need 
        self.tableWidget.setRowCount(20)

        sql_order = f'SELECT salesman_name, salesman_number, salesman_email FROM Administration'
        c.execute(sql_order)

        items = c.fetchall()

        row_number = 0
        for row in items:
            # set item in table |  start with0| col|  index the tuple to put in table
            self.tableWidget.setItem(row_number, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(row_number, 2, QtWidgets.QTableWidgetItem(row[2]))

            row_number += 1

        conn.commit()
        conn.close()



# app = QtWidgets.QApplication(sys.argv)
# window = Table()
# sys.exit(app.exec_())