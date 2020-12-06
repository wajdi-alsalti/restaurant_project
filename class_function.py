import smtplib
import sys
import time
from PyQt5 import QtGui, QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QMessageBox


class Ui(QtWidgets.QWidget):
    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('restaurant2.ui', self)  # Load the .ui file

        self.btn_1.clicked.connect(lambda: self.add_item_in_text_editor('1', price=0, manytime=1))
        self.btn_2.clicked.connect(lambda: self.add_item_in_text_editor('2', price=0, manytime=2))
        self.btn_3.clicked.connect(lambda: self.add_item_in_text_editor('3', price=0, manytime=3))
        self.btn_4.clicked.connect(lambda: self.add_item_in_text_editor('4', price=0, manytime=4))
        self.btn_5.clicked.connect(lambda: self.add_item_in_text_editor('5', price=0, manytime=5))
        self.btn_6.clicked.connect(lambda: self.add_item_in_text_editor('6', price=0, manytime=6))
        self.btn_7.clicked.connect(lambda: self.add_item_in_text_editor('7', price=0, manytime=7))
        self.btn_8.clicked.connect(lambda: self.add_item_in_text_editor('8', price=0, manytime=8))
        self.btn_9.clicked.connect(lambda: self.add_item_in_text_editor('9', price=0, manytime=9))
        self.btn_0.clicked.connect(lambda: self.add_item_in_text_editor('0', price=0, manytime=0))

        # foods btn
        self.btn_chicken.clicked.connect(lambda: self.add_item_in_text_editor('Chicken Burger = 12,50', price=12.50))
        self.btn_beef.clicked.connect(lambda: self.add_item_in_text_editor('Beef Burger = 15,50', price=15.50))
        self.btn_pizza.clicked.connect(lambda: self.add_item_in_text_editor('Pizza Stander = 10,00', price=10.00))
        self.btn_salat.clicked.connect(lambda: self.add_item_in_text_editor('Salad = 7,50', price=7.50))
        self.btn_soup.clicked.connect(lambda: self.add_item_in_text_editor('Soup = 5,50', price=5.50))
        self.btn_geyros.clicked.connect(lambda: self.add_item_in_text_editor('Gyros = 6,50', price=6.50))
        self.bt_botatao.clicked.connect(lambda: self.add_item_in_text_editor('Pommes = 3,50', price=3.50))
        self.btn_ketchup.clicked.connect(lambda: self.add_item_in_text_editor('Ketchup = 0,99', price=0.99))
        self.btn_mayo.clicked.connect(lambda: self.add_item_in_text_editor('Mayo = 0,99', price=0.99))

        # drinks btns
        self.btn_cola.clicked.connect(lambda: self.add_item_in_text_editor('Cola + Pfand = 1,75', price=1.75))
        self.btn_fanta.clicked.connect(lambda: self.add_item_in_text_editor('Fanta + Pfand = 1,75', price=1.75))
        self.btn_sevenup.clicked.connect(lambda: self.add_item_in_text_editor('Seven Up + Pfand = 1,75', price=1.75))
        self.btn_kaffee.clicked.connect(lambda: self.add_item_in_text_editor('Kaffee = 1,20', price=1.20))
        self.btn_tee.clicked.connect(lambda: self.add_item_in_text_editor('Tee = 0,99', price=0.99))
        self.btn_capuccino.clicked.connect(lambda: self.add_item_in_text_editor('Cappuccino = 2,25', price=2.25))
        self.btn_beer.clicked.connect(lambda: self.add_item_in_text_editor('Beer = 1,50', price=1.50))
        self.btn_radler.clicked.connect(lambda: self.add_item_in_text_editor('Radler = 1,50', price=1.50))
        self.btn_maonten.clicked.connect(lambda: self.add_item_in_text_editor('Maonten = 1,75', price=1.75))

        # clear btn
        self.btn_clear.clicked.connect(self.clear_in_text_editor)
        self.btn_minus.clicked.connect(self.flag_delete_price)
        self.btn_multi.clicked.connect(self.flag_multi_price)
        self.btn_equal.clicked.connect(self.equal_the_invoice)
        self.btn_email.clicked.connect(self.send_invoice_email)
        self.btn_return.clicked.connect(self.return_money)

        self.sum_list = []
        self.multi_list = []
        self.minus_list = []
        self.food_list = []
        self.food_list_check = []
        self.aat = '@'
        self.dot = '.'
        self.operation_signal = ''
        self.change_button_command = ''
        self.showMaximized()

    # flag to change command btns to write in label
    def return_money(self):
        self.change_button_command = 'to_label'
        self.label_total.setText('')

    # add flag and insert - signal
    def flag_delete_price(self):
        if self.textfood.toPlainText() == '':
            pass
        else:
            self.operation_signal = 'minus'
            self.textfood.insertPlainText('-' + '\n')
            self.set_numbers_button_disable(False)

        # add flag for removed and operation and pop last item from sum list
    def flag_multi_price(self):
        try:
            self.operation_signal = 'multi'
            self.removed = self.sum_list.pop()
            self.textfood.insertPlainText('X' + ' ')
            self.set_foods_buttons_enabled(False)
        except IndexError:
            pass

    # to add the name of food and the price in text and then add the price in the list
    def add_item_in_text_editor(self, charchter, price, manytime=int):
        if self.change_button_command != 'to_label':
            self.textfood.insertPlainText(charchter + '\n')
            self.sum_list.append(price)
            self.delete_price_in_text(price, charchter)
            self.double_number_in_list(manytime)
            self.textfood.moveCursor(QtGui.QTextCursor.End)  # to move the text down when i add more input

            if self.operation_signal != 'minus':
                self.food_list.append(charchter)

            self.show_total()

        elif self.change_button_command == 'to_label':
            self.write_numbers_in_label(charchter)
        self.operation_signal = ''
        self.set_foods_buttons_enabled(True)
        self.set_numbers_button_disable(True)

    # write the numbers correct
    def write_numbers_in_label(self, charchter):
        self.label_total.setText(self.label_total.text() + charchter)

        # pop up messages for warning
    def pop_up_message(self, head, subject):
        self.msg = QMessageBox()
        self.msg.about(self.msg, head, subject)

    # to make function can be delete an price from the list
    def delete_price_in_text(self, price, charchter):
        if self.operation_signal == 'minus':
            self.minus_list.append(price * -2)
            if charchter in self.food_list:
                self.food_list_check.append(charchter)
            else:
                self.check_in_list()

    # to undo the input in text editor
    def undo_write_inText_editor(self):
        for _y in range(2):
            self.textfood.undo()
            

    # another function to detect a order to subscrtion
    def check_in_list(self):
        self.pop_up_message('Error','Careful Please\nYou can not Subtraction For Value You Did not Insert Before')
        self.minus_list.pop()
        self.sum_list.pop(-1)
        self.undo_write_inText_editor()

    # to detect the sign of operations and loop for how many time to multi 
    def double_number_in_list(self, manytime):
        if self.operation_signal == 'multi':
            try:
                for _i in range(manytime):
                    self.multi_list.append(self.removed)
            except TypeError:
                pass

    # btn clear function to delete the list and the text
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
            self.btn_return.setEnabled(True)
        self.btn_equal.setEnabled(False)

        

        """ hours = time.strftime('%H')
            day = time.strftime('%d')
            month = time.strftime('%m')
            conn = sqlite3.connect('incoming_data.db')
            c = conn.cursor()

            c.execute("INSERT INTO details VALUES(?,?,?,?,?)",(hours, day, month, ui.line_email.text(), total))

            conn.commit()
            conn.close() """

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
            pass
        elif self.aat in self.to_check_character and self.dot in self.to_check_character:
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
            """ % (self.sent_from, ", ".join(self.to), self.subject, self.body)
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

    # function to show the sum in the label 
    def show_total(self):
        self.total = sum(self.sum_list + self.multi_list + self.minus_list)  # 2
        if self.total >=0:
            self.total2 = str(round(self.total, 2))
            self.label_total.setText(self.total2)
        else:
            self.pop_up_message('Error', 'False Entry ')
            self.undo_write_inText_editor()
        

app = QtWidgets.QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication
window = Ui()  # Create an instance of our class

app.exec_()  # Start the application
