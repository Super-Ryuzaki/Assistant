import sys
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import pcspecs
import installer
import hibp
import windowutil
import pcspecs

try:
    from PyQt5.QtGui import QPalette, QColor
    from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QSpacerItem, QSizePolicy
    from PyQt5.QtCore import Qt
except:
    os.system("pip install pyqt5")
    os.system("pip install wget")
    os.system("pip install requests")
    from PyQt5.QtGui import QPalette, QColor
    from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QSpacerItem, QSizePolicy
    from PyQt5.QtCore import Qt
    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # set window title and fixed size
        self.setWindowTitle("Assistant")
        self.setFixedSize(400, 400)

        # set window background color
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(47, 47, 47))
        self.setPalette(palette)

        # create buttons with new styling
        font = QFont()
        font.setFamily("Trajan")
        font.setPointSize(16)
        font.setBold(True)

        self.pcspecs_button = QPushButton("PC specifications", self)
        self.pcspecs_button.setGeometry(50, 50, 300, 50)
        self.pcspecs_button.setStyleSheet("background-color: #0066CC; color: #FFFFFF; font-size: 20px; border-radius: 5px;")
        self.pcspecs_button.setFont(font)
        self.pcspecs_button.clicked.connect(self.open_pcspecs)

        self.installer_button = QPushButton("Installer", self)
        self.installer_button.setGeometry(50, 120, 300, 50)
        self.installer_button.setStyleSheet("background-color: #0066CC; color: #FFFFFF; font-size: 20px; border-radius: 5px;")
        self.installer_button.setFont(font)
        self.installer_button.clicked.connect(self.open_installer)

        self.hibp_button = QPushButton("Have i been pawned", self)
        self.hibp_button.setGeometry(50, 190, 300, 50)
        self.hibp_button.setStyleSheet("background-color: #0066CC; color: #FFFFFF; font-size: 20px; border-radius: 5px;")
        self.hibp_button.setFont(font)
        self.hibp_button.clicked.connect(self.open_hibp)

        self.windowutil_button = QPushButton("Window Utilities", self)
        self.windowutil_button.setGeometry(50, 260, 300, 50)
        self.windowutil_button.setStyleSheet("background-color: #0066CC; color: #FFFFFF; font-size: 20px; border-radius: 5px;")
        self.windowutil_button.setFont(font)
        self.windowutil_button.clicked.connect(self.open_windowutil)

    def open_pcspecs(self):
        pcspecs_window = pcspecs.pcspecs_window()
        self.setCentralWidget(pcspecs_window)

    def open_installer(self):
        installer_window = installer.installer_window()
        self.setCentralWidget(installer_window)

    def open_hibp(self):
        hibp_window = hibp.HIBPWindow()
        self.setCentralWidget(hibp_window)

    def open_windowutil(self):
        windutil = windowutil.windows_util_window()
        self.setCentralWidget(windutil)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
