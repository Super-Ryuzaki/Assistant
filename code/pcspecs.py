from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel
from PyQt5.QtGui import QFont
from PyQt5 import QtWidgets, QtCore
import platform,socket,re, uuid
import psutil
import speedtest
from requests import get
import assistant


class pcspecs_window(QMainWindow):
    def __init__(self):
        super().__init__()
         
        self.setFixedSize(400, 400)
        self.setStyleSheet("background-color: #2f2f2f;")
        self.setWindowTitle("Assistant")    
        self.setFont(QFont('Trajan', 12))
         
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
        self.platform_system_label.setStyleSheet("color:White")
        self.platform_system_label.setGeometry(10, 10, 450, 25)
        self.platform_system_label.setFont(QFont('Trajan', 11))
           
        #platform version
        self.platform_version_label = QLabel("Version: " + self.platform_version,self)
        self.platform_version_label.setStyleSheet("color:White")
        self.platform_version_label.setGeometry(10, 40, 450, 25)
        self.platform_version_label.setFont(QFont('Trajan', 11))

        #platform platform
        self.platform_platform_label = QLabel("Platform: " + self.platform_platform,self)
        self.platform_platform_label.setStyleSheet("color:White")
        self.platform_platform_label.setGeometry(10, 70, 450, 25)
        self.platform_platform_label.setFont(QFont('Trajan', 11))
    
        #platform machine
        self.platform_machine_label = QLabel("Architecture: "+self.platform_machine,self)
        self.platform_machine_label.setStyleSheet("color:White")
        self.platform_machine_label.setGeometry(10, 100, 450, 25)
        self.platform_machine_label.setFont(QFont('Trajan', 11))
         
        #platform processor
        self.platform_processor_label = QLabel("Processor: "+ self.platform_processor,self)
        self.platform_processor_label.setStyleSheet("color:White")
        self.platform_processor_label.setGeometry(10, 130, 450, 25)
        self.platform_processor_label.setFont(QFont('Trajan', 10))
        
        #ram 
        self.ram_label = QLabel("Ram: "+self.ram+" GB",self)
        self.ram_label.setStyleSheet("color:White")
        self.ram_label.setGeometry(10, 160, 450, 25)
        self.ram_label.setFont(QFont('Trajan', 11))
        
        #Local Ip
        self.loc_ip_label = QLabel("Local IP: "+self.local_ip,self)
        self.loc_ip_label.setStyleSheet("color:White")
        self.loc_ip_label.setGeometry(10, 190, 450, 25)
        self.loc_ip_label.setFont(QFont('Trajan', 11))
        
        #Public IP
        self.pub_ip_label = QLabel("Public IP: "+self.pub_ip,self)
        self.pub_ip_label.setStyleSheet("color:White")
        self.pub_ip_label.setGeometry(10, 220, 450, 25)
        self.pub_ip_label.setFont(QFont('Trajan', 11))
        
        #Download speed label
        self.download_speed_label = QLabel("Download speed: "+ self.download_speed_holder,self)
        self.download_speed_label.setStyleSheet("color:White")
        self.download_speed_label.setGeometry(10, 250, 450, 25)
        self.download_speed_label.setFont(QFont('Trajan', 11))
        
        #Upload speed label
        self.upload_speed_label = QLabel("Upload speed: "+ self.upload_speed_holder,self)
        self.upload_speed_label.setStyleSheet("color:White")
        self.upload_speed_label.setGeometry(10, 280, 450, 25)
        self.upload_speed_label.setFont(QFont('Trajan', 11))
        
        #Do speedtest button
        self.start_speedtest_button = QPushButton("Start Speedtest",self)
        self.start_speedtest_button.setGeometry(95, 320, 210, 30)
        self.start_speedtest_button.setStyleSheet("background-color: #0066CC; color: #FFFFFF; font-size: 16px; border-radius: 5px;")
        self.start_speedtest_button.clicked.connect(self.start_speedtest)
        self.start_speedtest_button.setFont(QFont('Trajan'))
        
        #ReturnButton
        self.return_button = QPushButton("Back",self)
        self.return_button.setStyleSheet("color:red")
        self.return_button.setStyleSheet("background-color: #0066CC; color: #FFFFFF; font-size: 16px; border-radius: 5px;")
        self.return_button.setGeometry(95, 360, 210, 30)
        self.return_button.clicked.connect(self.close)
        self.return_button.setFont(QFont('Trajan', 11))
 
 
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main_window()
    sys.exit(app.exec())