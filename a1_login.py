import sys
import sqlite3
from datetime import datetime
from PyQt5 import QtGui, QtWidgets, uic, QtCore
from a2_admin_window import main_window
from a3_sell_window import Ui


class Login(QtWidgets.QWidget):
    def __init__(self):
        super(Login, self).__init__()
        uic.loadUi('login_gui.ui', self)

        self.login_btn.clicked.connect(lambda : self.approve())

        self.wrong_label.setHidden(True)

        self.show()

    #-----------------------------------------------------------------------------------------------------#
    ''' the command of the login button '''

    def approve(self):
        # just for admin
        if self.bring_userName_fromDB(1) == self.user_name_line.text() and self.bring_pass_fromDB(1) == self.password_line.text():
            self.addTimeLogin_inmDB()
            self.open_main_window()
            self.destroy()

        else:
            self.wrong_label.setHidden(False)
        # loop for all worker to open the sell window
        for i in range(2,self.many_worker()+1):
            if self.bring_userName_fromDB(i) == self.user_name_line.text() and self.bring_pass_fromDB(i) == self.password_line.text():
                self.open_sell_window()
                self.addTimeLogin_inmDB()
                self.destroy()
        
    #-----------------------------------------------------------------------------------------------------#
    """ functions to open the sell window and maine """
    def open_main_window(self):
        self.open_main = main_window()
        self.open_main.show()

    def open_sell_window(self):
        self.sell_main = Ui(userName_fromDB=self.userName_db)
        self.sell_main.show()

    #-----------------------------------------------------------------------------------------------------#
    """ functions to bring the name and password of the user from data base and insert the login time in db """
    def bring_userName_fromDB(self,row):
        self.conn = sqlite3.connect('saling.db')

        self.c = self.conn.cursor()
        self.sql_excute_order = f""" SELECT salesman_login_name, salesman_name 
                                FROM Administration WHERE rowid={row} """

        self.c.execute(self.sql_excute_order)

        self.name_pass = self.c.fetchone()

        self.loginName_db = self.name_pass[0]
        self.userName_db = self.name_pass[1]

        self.conn.commit()
        self.conn.close()
        return self.loginName_db

    def bring_pass_fromDB(self,row):
        self.conn = sqlite3.connect('saling.db')

        self.c = self.conn.cursor()
        self.sql_excute_order = f""" SELECT salesman_password 
                                FROM Administration WHERE rowid={row} """

        self.c.execute(self.sql_excute_order)

        self.name_pass = self.c.fetchone()

        self.pass_db = self.name_pass[0]

        self.conn.commit()
        self.conn.close()
        return self.pass_db


    def addTimeLogin_inmDB(self):
        login_day = datetime.now().strftime("%d-%m-%Y")
        login_time = datetime.now().strftime("%H:%M:%S")
        self.conn = sqlite3.connect('saling.db')

        self.c = self.conn.cursor()
        self.sql_excute_order = """ INSERT INTO login_time VALUES (?,?,?) """

        self.c.execute(self.sql_excute_order,(self.userName_db,login_day,login_time))

        self.conn.commit()
        self.conn.close()

    # return a number of the employee in db
    def many_worker(self):
        self.conn = sqlite3.connect('saling.db')

        self.c = self.conn.cursor()
        self.sql_excute_order = """ SELECT COUNT(*) FROM Administration"""

        self.c.execute(self.sql_excute_order)
        self.worker_number = self.c.fetchone()

        self.conn.commit()
        self.conn.close()
        return self.worker_number[0]

    #-----------------------------------------------------------------------------------------------------#



# run the app 
app = QtWidgets.QApplication(sys.argv)  
window = Login() 
app.exec_()  # Start the app

