from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

from login_ui import Ui_MainWindow

class MainHandle(Ui_MainWindow):
    def __init__(self):
        self.setupUi(mainWindow)

        #------------------------
        # login
        self.pgBar.hide()
        self.lnedtUsername.setPlaceholderText("Email or PhoneNumber LinkedIn")
        self.lnedtPassword.setPlaceholderText("Password")
        self.lnedtGroupID.setPlaceholderText("Link Group you want to get Members' Information")
        self.lnedtPassword.setEchoMode(QLineEdit.Password)
        self.spBNumMem.setMaximum(100)
        self.spBNumMem.setMinimum(0)
        self.spBNumMem.valueChanged.connect(self.spBsetNum)

        # button submit
        self.btSubmit.clicked.connect(self.btHandle)

    def spBsetNum(self):
        num = self.spBNumMem.value()
        return num

    def btHandle(self):
        import os

        
        email = self.lnedtUsername.text()
        password = self.lnedtPassword.text()
        linkGroup = self.lnedtGroupID.text()
        groupID = linkGroup.split("groups/")[1].split("/")[0]
        command = 'python src/scrape_profiles.py --email='+email+' --password='+password+' --group_ids='+groupID

        self.pgBar.show()

        os.system(command)
        
        
if __name__=="__main__":
    import sys
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    GUI = MainHandle()
    mainWindow.show()
    sys.exit(app.exec_())