import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QCheckBox, QRadioButton
from PyQt5.QtGui import QFont
from PyQt5 import QtWidgets, QtCore
import assistant
from pathlib import Path
import subprocess
import wget
import shutil

class installer_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 400)
        self.setStyleSheet("background-color: #2f2f2f;")
        self.setWindowTitle("Assistant")

        # Checkboxes for the software
        font = QFont("Trajan", 10)
        font.setBold(True)
        font.setWeight(75)

        # 64-bit Software Checkboxes
        checkbox_group_64 = QtWidgets.QGroupBox(self)
        checkbox_group_64.setTitle("64-bit Software")
        checkbox_group_64.setFont(font)
        checkbox_group_64.setStyleSheet("color: #00FF00")
        checkbox_group_64.setGeometry(10, 10, 250, 200)

        self.vnc_server_checkbox = QCheckBox("Install VNC Server", checkbox_group_64)
        self.vnc_server_checkbox.move(10, 20)
        self.vnc_server_checkbox.setFont(font)
        self.vnc_server_checkbox.setStyleSheet("color: #00FF00")
        self.vnc_server_checkbox.adjustSize()

        self.firefox_checkbox = QCheckBox("Install Firefox", checkbox_group_64)
        self.firefox_checkbox.move(10, 50)
        self.firefox_checkbox.setFont(font)
        self.firefox_checkbox.setStyleSheet("color: #00FF00")
        self.firefox_checkbox.adjustSize()

        self.chrome_checkbox = QCheckBox("Install Google Chrome", checkbox_group_64)
        self.chrome_checkbox.move(10, 80)
        self.chrome_checkbox.setFont(font)
        self.chrome_checkbox.setStyleSheet("color: #00FF00")
        self.chrome_checkbox.adjustSize()

        self.zip7_checkbox = QCheckBox("Install 7zip", checkbox_group_64)
        self.zip7_checkbox.move(10, 110)
        self.zip7_checkbox.setFont(font)
        self.zip7_checkbox.setStyleSheet("color: #00FF00")
        self.zip7_checkbox.adjustSize()

        self.zoom_checkbox = QCheckBox("Install zoom", checkbox_group_64)
        self.zoom_checkbox.move(10, 140)
        self.zoom_checkbox.setFont(font)
        self.zoom_checkbox.setStyleSheet("color: #00FF00")
        self.zoom_checkbox.adjustSize()

        self.anydesk_checkbox = QCheckBox("Install Anydesk", checkbox_group_64)
        self.anydesk_checkbox.move(10, 170)
        self.anydesk_checkbox.setFont(font)
        self.anydesk_checkbox.setStyleSheet("color: #00FF00")
        self.anydesk_checkbox.adjustSize()

        # 32-bit Software Checkboxes
        checkbox_group_32 = QtWidgets.QGroupBox(self)
        checkbox_group_32.setTitle("32-bit Software")
        checkbox_group_32.setFont(font)
        checkbox_group_32.setStyleSheet("color: #00FF00")
        checkbox_group_32.setGeometry(200, 10, 190, 200)

        self.vnc_server_checkbox32 = QCheckBox("Install VNC Server", checkbox_group_32)
        self.vnc_server_checkbox32.move(10, 20)
        self.vnc_server_checkbox32.setFont(font)
        self.vnc_server_checkbox32.setStyleSheet("color: #00FF00")
        self.vnc_server_checkbox32.adjustSize()
        
        self.firefox_checkbox32 = QCheckBox("Install Firefox", checkbox_group_32)
        self.firefox_checkbox32.move(10, 50)
        self.firefox_checkbox32.setFont(font)
        self.firefox_checkbox32.setStyleSheet("color: #00FF00")
        self.firefox_checkbox32.adjustSize()

        self.chrome_checkbox32 = QCheckBox("Install Google Chrome", checkbox_group_32)
        self.chrome_checkbox32.move(10, 80)
        self.chrome_checkbox32.setFont(font)
        self.chrome_checkbox32.setStyleSheet("color: #00FF00")
        self.chrome_checkbox32.adjustSize()

        self.zip7_checkbox32 = QCheckBox("Install 7zip", checkbox_group_32)
        self.zip7_checkbox32.move(10, 110)
        self.zip7_checkbox32.setFont(font)
        self.zip7_checkbox32.setStyleSheet("color: #00FF00")
        self.zip7_checkbox32.adjustSize()

        self.zoom_checkbox32 = QCheckBox("Install zoom", checkbox_group_32)
        self.zoom_checkbox32.move(10, 140)
        self.zoom_checkbox32.setFont(font)
        self.zoom_checkbox32.setStyleSheet("color: #00FF00")
        self.zoom_checkbox32.adjustSize()

        self.anydesk_checkbox32 = QCheckBox("Install Anydesk", checkbox_group_32)
        self.anydesk_checkbox32.move(10, 170)
        self.anydesk_checkbox32.setFont(font)
        self.anydesk_checkbox32.setStyleSheet("color: #00FF00")
        self.anydesk_checkbox32.adjustSize()


        #EDW
        self.checkboxes_checker_label = QLabel("",self)
        self.checkboxes_checker_label.adjustSize()
        self.checkboxes_checker_label.setStyleSheet("color:Green")
        self.checkboxes_checker_label.move(125,250)
        self.checkboxes_checker_label.setHidden(True)

        # Buttons for installing and cancelling
        install_button = QPushButton("Install", self)
        install_button.setGeometry(60, 300, 100, 50)
        install_button.setFont(font)
        install_button.setStyleSheet("background-color: #00FF00;")
        install_button.clicked.connect(self.install_function)

        cancel_button = QPushButton("Back", self)
        cancel_button.setGeometry(220, 300, 100, 50)
        cancel_button.setFont(font)
        cancel_button.setStyleSheet("background-color: #FF0000;")
        cancel_button.clicked.connect(self.close)
        
        checkboxes = {
        "vnc_server": self.vnc_server_checkbox.isChecked(),
        "firefox": self.firefox_checkbox.isChecked(),
        "chrome": self.chrome_checkbox.isChecked(),
        "zip7": self.zip7_checkbox.isChecked(),
        "zoom": self.zoom_checkbox.isChecked(),
        "anydesk": self.anydesk_checkbox.isChecked(),
        "vnc_server_x32": self.vnc_server_checkbox32.isChecked(),
        "firefox_x32": self.firefox_checkbox32.isChecked(),
        "chrome_x32": self.chrome_checkbox32.isChecked(),
        "zip7_x32": self.zip7_checkbox32.isChecked(),
        "zoom_x32": self.zoom_checkbox32.isChecked(),
        "anydesk_x32": self.anydesk_checkbox32.isChecked()
        }
        
    def install_function(self):
        folder_path = "C:/IT"
        os.makedirs(folder_path, exist_ok=True)
        if os.path.isfile('C:/Windows/wget.exe') is not True:
            os.system('cd C:/IT/ && curl https://eternallybored.org/misc/wget/1.21.1/32/wget.exe -O')          
            os.system('cd C:/IT/ && xcopy wget.exe "C:/Windows"')
            
        if self.vnc_server_checkbox.isChecked() == True:
           self.checkboxes_checker_label.setHidden(True)
           os.system('cd C:/IT && wget --no-check-certificate -O "vnc.msi" "https://onedrive.live.com/download?cid=8B3766DEBFF9139D&resid=8B3766DEBFF9139D%212499&authkey=AGXO07RGl7Peiwk"')
           os.system("cd C:/IT && msiexec /i vnc.msi /qn")
        
        if self.vnc_server_checkbox32.isChecked() == True:
           self.checkboxes_checker_label.setHidden(True)
           os.system('cd C:/IT && wget --no-check-certificate -O "vnc32.msi" "https://onedrive.live.com/download?cid=8B3766DEBFF9139D&resid=8B3766DEBFF9139D%212500&authkey=ALhF09or4Psq_Nk"')
           os.system('cd C:/IT && msiexec /i vnc32.msi /qn')
 
        #Firefox Installer    
        if self.firefox_checkbox.isChecked() == True:
           self.checkboxes_checker_label.setHidden(True)
           os.system('cd C:/IT && wget --no-check-certificate -O "Firefox.msi" "https://onedrive.live.com/download?cid=8B3766DEBFF9139D&resid=8B3766DEBFF9139D%212501&authkey=ANjN8oSaWkPJW5U"')
           os.system('cd C:/IT && msiexec /i Firefox.msi /qn')
        
        if self.firefox_checkbox32.isChecked() == True:
           self.checkboxes_checker_label.setHidden(True)
           os.system('cd C:/IT && wget --no-check-certificate -O "Firefox32.msi" "https://onedrive.live.com/download?cid=8B3766DEBFF9139D&resid=8B3766DEBFF9139D%212504&authkey=AJF3R3t3tqil2PU"')
           os.system('cd C:/IT && msiexec /i Firefox32.msi /qn')

        #Chrome Installer
        if self.chrome_checkbox.isChecked() == True:
           self.checkboxes_checker_label.setHidden(True)
           os.system('cd C:/IT && wget --no-check-certificate -O "Chrome.msi" "https://onedrive.live.com/download?cid=8B3766DEBFF9139D&resid=8B3766DEBFF9139D%212503&authkey=AKhInA8RwcD5jV0"')
           os.system('cd C:/IT && msiexec /i Chrome.msi /qn')

        if self.chrome_checkbox32.isChecked() == True:
           self.checkboxes_checker_label.setHidden(True)
           os.system('cd C:/IT && wget --no-check-certificate -O "Chrome32.msi" "https://onedrive.live.com/download?cid=8B3766DEBFF9139D&resid=8B3766DEBFF9139D%212504&authkey=AJF3R3t3tqil2PU"')
           os.system('cd C:/IT && msiexec /i Chrome32.msi /qn')

        #7Zip Installer
        if self.zip7_checkbox.isChecked() == True:
            self.checkboxes_checker_label.setHidden(True)
            os.system('cd C:/IT && wget --no-check-certificate -O "7zip.msi" "https://onedrive.live.com/download?cid=8B3766DEBFF9139D&resid=8B3766DEBFF9139D%212507&authkey=AEA878Rjl2h-Zk4"')
            os.system('cd C:/IT && msiexec /i 7zip.msi /qn ')

        if self.zip7_checkbox32.isChecked() == True:
           self.checkboxes_checker_label.setHidden(True)
           os.system('cd C:/IT && wget --no-check-certificate -O "7zip32.msi" "https://onedrive.live.com/download?cid=8B3766DEBFF9139D&resid=8B3766DEBFF9139D%212506&authkey=AAfO9ta1yh57jJw"')
           os.system('cd C:/IT && msiexec /i 7zip32.msi /qn ')

        #Zoom
        if self.zoom_checkbox.isChecked() == True:
            self.checkboxes_checker_label.setHidden(True)
            os.system('cd C:/IT && wget --no-check-certificate -O "Zoom.msi" "https://onedrive.live.com/download?cid=8B3766DEBFF9139D&resid=8B3766DEBFF9139D%212510&authkey=ALyUPgBBBhGjTSM"')
            os.system('cd C:/IT && msiexec /i Zoom.msi /qn')
        #32bit
        if self.zoom_checkbox32.isChecked() == True:
            self.checkboxes_checker_label.setHidden(True)
            os.system('cd C:/IT && wget --no-check-certificate -O "Zoom32.msi" "https://onedrive.live.com/download?cid=8B3766DEBFF9139D&resid=8B3766DEBFF9139D%212509&authkey=ANysrtV9MCREslI"')
            os.system('cd C:/IT && msiexec /i Zoom32.msi /qn')

        #Anydesk Installer
        if self.anydesk_checkbox.isChecked() == True:
            self.checkboxes_checker_label.setHidden(True)
            os.system('cd C:/IT && wget --no-check-certificate -O "Anydesk.msi" "https://onedrive.live.com/download?cid=8B3766DEBFF9139D&resid=8B3766DEBFF9139D%212508&authkey=AE_gU99VXp2Syj4"')
            os.system('cd C:/IT && msiexec /i Anydesk.msi /qn')

        #Nothing Checked
        if self.vnc_server_checkbox.isChecked() == False and self.vnc_server_checkbox32.isChecked() == False and self.firefox_checkbox.isChecked() == False and self.firefox_checkbox32.isChecked() == False and self.chrome_checkbox.isChecked() == False and self.chrome_checkbox32.isChecked() == False and self.anydesk_checkbox.isChecked() == False and self.zoom_checkbox.isChecked() == False and self.zoom_checkbox32.isChecked() == False:
            self.checkboxes_checker_label.setHidden(False)
            self.checkboxes_checker_label.setText("You must choose at least 1!")
            self.error_dialog.showMessage('You must Choose at least 1!')
            self.checkboxes_checker_label.adjustSize()
        shutil.rmtree('C:/IT')
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
