import matplotlib.pyplot as plt
import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from a3_sell_window import Ui
from a4_worker_table import Table


class main_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(main_window, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('a2_adminWindow.ui', self)  # Load the .ui file

        self.list_of_worker = []
        self.list_of_numberOfSales = []

        self.sales_btn.clicked.connect(lambda: self.open_sell_window())
        self.graf_sales_btn.clicked.connect(lambda : self.show_graf())
        self.workerInfo_btn.clicked.connect(lambda: self.open_table())

        self.show()
    #--------------------------------------------------------------------------------------------------------#
    """ open the sale window and destroy admin window, userName add in data base that the admin had login """
    def open_sell_window(self):
        self.open_sellWindow = Ui(userName_fromDB='admin')
        self.open_sellWindow.show()
        self.destroy()

    """ to open the table from class Table in a4_worker_table """
    def open_table(self):
        self.window = Table()
        self.window.show()

    #--------------------------------------------------------------------------------------------------------#
    """ connect to db and bring the employee names of each and return the list of the names """
    def workerName_list(self):
        self.conn = sqlite3.connect('saling.db')

        self.c = self.conn.cursor()
        self.sql_excute_order = """ SELECT salesman_name , count(salesman_name) as [number of sales] 
                                    FROM daily_sale GROUP BY salesman_name; """

        self.c.execute(self.sql_excute_order)

        self.list_worker_salesNumber = self.c.fetchall()
        for worker_names in self.list_worker_salesNumber:
            self.list_of_worker.append(worker_names[0])

        self.conn.commit()
        self.conn.close()

        return self.list_of_worker

    """ connect to db and bring many time sales of each  and return number of sales for every employee"""
    def sales_time(self):
        self.conn = sqlite3.connect('saling.db')

        self.c = self.conn.cursor()
        self.sql_excute_order = """ SELECT salesman_name , count(salesman_name) as [number of sales] 
                                    FROM daily_sale GROUP BY salesman_name """

        self.c.execute(self.sql_excute_order)

        self.list_worker_salesNumber = self.c.fetchall()
        for worker_names in self.list_worker_salesNumber:
            self.list_of_numberOfSales.append(worker_names[1])

        # max number used to make y axis in plot draw the max number of sales  
        self.max_numberOfSales = max(self.list_of_numberOfSales)

        self.conn.commit()
        self.conn.close()

        return self.list_of_numberOfSales
    #--------------------------------------------------------------------------------------------------------#
    """ draw plot using matplotlib  """
    def show_graf(self):
        x_values = self.workerName_list()
        y_values = self.sales_time()
        plt.figure(figsize=(12, 9))
        
        plt.bar(x_values, y_values)

        plt.suptitle('Total Numbers of Sales')

        # Set the range for each axis.
        plt.axis([-0.5, len(self.list_of_worker), 0, self.max_numberOfSales + 1])
        
        # clear the lists after showing cause when clicked the grafh button again will appends more items 
        self.workerName_list().clear()
        self.sales_time().clear()

        plt.show()
    
    #--------------------------------------------------------------------------------------------------------#


# app = QtWidgets.QApplication(sys.argv)
# ui = main_window()
# sys.exit(app.exec_())

# # manager = QtWidgets.QMai()