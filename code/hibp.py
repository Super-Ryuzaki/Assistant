from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget,QMainWindow, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QFont
from PyQt5 import QtWidgets, QtCore
import pyhibp
from pyhibp import pwnedpasswords as pw
import assistant

pyhibp.set_user_agent(ua="Assistant/0.0.1 (An All in One IT Tool)")

class HIBPWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Have I Been Pwned")
        self.setGeometry(200, 200, 400, 400)
        self.setStyleSheet("background-color: #2f2f2f;")
        self.setFont(QFont("Trajan", 16))

        # Create central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Password Search
        self.enter_password = QLineEdit("Enter Password",central_widget)
        self.enter_password.setStyleSheet("color: white")
        self.enter_password.setGeometry(10, 10, 140, 25)
        self.enter_password.installEventFilter(self)           
        self.ispwleaked_label = QLabel(central_widget)
        self.ispwleaked_label.setStyleSheet("color: white")
        self.ispwleaked_label.setGeometry(160, 10, 230, 25)
        self.password_response_label = QLabel(central_widget)
        self.password_response_label.setStyleSheet("color: white")
        self.password_response_label.setGeometry(10, 45, 380, 25)
        self.searchpassword_button = QPushButton("Search for Password Leak", central_widget)
        self.searchpassword_button.setStyleSheet("background-color: #0066CC; color: #FFFFFF; font-size: 11px; border-radius: 5px;")
        self.searchpassword_button.setToolTip("<h3><font color='blue'>Check if your password exists on the internet</font></h3>")
        self.searchpassword_button.setGeometry(10, 70, 380, 30)
        self.searchpassword_button.clicked.connect(self.searchpw_breaches)

        # For Websites
        self.enter_wb = QLineEdit("Enter Website",central_widget)
        self.enter_wb.setStyleSheet("color: white")
        self.enter_wb.setGeometry(10, 130, 140, 25)
        self.enter_wb.installEventFilter(self)             
        self.iswbbreached_label = QLabel(central_widget)
        self.iswbbreached_label.setStyleSheet("color: white")
        self.iswbbreached_label.setGeometry(160, 130, 230, 25)
        self.wbbreach_button = QPushButton("Search for Websites", central_widget)
        self.wbbreach_button.setStyleSheet("background-color: #0066CC; color: #FFFFFF; font-size: 11px; border-radius: 5px;")
        self.wbbreach_button.setToolTip("<h3><font color='blue'>Check for websites that may have leaked data</font></h3>")
        self.wbbreach_button.setGeometry(10, 165, 380, 30)
        self.wbbreach_button.clicked.connect(self.searchweb_breaches)

        # Back Button
        self.back_button = QPushButton("Back", central_widget)
        self.back_button.setStyleSheet("background-color: #0066CC; color: #FFFFFF; font-size: 11px; border-radius: 5px;")
        self.back_button.setGeometry(95, 360, 210, 30)
        self.back_button.clicked.connect(self.close)       

    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.FocusIn and source is self.enter_password):
            self.enter_password.clear()
        elif (event.type() == QtCore.QEvent.FocusIn and source is self.enter_wb):
            self.enter_wb.clear()
        return super().eventFilter(source, event)

    def searchpw_breaches(self):
        self.enterpw_holder = self.enter_password.text()
        pwresp = pw.is_password_breached(password=self.enterpw_holder)
        if pwresp:
            self.ispwleaked_label.setText("Password Breached!!")
            self.ispwleaked_label.adjustSize()
            self.password_response_label.setText("This password was used {0} time(s) before.".format(pwresp))
            self.password_response_label.adjustSize()
        else:
            self.ispwleaked_label.setText("No Password Breach!!!")
            self.ispwleaked_label.adjustSize()
            self.password_response_label.setText("")
            self.password_response_label.adjustSize()
            
    def searchweb_breaches(self):
        webresp = pyhibp.get_single_breach(breach_name=self.enter_wb.text())
        if webresp:
            self.iswbbreached_label.setText("Website Breached!!")
            self.iswbbreached_label.adjustSize()
            if 'name' in webresp:
                self.wbbreach_response_label = QLabel(self)
                self.wbbreach_response_label.setStyleSheet("color: white")
                self.wbbreach_response_label.move(10, 140)
                self.wbbreach_response_label.setText(f"The website {webresp['name']} was breached on {webresp['breach_date']}.")
                self.wbbreach_response_label.adjustSize()
            else:
                self.wbbreach_response_label = QLabel(self)
                self.wbbreach_response_label.setStyleSheet("color: red")
                self.wbbreach_response_label.move(10, 140)
                self.wbbreach_response_label.setText("No breach details found for this website.")
                self.wbbreach_response_label.adjustSize()
        else:
            self.iswbbreached_label.setText("No Website Breach!!!")
            self.iswbbreached_label.adjustSize()
            self.wbbreach_response_label = QLabel(self)
            self.wbbreach_response_label.setStyleSheet("color: white")
            self.wbbreach_response_label.move(10, 140)
            self.wbbreach_response_label.setText(f"The website {self.enter_wb.text()} was not breached.")
            self.wbbreach_response_label.adjustSize()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
