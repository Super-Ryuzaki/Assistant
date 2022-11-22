import sys, ctypes
import platform,socket,re, uuid
import os
import os.path
import datetime
   

#Import Libraries, If something missing go to except
try:
    from PyQt5 import QtWidgets
    from PyQt5 import QtGui
    from PyQt5.QtWidgets import *
    from PyQt5 import QtCore
    import psutil
    from requests import get
    import speedtest


#Installing the libraries and importing them again
except:
    #install requests if it's missing
    os.system("pip install requests")
    #install psutil for process and system utilities it's missing
    os.system("pip install psutil")
    #install pyqt5 for the UI if it's missing
    os.system("pip install pyqt5")
    #install speedtest CLI
    os.system('pip install speedtest-cli')

    #for the UI
    from PyQt5 import QtGui
    from PyQt5 import QtCore
    from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QMessageBox, QLabel, QCheckBox , QLineEdit, QSizePolicy
    #for the system specs
    import psutil
    #For Public IP
    from requests import get
    import speedtest

#Creates a folder to store the applications that downloads, Uses that folder to add wget if it's not in the PC
#Folder located at C:/IT each time you use "EXIT" in the program the folder is deleted
path = 'C:/IT'
if path is True :
    os.system('cd C:/IT')
else:
    os.system('cd C:/ && mkdir IT')
    os.system('icacls "C:/IT" /grant %USERNAME%:(OI)(CI)F /T')
    os.system('cd C:/IT')

if os.path.isfile('C:/Windows/wget.exe') is not True:
    os.system('cd C:/IT/ && curl https://eternallybored.org/misc/wget/1.21.1/32/wget.exe -O')          
    os.system('cd C:/IT/ && xcopy wget.exe "C:/Windows"')

class windows_util_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,400,400)
        self.setStyleSheet("background-color : black;")
        self.setWindowTitle("Assistant") 

        #holders
        self.transm_type = ""
        self.rule_name_holder = ""
        self.port_name_holder = ""
        self.command_caller = ""
        self.connection_type = ""

        #Labels
        #Label for port
        self.port_label = QLabel("Enter Port: ",self)
        self.port_label.adjustSize()
        self.port_label.setStyleSheet("color:Green")
        self.port_label.move (10,10) 
        
        
        #label for Rule name
        self.rule_name_label = QLabel("Enter Rule Name: ",self)
        self.rule_name_label.adjustSize()
        self.rule_name_label.setStyleSheet("color:Green")
        self.rule_name_label.move (125,10) 

        #Inputs
        #Input for Port
        self.port_entry = QLineEdit(self)
        self.port_entry.setStyleSheet("color:Green")
        self.port_entry.setGeometry(0,0,50,20)
        self.port_entry.move(65,8)
        self.port_entry.setValidator(QtGui.QIntValidator(1,65535,self))

        #input for Rule Name
        self.rulename_entry = QLineEdit(self)
        self.rulename_entry.setStyleSheet("color:Green")
        self.rulename_entry.setGeometry(0,0,120,20)
        self.rulename_entry.move(210,8)
        

        #radio buttons
        #tcp
        self.tcp_radiobutton = QtWidgets.QRadioButton("TCP type of Connection",self)
        self.tcp_radiobutton.move(10,40)
        self.tcp_radiobutton.setStyleSheet("color:Green")
        self.tcp_radiobutton.adjustSize()
        #signal
        self.tcp_radiobutton.toggled.connect(self.tcp_selected)
        
        #udp
        self.udp_radiobutton = QtWidgets.QRadioButton("UDP type of Connection",self)
        self.udp_radiobutton.move(160,40)
        self.udp_radiobutton.setStyleSheet("color:Green")
        self.udp_radiobutton.adjustSize()
        #signal
        self.udp_radiobutton.toggled.connect(self.udp_selected)

        #inbound connection
        self.inbound_radiobutton = QtWidgets.QRadioButton("Inbound type of Connection",self)
        self.inbound_radiobutton.move(10,70)
        self.inbound_radiobutton.setStyleSheet("color:Green")
        self.inbound_radiobutton.adjustSize()
        #signal
        self.inbound_radiobutton.toggled.connect(self.inbound_selected)

        #outbound connection
        self.outbound_radiobutton = QtWidgets.QRadioButton("Outbound type of Connection",self)
        self.outbound_radiobutton.move(190,70)
        self.outbound_radiobutton.setStyleSheet("color:Green")
        self.outbound_radiobutton.adjustSize()
        #signal
        self.outbound_radiobutton.toggled.connect(self.outbound_selected)


        #radiobutton groups
        #Transmition type Group
        transm_type_group = QButtonGroup(self)
        transm_type_group.addButton(self.tcp_radiobutton)
        transm_type_group.addButton(self.udp_radiobutton)

        #Connection Type Group
        connection_type_group = QButtonGroup(self)
        connection_type_group.addButton(self.inbound_radiobutton)
        connection_type_group.addButton(self.outbound_radiobutton)


        #buttons

        #Inbound Rules for port
        self.inb_rules_button = QPushButton("Set Port Rule",self)
        self.inb_rules_button.adjustSize()
        self.inb_rules_button.setStyleSheet("background-color: gray")
        self.inb_rules_button.setToolTip("<h3><font color = 'blue'> Enable Active Directory Users and Computers on this PC </font></h3>")
        self.inb_rules_button.move(10,105)
        self.inb_rules_button.clicked.connect(self.set_port_rule) 

        #ADUC Button
        self.aduc_button = QPushButton("Enable RSAT",self)
        self.aduc_button.adjustSize()
        self.aduc_button.setStyleSheet("background-color: gray")
        self.aduc_button.setToolTip("<h3><font color = 'blue'> Enable Remote Server Administration Tools on this PC </font></h3>")
        self.aduc_button.move(10,150)
        self.aduc_button.clicked.connect(self.get_aduc)

        #Hyper V Button
        self.hyperv_button = QPushButton("Enable Hyper-V",self)
        self.hyperv_button.adjustSize()
        self.hyperv_button.setStyleSheet("background-color: gray")
        self.hyperv_button.setToolTip("<h3><font color = 'blue'> Enable Hyper-V Manager on this PC (Be sure you have Virtualization enabled from bios as well!</font></h3>")
        self.hyperv_button.move(90,150)
        self.hyperv_button.clicked.connect(self.enable_hyperv)

        #ReturnButton
        self.return_button = QPushButton("Back",self)
        self.return_button.adjustSize()
        self.return_button.setStyleSheet("background-color: gray")
        self.return_button.move(150,340)
        self.return_button.clicked.connect(self.return_back)
            
        #exitButton
        self.exit_button = QPushButton("Exit",self)
        self.exit_button.adjustSize()
        self.exit_button.setStyleSheet("background-color: gray")
        self.exit_button.move(150,370)
        self.exit_button.clicked.connect(self.exit_fan)

    #Enables ADUC
    def get_aduc(self):
        os.system('powershell "Add-WindowsCapability -Online -Name Rsat.ActiveDirectory.DS-LDS.Tools~~~~0.0.1.0')
    
    #Enable Hyper-V Manager
    def enable_hyperv(self):
        os.system('DISM /Online /Enable-Feature /All /FeatureName:Microsoft-Hyper-V')

    #if tcp is selected
    def tcp_selected(self, selected):
        if selected:
           self.transm_type = "TCP "
           print("TCP Selected")
    #if udp is selected
    def udp_selected(self, selected):
        if selected:
            self.transm_type = "UDP "
            print("UDP Selected")

    def inbound_selected(self, selected):
        if selected:
            self.con_type = "in "

    def outbound_selected(self, selected):
        if selected:
            self.con_type = "out "

    def set_port_rule(self):
        self.rule_name_holder = self.rulename_entry.text()
        self.port_name_holder = self.port_entry.text()
        self.command_caller = 'netsh advfirewall firewall add rule name= "'+self.rule_name_holder +'" dir='+self.con_type+'action=allow protocol='+self.transm_type+' localport='+self.port_name_holder
        os.system(self.command_caller)
        print(self.command_caller)
        print("Done")

    def return_back(self):
        self.w_main = main_window()
        self.w_main.show()
        self.hide()

    def exit_fan(self):
        #close the program
        self.close()


class installer_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,400,400)
        self.setStyleSheet("background-color : black;")
        self.setWindowTitle("Assistant") 

        #Checkboxes for the software
        #VNC
        self.vnc_server_checkbox = QCheckBox("Install VNC Server",self)
        self.vnc_server_checkbox.move(10,10)
        self.vnc_server_checkbox.setStyleSheet("color: Green")
        self.vnc_server_checkbox.adjustSize()

        self.vnc_server_checkboxx32 = QCheckBox("Install VNC Server 32bit",self)
        self.vnc_server_checkboxx32.move(150,10)
        self.vnc_server_checkboxx32.setStyleSheet("color: Green")
        self.vnc_server_checkboxx32.adjustSize()

        #Browsers
        #checkbox for firefox
        self.firefox_checkbox = QCheckBox("Install Firefox",self)
        self.firefox_checkbox.move(10,30)
        self.firefox_checkbox.setStyleSheet("color: Green")
        self.firefox_checkbox.adjustSize()
        #32bit
        self.firefox_checkbox32 = QCheckBox("Install Firefox 32bit",self)
        self.firefox_checkbox32.move(150,30)
        self.firefox_checkbox32.setStyleSheet("color: Green")
        self.firefox_checkbox32.adjustSize()

        #checkbox for Chrome
        self.chrome_checkbox = QCheckBox("Install Google Chrome",self)
        self.chrome_checkbox.move(10,50)
        self.chrome_checkbox.setStyleSheet('color: Green')
        self.chrome_checkbox.adjustSize()
        #32bix
        self.chrome_checkbox32 = QCheckBox("Install Google Chrome 32bit",self)
        self.chrome_checkbox32.move(150,50)
        self.chrome_checkbox32.setStyleSheet('color: Green')
        self.chrome_checkbox32.adjustSize()

        #Checkbox for 7zip
        self.zip7_checkbox = QCheckBox("Install 7zip",self)
        self.zip7_checkbox.move(10,70)
        self.zip7_checkbox.setStyleSheet('color: Green')
        self.zip7_checkbox.adjustSize()
        #32bit
        self.zip7_checkbox32 = QCheckBox("Install 7zip 32bit",self)
        self.zip7_checkbox32.move(150,70)
        self.zip7_checkbox32.setStyleSheet('color: Green')
        self.zip7_checkbox32.adjustSize()

        #Checkbox for zoom
        self.zoom_checkbox = QCheckBox("Install zoom",self)
        self.zoom_checkbox.move(10,90)
        self.zoom_checkbox.setStyleSheet('color: Green')
        self.zoom_checkbox.adjustSize()

        #32bit
        self.zoom_checkbox32 = QCheckBox("Install zoom 32bit",self)
        self.zoom_checkbox32.move(150,90)
        self.zoom_checkbox32.setStyleSheet('color: Green')
        self.zoom_checkbox32.adjustSize()
        
        #Checkbox for anydesk
        self.anydesk_checkbox = QCheckBox("Install Anydesk",self)
        self.anydesk_checkbox.move(10,110)
        self.anydesk_checkbox.setStyleSheet('color: Green')
        self.anydesk_checkbox.adjustSize()

        #Label for error if no check boxes are present
        self.checkboxes_checker_label = QLabel("",self)
        self.checkboxes_checker_label.adjustSize()
        self.checkboxes_checker_label.setStyleSheet("color:Green")
        self.checkboxes_checker_label.move(125,250)
        self.checkboxes_checker_label.setHidden(True)

        #Buttons
        #Install Button
        self.install_fanction_button = QPushButton("Install this!",self)
        self.install_fanction_button.move(150,300)
        self.install_fanction_button.setToolTip("<h3><font color = 'blue'>Install the Checked Software</font></h3>")
        self.install_fanction_button.setStyleSheet("background-color: gray")
        self.install_fanction_button.adjustSize()
        self.install_fanction_button.clicked.connect(self.install_fanction) 

        #ReturnButton
        self.return_button = QPushButton("Back",self)
        self.return_button.adjustSize()
        self.return_button.setStyleSheet("background-color: gray")
        self.return_button.move(150,340)
        self.return_button.clicked.connect(self.return_back)
 
       #Button for Exit
        self.exit_button = QPushButton("Exit",self)
        self.exit_button.move(150,380)
        self.exit_button.setToolTip("<h3><font color = 'blue'>Exit Software</font></h3>")
        self.exit_button.setStyleSheet("background-color: gray")
        self.exit_button.adjustSize()
        self.exit_button.clicked.connect(self.exit_fan) 

    def install_fanction(self):
        #VNC Server installer
        if self.vnc_server_checkbox.isChecked() == True:
           self.checkboxes_checker_label.setHidden(True)
           os.system('cd C:/IT && wget --no-check-certificate -O "vnc.msi" "https://onedrive.live.com/download?cid=8B3766DEBFF9139D&resid=8B3766DEBFF9139D%212499&authkey=AGXO07RGl7Peiwk"')
           os.system("cd C:/IT && msiexec /i vnc.msi /qn")
        
        if self.vnc_server_checkboxx32.isChecked() == True:
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
        if self.vnc_server_checkbox.isChecked() == False and self.vnc_server_checkboxx32.isChecked() == False and self.firefox_checkbox.isChecked() == False and self.firefox_checkbox32.isChecked() == False and self.chrome_checkbox.isChecked() == False and self.chrome_checkbox32.isChecked() == False and self.anydesk_checkbox.isChecked() == False and self.zoom_checkbox.isChecked() == False and self.zoom_checkbox32.isChecked() == False:
            self.checkboxes_checker_label.setHidden(False)
            self.checkboxes_checker_label.setText("You must choose at least 1!")
            self.error_dialog.showMessage('You must Choose at least 1!')
            self.checkboxes_checker_label.adjustSize()

    def return_back(self):
        self.w_main = main_window()
        self.w_main.show()
        self.hide()

    def exit_fan(self):
        #close the program
        self.close()


class pcspecs_window(QMainWindow):
    def __init__(self):
        super().__init__()
         
        self.setGeometry(200,200,400,400)
        self.setStyleSheet("background-color : black;")
        self.setWindowTitle("Assistant")         
         
        #kali ta antistixa stoixeia apo thn system_specs
        self.platform_system = platform.system()
        self.platform_version = platform.version()
        self.platform_platform = platform.platform()
        self.platform_machine = platform.machine()
        self.platform_processor = platform.processor()
        self.ram = str(round(psutil.virtual_memory().total / (1024.0 **3)))
        self.local_ip = socket.gethostbyname(socket.gethostname())
        self.pub_ip = get('https://api.ipify.org').text
        self.download_speed_holder = "-"
        self.upload_speed_holder = "-"

        self.system_specs()

    #edw einai ola ta config gia ta labels
    def system_specs(self):
        #platform system
        self.platform_system_label = QLabel("Operating System: " + self.platform_system,self)
        self.platform_system_label.adjustSize()
        self.platform_system_label.setStyleSheet("color:Red")
        self.platform_system_label.move (10,10)            
           
        #platform version
        self.platform_version_label = QLabel("Version: " + self.platform_version,self)
        self.platform_version_label.adjustSize()
        self.platform_version_label.setStyleSheet("color:Red")
        self.platform_version_label.move(10,30)

        #platform platform
        self.platform_platform_label = QLabel("Platform: " + self.platform_platform,self)
        self.platform_platform_label.adjustSize()
        self.platform_platform_label.setStyleSheet("color:Red")
        self.platform_platform_label.move(10,50)
           
        #platform machine
        self.platform_machine_label = QLabel("Architecture: "+self.platform_machine,self)
        self.platform_machine_label.adjustSize()
        self.platform_machine_label.setStyleSheet("color:Red")
        self.platform_machine_label.move(10,70)
            
        #platform processor
        self.platform_processor_label = QLabel("Processor: "+ self.platform_processor,self)
        self.platform_processor_label.adjustSize()
        self.platform_processor_label.setStyleSheet("color:Red")
        self.platform_processor_label.move(10,90)
            
        #ram 
        self.ram_label = QLabel("Ram: "+self.ram+" GB",self)
        self.ram_label.adjustSize()
        self.ram_label.setStyleSheet("color:Red")
        self.ram_label.move(10,110)
            
        #Local Ip
        self.loc_ip_label = QLabel("Local IP: "+self.local_ip,self)
        self.loc_ip_label.adjustSize()
        self.loc_ip_label.setStyleSheet("color:Red")
        self.loc_ip_label.move(10,130)
            
        #Public IP
        self.pub_ip_label = QLabel("Public IP: "+self.pub_ip,self)
        self.pub_ip_label.adjustSize()
        self.pub_ip_label.setStyleSheet("color:Red")
        self.pub_ip_label.move(10,150)
        
        #Download speed label
        self.download_speed_label = QLabel("Download speed: "+ self.download_speed_holder,self)
        self.download_speed_label.adjustSize()
        self.download_speed_label.setStyleSheet("color:Red")
        self.download_speed_label.move(10,170)

        #Upload speed label
        self.upload_speed_label = QLabel("Upload speed: "+ self.upload_speed_holder,self)
        self.upload_speed_label.adjustSize()
        self.upload_speed_label.setStyleSheet("color:Red")
        self.upload_speed_label.move(10,190)

        #Do speedtest button
        self.start_speedtest_button = QPushButton("Start Speedtest",self)
        self.start_speedtest_button.adjustSize()
        self.start_speedtest_button.setStyleSheet("color:black")
        self.start_speedtest_button.move(6,210)
        self.start_speedtest_button.setStyleSheet("background-color: gray")
        self.start_speedtest_button.clicked.connect(self.start_speedtest)

        #ReturnButton
        self.return_button = QPushButton("Back",self)
        self.return_button.adjustSize()
        self.return_button.setStyleSheet("color:red")
        self.return_button.setStyleSheet("background-color: gray")
        self.return_button.move(150,340)
        self.return_button.clicked.connect(self.return_back)
            
        #exitButton
        self.exit_button = QPushButton("Exit",self)
        self.exit_button.adjustSize()
        self.exit_button.setStyleSheet("color:black")
        self.exit_button.setStyleSheet("background-color: gray")
        self.exit_button.move(150,370)
        self.exit_button.clicked.connect(self.exit_fan)
 
    def start_speedtest(self):
        print('Speedtest Running please wait')
        #To start the speedtest
        net_speed = speedtest.Speedtest(secure=1)
        #get server
        net_speed.get_best_server()
        #keep and convert the number for download and upload
        self.download_speed_holder = round(net_speed.download()/1024000, 2)
        self.upload_speed_holder = round(net_speed.upload()/1024000, 2)
        #update the number to the label
        self.download_speed_label.setText("Download speed: "+ (str(self.download_speed_holder)+ " MB"))
        self.upload_speed_label.setText("Upload speed: "+(str(self.upload_speed_holder)+ " MB"))
        #adjust the size
        self.download_speed_label.adjustSize()
        self.upload_speed_label.adjustSize()


    def return_back(self):
        self.w_main = main_window()
        self.w_main.show()
        self.hide()

    def exit_fan(self):
        #close the program
        self.close()

class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
     
        #Button for PC Specs
        self.pcspecs_button = QPushButton("PC Specifiactions",self)
        self.pcspecs_button.move (10,10)
        self.pcspecs_button.setToolTip("<h3><font color = 'blue'>Check your PC Specifiactions </font></h3>")
        self.pcspecs_button.setStyleSheet("background-color: gray")
        self.pcspecs_button.adjustSize()
        self.pcspecs_button.clicked.connect(self.pcspecs_window_swap)

        #Button for Installer
        self.installer_button = QPushButton ("Install Software",self)
        self.installer_button.move (105,10)
        self.installer_button.setToolTip("<h3><font color = 'blue'>Choose software to download and install </font></h3>")
        self.installer_button.setStyleSheet("background-color: gray")
        self.installer_button.adjustSize()
        self.installer_button.clicked.connect(self.installer_window_swap)

        #Button for Windows Utilities
        self.windows_u_button = QPushButton ("Windows Utilities",self)
        self.windows_u_button.move (195,10)
        self.windows_u_button.setToolTip("<h3><font color = 'blue'> Get ADUC, set rules on firewall etc </font></h3>")
        self.windows_u_button.setStyleSheet("background-color: gray")
        self.windows_u_button.adjustSize()
        self.windows_u_button.clicked.connect(self.windows_util_swap)

        #Button for Exit
        self.exit_button = QPushButton("Exit",self)
        self.exit_button.move(200,300)
        self.exit_button.setToolTip("<h3><font color = 'blue'>Exit Software</font></h3>")
        self.exit_button.setStyleSheet("background-color: gray")
        self.exit_button.adjustSize()
        self.exit_button.clicked.connect(self.exit_fan) 

        #Goto window configs
        self.main_window_configs()

    def installer_window_swap(self):
        self.w_installer = installer_window()
        self.w_installer.show()
        self.hide()

    #Window swap from main to PC Specs handler
    def pcspecs_window_swap(self):
        self.w_pcspecs = pcspecs_window()
        self.w_pcspecs.show()
        self.hide()
        
    #Window swap from main to Windows utilities
    def windows_util_swap(self):
        self.w_windows_util = windows_util_window()
        self.w_windows_util.show()
        self.hide()

        #Window Configs
    def main_window_configs(self):
        self.setStyleSheet("background-color: black;")
        self.setWindowTitle("Assistant")
        self.setGeometry(200,200,500,500)
        self.show()
        
    def exit_fan(self):
        #close the program
        os.system('cd C:/ && rmdir /Q /S IT')
        self.close()        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main_window()
    sys.exit(app.exec())