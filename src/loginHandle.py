from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, QThread, Signal, QUrl,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter, QDesktopServices,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

from login_ui import Ui_MainWindow
import time

class Worker(QThread):
    progress = Signal(int)

    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(101):
            self.progress.emit(i)
            time.sleep(0.1)

class MainHandle(Ui_MainWindow):
    def __init__(self):
        self.setupUi(mainWindow)

        #------------------------
        # login
        self.btOpenfile.hide()
        self.lnedtUsername.setPlaceholderText("Email or PhoneNumber LinkedIn")
        self.lnedtPassword.setPlaceholderText("Password")
        self.lnedtGroupID.setPlaceholderText("Link Group you want to get Members' Information")
        self.lnedtPassword.setEchoMode(QLineEdit.Password)

        # button submit
        self.btSubmit.clicked.connect(self.btHandle)


    def openFile(self):
        import os
        import datetime

        # folder_name = 'Scrape_memIn4_in_LinkedInGroup'
        file_name = f'Profiles-{datetime.datetime.now().strftime("%d-%m-%Y")}.csv'
        current_directory = os.getcwd()
        # folder_path = os.path.join(current_directory, folder_name)
        file_path = os.path.join(current_directory, file_name)
        QDesktopServices.openUrl(QUrl.fromLocalFile(file_path))

    def btHandle(self):
        import os

        email = self.lnedtUsername.text()
        password = self.lnedtPassword.text()
        linkGroup = self.lnedtGroupID.text()
        groupID = linkGroup.split("groups/")[1].split("/")[0]

        command = 'python src/scrape_profiles.py --email='+email+' --password='+password+' --group_ids='+groupID
        self.btOpenfile.show()
        self.btOpenfile.clicked.connect(self.openFile)
        os.system(command)
        
        
if __name__=="__main__":
    import sys
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    GUI = MainHandle()
    mainWindow.show()
    sys.exit(app.exec_())