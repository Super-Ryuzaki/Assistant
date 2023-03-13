from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget,QMainWindow, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QFont
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
import os

class windows_util_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,400,400)
        self.setStyleSheet("background-color: #2f2f2f;")
        self.setWindowTitle("Assistant") 
        self.setFont(QFont("Trajan", 16))

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
        self.port_label.setStyleSheet("color:white")
        self.port_label.move (10,10) 
        
        
        #label for Rule name
        self.rule_name_label = QLabel("Enter Rule Name: ",self)
        self.rule_name_label.adjustSize()
        self.rule_name_label.setStyleSheet("color:white")
        self.rule_name_label.move (125,10) 

        #Inputs
        #Input for Port
        self.port_entry = QLineEdit(self)
        self.port_entry.setStyleSheet("color:white")
        self.port_entry.setGeometry(0,0,50,20)
        self.port_entry.move(65,8)
        self.port_entry.setValidator(QtGui.QIntValidator(1,65535,self))

        #input for Rule Name
        self.rulename_entry = QLineEdit(self)
        self.rulename_entry.setStyleSheet("color:white")
        self.rulename_entry.setGeometry(0,0,120,20)
        self.rulename_entry.move(210,8)
        

        #radio buttons
        #tcp
        self.tcp_radiobutton = QtWidgets.QRadioButton("TCP type of Connection",self)
        self.tcp_radiobutton.move(10,40)
        self.tcp_radiobutton.setStyleSheet("color:white")
        self.tcp_radiobutton.adjustSize()
        #signal
        self.tcp_radiobutton.toggled.connect(self.tcp_selected)
        
        #udp
        self.udp_radiobutton = QtWidgets.QRadioButton("UDP type of Connection",self)
        self.udp_radiobutton.move(160,40)
        self.udp_radiobutton.setStyleSheet("color:white")
        self.udp_radiobutton.adjustSize()
        #signal
        self.udp_radiobutton.toggled.connect(self.udp_selected)

        #inbound connection
        self.inbound_radiobutton = QtWidgets.QRadioButton("Inbound type of Connection",self)
        self.inbound_radiobutton.move(10,70)
        self.inbound_radiobutton.setStyleSheet("color:white")
        self.inbound_radiobutton.adjustSize()
        #signal
        self.inbound_radiobutton.toggled.connect(self.inbound_selected)

        #outbound connection
        self.outbound_radiobutton = QtWidgets.QRadioButton("Outbound type of Connection",self)
        self.outbound_radiobutton.move(190,70)
        self.outbound_radiobutton.setStyleSheet("color:white")
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
        self.inb_rules_button.setStyleSheet("background-color: #0066CC; color: #FFFFFF; font-size: 11px; border-radius: 5px;")
        self.inb_rules_button.setToolTip("<h3><font color = 'blue'> add a Rule for Inbound or Outbound Connection</font></h3>")
        self.inb_rules_button.move(10,105)
        self.inb_rules_button.clicked.connect(self.set_port_rule) 

        #ADUC Button
        self.aduc_button = QPushButton("Enable RSAT",self)
        self.aduc_button.setStyleSheet("background-color: #0066CC; color: #FFFFFF; font-size: 11px; border-radius: 5px;")
        self.aduc_button.setToolTip("<h3><font color = 'blue'> Enable Remote Server Administration Tools on this PC </font></h3>")
        self.aduc_button.move(10,150)
        self.aduc_button.clicked.connect(self.get_aduc)

        #Hyper V Button
        self.hyperv_button = QPushButton("Enable Hyper-V",self)
        self.hyperv_button.setStyleSheet("background-color: #0066CC; color: #FFFFFF; font-size: 11px; border-radius: 5px;")
        self.hyperv_button.setToolTip("<h3><font color = 'blue'> Enable Hyper-V Manager on this PC (Be sure you have Virtualization enabled from bios as well!</font></h3>")
        self.hyperv_button.move(120,150)
        self.hyperv_button.clicked.connect(self.enable_hyperv)
            
        #exitButton
        self.back_button = QPushButton("Back",self)
        self.back_button.setStyleSheet("background-color: #0066CC; color: #FFFFFF; font-size: 11px; border-radius: 5px;")
        self.back_button.setGeometry(95, 360, 210, 30)
        self.back_button.clicked.connect(self.close)

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