import smtplib
import sqlite3
import sys
import time
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox


class Ui(QtWidgets.QWidget):
    def __init__(self, userName_fromDB): # pass user name in class to bring it the value from db when it login
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('a3_sell_window.ui', self)  # Load the .ui file
        # -----------------------------------------------------------------------------------------------------------------------------------#
        """ all the buttons and with which functions connected"""
        self.userName_fromDB = userName_fromDB
        # numbers buttons
        self.btn_1.clicked.connect(lambda: self.add_item_in_text_editor('1', manytime=1))
        self.btn_2.clicked.connect(lambda: self.add_item_in_text_editor('2', manytime=2))
        self.btn_3.clicked.connect(lambda: self.add_item_in_text_editor('3', manytime=3))
        self.btn_4.clicked.connect(lambda: self.add_item_in_text_editor('4', manytime=4))
        self.btn_5.clicked.connect(lambda: self.add_item_in_text_editor('5', manytime=5))
        self.btn_6.clicked.connect(lambda: self.add_item_in_text_editor('6', manytime=6))
        self.btn_7.clicked.connect(lambda: self.add_item_in_text_editor('7', manytime=7))
        self.btn_8.clicked.connect(lambda: self.add_item_in_text_editor('8', manytime=8))
        self.btn_9.clicked.connect(lambda: self.add_item_in_text_editor('9', manytime=9))
        self.btn_0.clicked.connect(lambda: self.add_item_in_text_editor('0', manytime=0))

        # foods btn
        self.btn_chicken.clicked.connect(lambda: self.add_item_in_text_editor(
                                        f'{self.bringValue_db(1,self.bring_food_name)} = {self.bringValue_db(1,self.bring_food_price)}',
                                        price=float(self.bringValue_db(1,self.bring_food_price))))

        self.btn_beef.clicked.connect(lambda: self.add_item_in_text_editor(
                                        f'{self.bringValue_db(2,self.bring_food_name)} = {self.bringValue_db(2,self.bring_food_price)}',
                                        price=float(self.bringValue_db(2,self.bring_food_price))))

        self.btn_pizza.clicked.connect(lambda: self.add_item_in_text_editor(
                                        f'{self.bringValue_db(3,self.bring_food_name)} = {self.bringValue_db(3,self.bring_food_price)}',
                                        price=float(self.bringValue_db(3,self.bring_food_price))))

        self.btn_salat.clicked.connect(lambda: self.add_item_in_text_editor(
                                        f'{self.bringValue_db(4,self.bring_food_name)} = {self.bringValue_db(4,self.bring_food_price)}',
                                        price=float(self.bringValue_db(4,self.bring_food_price))))

        self.btn_soup.clicked.connect(lambda: self.add_item_in_text_editor(
                                        f'{self.bringValue_db(5,self.bring_food_name)} = {self.bringValue_db(5,self.bring_food_price)}',
                                        price=float(self.bringValue_db(5,self.bring_food_price))))

        self.btn_geyros.clicked.connect(lambda: self.add_item_in_text_editor(
                                        f'{self.bringValue_db(6,self.bring_food_name)} = {self.bringValue_db(6,self.bring_food_price)}',
                                        price=float(self.bringValue_db(6,self.bring_food_price))))

        self.bt_botatao.clicked.connect(lambda: self.add_item_in_text_editor(
                                        f'{self.bringValue_db(7,self.bring_food_name)} = {self.bringValue_db(7,self.bring_food_price)}',
                                        price=float(self.bringValue_db(7,self.bring_food_price))))

        self.btn_ketchup.clicked.connect(lambda: self.add_item_in_text_editor(
                                        f'{self.bringValue_db(8,self.bring_food_name)} = {self.bringValue_db(8,self.bring_food_price)}',
                                        price=float(self.bringValue_db(8,self.bring_food_price))))

        self.btn_mayo.clicked.connect(lambda: self.add_item_in_text_editor(
                                        f'{self.bringValue_db(9,self.bring_food_name)} = {self.bringValue_db(9,self.bring_food_price)}',
                                        price=float(self.bringValue_db(9,self.bring_food_price))))

        # drinks buttons
        self.btn_cola.clicked.connect(lambda: self.add_item_in_text_editor(
                                        f'{self.bringValue_db(1,self.bring_drink_name)} = {self.bringValue_db(1,self.bring_drink_price)}',
                                        price=float(self.bringValue_db(1,self.bring_drink_price))))

        self.btn_fanta.clicked.connect(lambda: self.add_item_in_text_editor(
                                        f'{self.bringValue_db(2,self.bring_drink_name)} = {self.bringValue_db(2,self.bring_drink_price)}',
                                        price=float(self.bringValue_db(2,self.bring_drink_price))))

        self.btn_sevenup.clicked.connect(lambda: self.add_item_in_text_editor(
                                        f'{self.bringValue_db(3,self.bring_drink_name)} = {self.bringValue_db(3,self.bring_drink_price)}',
                                        price=float(self.bringValue_db(3,self.bring_drink_price))))

        self.btn_kaffee.clicked.connect(lambda: self.add_item_in_text_editor(
                                        f'{self.bringValue_db(4,self.bring_drink_name)} = {self.bringValue_db(4,self.bring_drink_price)}',
                                        price=float(self.bringValue_db(4,self.bring_drink_price))))

        self.btn_tee.clicked.connect(lambda: self.add_item_in_text_editor(
                                        f'{self.bringValue_db(5,self.bring_drink_name)} = {self.bringValue_db(5,self.bring_drink_price)}',
                                        price=float(self.bringValue_db(5,self.bring_drink_price))))

        self.btn_capuccino.clicked.connect(lambda: self.add_item_in_text_editor(
                                        f'{self.bringValue_db(6,self.bring_drink_name)} = {self.bringValue_db(6,self.bring_drink_price)}',
                                        price=float(self.bringValue_db(6,self.bring_drink_price))))

        self.btn_beer.clicked.connect(lambda: self.add_item_in_text_editor(
                                        f'{self.bringValue_db(7,self.bring_drink_name)} = {self.bringValue_db(7,self.bring_drink_price)}',
                                        price=float(self.bringValue_db(7,self.bring_drink_price))))

        self.btn_radler.clicked.connect(lambda: self.add_item_in_text_editor(
                                        f'{self.bringValue_db(8,self.bring_drink_name)} = {self.bringValue_db(8,self.bring_drink_price)}',
                                        price=float(self.bringValue_db(8,self.bring_drink_price))))

        self.btn_maonten.clicked.connect(lambda: self.add_item_in_text_editor(
                                        f'{self.bringValue_db(9,self.bring_drink_name)} = {self.bringValue_db(9,self.bring_drink_price)}',
                                        price=float(self.bringValue_db(9,self.bring_drink_price))))


        # buttons
        self.btn_clear.clicked.connect(self.clear_in_text_editor)
        self.btn_minus.clicked.connect(self.flag_delete_price)
        self.btn_multi.clicked.connect(self.flag_multi_price)
        self.btn_equal.clicked.connect(self.equal_the_invoice)
        self.btn_email.clicked.connect(self.send_invoice_email)
        self.btn_return.clicked.connect(self.return_money)

        # -----------------------------------------------------------------------------------------------------------------------------------#

        self.sum_list = []
        self.multi_list = []
        self.minus_list = []
        self.food_list = []
        self.food_list_check = []

        self.aat = '@'
        self.dot = '.'
        self.operation_signal = ''
        self.change_button_command = ''

        # sql order from foods table
        self.bring_food_name = " SELECT foods_name FROM foods where ROWID={} "
        self.bring_food_price = " SELECT foods_price FROM foods where ROWID={} "

        # sql orders from drinks table
        self.bring_drink_name = " SELECT drinks_name FROM drinks where ROWID={} "
        self.bring_drink_price = " SELECT drinks_price FROM drinks where ROWID={} "

        # to open the gui in full screen
        self.showMaximized()

    # -----------------------------------------------------------------------------------------------------------------------------------#
    """ data base connect and insert the amount in db"""

    # connect to db and bring the values from tables
    def bringValue_db(self,row,sql_order):
        conn = sqlite3.connect('saling.db')
        c = conn.cursor()

        bring_value = sql_order.format(row)

        c.execute(bring_value)

        value0 = c.fetchone()
        value1 = value0[0] # return a number not a tuple

        conn.commit()
        conn.close()

        return value1

    # add the price and email from customers in data base
    def add_values_inDailySale(self):
        time = datetime.now().strftime("%d-%m-%Y")
        conn = sqlite3.connect('saling.db')

        self.c = conn.cursor()
        self.bring_value = """ INSERT INTO daily_sale 
                                VALUES (?,?,?,?)  
                        """
        self.c.execute(self.bring_value,(self.userName_fromDB,time,self.total2,self.line_email.text()))

        conn.commit()
        conn.close()

    # -----------------------------------------------------------------------------------------------------------------------------------#

    # flag to change command buttons to write in label
    def return_money(self):
        self.change_button_command = 'to_label'
        self.label_total.setText('')
        self.label_2.setText('Return')

    # -----------------------------------------------------------------------------------------------------------------------------------#
    """functions for subtraction"""
    # add flag and insert - signal
    def flag_delete_price(self):
        if self.textfood.toPlainText() == '':
            pass
        else:
            self.operation_signal = 'minus'
            self.textfood.insertPlainText('-' + '\n')
            self.set_numbers_button_disable(False)

    # to make function can be delete an price from the list
    def delete_price_in_text(self, price, character):
        if self.operation_signal == 'minus':
            self.minus_list.append(price * -2)

            # add items in food list to compare it with food list
            if character in self.food_list:
                self.food_list_check.append(character)

            # will count how many same item in list and if in number check list more than in food list will do things
                if self.food_list_check.count(character) > self.food_list.count(character):
                    self.check_in_list('Error','You have already removed the order')

            else:
                self.check_in_list('Error','Careful Please\nYou can not Subtraction a Value You Did not Insert Before')

    # function to delete the last item if it was not in list before
    def check_in_list(self, error, mes):
        self.undo_write_inText_editor()
        self.pop_up_message(error,mes)
        self.minus_list.pop()
        self.sum_list.pop()

    # -----------------------------------------------------------------------------------------------------------------------------------#
    """functions for multifunction"""
    # add flag for removed and operation and pop last item from sum list
    def flag_multi_price(self):
        try:
            self.operation_signal = 'multi'
            self.removed = self.sum_list.pop()
            self.textfood.insertPlainText('X' + ' ')
            self.set_foods_buttons_enabled(False)
        except IndexError:
            pass

    # to detect the sign of operations and loop for how many time to multi
    def double_number_in_list(self, manytime):
        if self.operation_signal == 'multi':
            try:
                # repeat last item if food list and add in loop to give the same number had multiplicate
                repeat = self.food_list[-1]
                for _i in range(manytime):
                    self.multi_list.append(self.removed)
                    self.food_list.append(repeat)
                # pop last item to have a same number we want to count
                self.food_list.pop()
            except TypeError:
                pass
    # -----------------------------------------------------------------------------------------------------------------------------------#
    """tha main function will change the functionality of buttons too when the change_button_command change it"""
    # to add the name of food and the price in text and then add the price in the list
    def add_item_in_text_editor(self, character, price=0, manytime=None):
        if self.change_button_command != 'to_label':
            self.textfood.insertPlainText(character + '\n')
            self.sum_list.append(price)
            # print(self.sum_list)
            self.delete_price_in_text(price, character)
            self.double_number_in_list(manytime)
            self.textfood.moveCursor(QtGui.QTextCursor.End)  # to move the text down when i add more input

            if self.operation_signal != 'minus':
                self.food_list.append(character)
                print(self.food_list)

            self.show_total()

        elif self.change_button_command == 'to_label':
            self.write_numbers_in_label(character)
        self.operation_signal = ''
        self.set_foods_buttons_enabled(True)
        self.set_numbers_button_disable(True)

    # -----------------------------------------------------------------------------------------------------------------------------------#

    # write the numbers correct
    def write_numbers_in_label(self, character):
        self.label_total.setText(self.label_total.text() + character)
    # -----------------------------------------------------------------------------------------------------------------------------------#

        # pop up messages for warning
    def pop_up_message(self, head, subject):
        self.msg = QMessageBox()
        self.msg.about(self.msg, head, subject)

    # -----------------------------------------------------------------------------------------------------------------------------------#

    # to undo the input in text editor
    def undo_write_inText_editor(self):
        for _y in range(2):
            self.textfood.undo()

    # -----------------------------------------------------------------------------------------------------------------------------------#

    # button clear function to delete the list and the text
    def clear_in_text_editor(self):
        self.operation_signal = ''
        self.change_button_command = ''
        self.label_total.setText('')
        self.textfood.clear()
        self.sum_list.clear()
        self.minus_list.clear()
        self.multi_list.clear()
        self.food_list.clear()
        self.food_list_check.clear()
        self.label_total.setText('0')
        self.btn_return.setEnabled(False)
        self.set_foods_buttons_enabled(True)
        self.label_2.setText('Total :')

    # -----------------------------------------------------------------------------------------------------------------------------------#
    """ press the = and the condition  """
    # btn equal function
    def equal_the_invoice(self):
        if self.textfood.toPlainText() == '':
            pass

        elif self.change_button_command == 'to_label':
            try:
                x = self.label_total.text()
                y = round(eval(str(x) + ' - ' + str(self.total2)), 2)

                if y >= 0:
                    self.label_total.setText(str(x) + ' - ' + str(self.total2) + ' = ' + str(y))
                else:
                    self.pop_up_message('Error', 'Not enough Money')
                    self.label_total.setText('')

            except :
                pass

        else:
            self.show_total()
            self.textfood.insertPlainText('-' * 30 + '\n' + 'Your Total = ' + self.total2)
            self.textfood.moveCursor(QtGui.QTextCursor.End)  # to move the text down when i add more input
            self.add_values_inDailySale()
            self.btn_return.setEnabled(True)
        self.btn_equal.setEnabled(False)

    # -----------------------------------------------------------------------------------------------------------------------------------#

    # to disable the foods buttons when we press X
    def set_foods_buttons_enabled(self, command):
        self.btn_chicken.setEnabled(command)
        self.btn_beef.setEnabled(command)
        self.btn_pizza.setEnabled(command)
        self.btn_salat.setEnabled(command)
        self.btn_soup.setEnabled(command)
        self.btn_geyros.setEnabled(command)
        self.bt_botatao.setEnabled(command)
        self.btn_ketchup.setEnabled(command)
        self.btn_mayo.setEnabled(command)
        self.btn_cola.setEnabled(command)
        self.btn_fanta.setEnabled(command)
        self.btn_sevenup.setEnabled(command)
        self.btn_kaffee.setEnabled(command)
        self.btn_tee.setEnabled(command)
        self.btn_capuccino.setEnabled(command)
        self.btn_beer.setEnabled(command)
        self.btn_radler.setEnabled(command)
        self.btn_maonten.setEnabled(command)
        self.btn_minus.setEnabled(command)
        self.btn_equal.setEnabled(command)

    # to disable the numbers buttons when we press -
    def set_numbers_button_disable(self,command):
        self.btn_1.setEnabled(command)
        self.btn_2.setEnabled(command)
        self.btn_3.setEnabled(command)
        self.btn_4.setEnabled(command)
        self.btn_5.setEnabled(command)
        self.btn_6.setEnabled(command)
        self.btn_7.setEnabled(command)
        self.btn_8.setEnabled(command)
        self.btn_9.setEnabled(command)
        self.btn_0.setEnabled(command)
        self.btn_multi.setEnabled(command)
        self.btn_equal.setEnabled(command)

    # -----------------------------------------------------------------------------------------------------------------------------------#
    """ send an email with the invoice to the customer  """
    # a function to check if the email text is empty or not
    def is_empty_email_line(self):
        if self.the_email_address == '':
            return True
        else:
            return False

    # function to send the invoice from the email restaurant to the email clain
    def send_invoice_email(self):
        self.gmail_user = 'aboalirestaurant1991@gmail.com'
        self.gmail_password = 'wajdiaboali1991'
        self.sent_from = self.gmail_user
        self.the_email_address = self.line_email.text()  # 1
        self.to_check_character = list(self.the_email_address)

        if self.is_empty_email_line():
            self.pop_up_message('Error', 'There is no Email address')

        elif (self.aat in self.to_check_character and self.dot in self.to_check_character):
            self.subject = 'Your Invoice'
            text_box_value = self.textfood.toPlainText()
            self.body = ("""\nYour Order From Abo Ali Restaurant\n{}
                        \n Thank You For Your Perfectly Choice, We are waiting for You next Time """.format(
                text_box_value))

            email_text = """\
            From: %s
            To: %s
            Subject: %s

            %s
            """ % (self.sent_from, ", ".join(self.to_check_character), self.subject, self.body)
            self.line_email.setText('')

            try:
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.ehlo()
                server.login(self.gmail_user, self.gmail_password)
                server.sendmail(self.sent_from, self.to, email_text)
                server.close()
            except:
                pass
        else:
            self.pop_up_message('Error',
                                'You Did not Insert @ or . check The Email Address Again Please')

    # -----------------------------------------------------------------------------------------------------------------------------------#

    """ auto sum and put it in label and warning if the sum less than 0 """
    # function to show the sum in the label
    def show_total(self):
        self.total = sum(self.sum_list + self.multi_list + self.minus_list)  # 2
        if self.total >=0:
            self.total2 = str(round(self.total, 2))
            self.label_total.setText(self.total2)
        else:
            self.pop_up_message('Error', 'False Entry ')
            self.undo_write_inText_editor()

    # -----------------------------------------------------------------------------------------------------------------------------------#


# app = QtWidgets.QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication
# window = Ui(userName_fromDB='test')  # Create an instance of our class

# app.exec_()  # Start the application
