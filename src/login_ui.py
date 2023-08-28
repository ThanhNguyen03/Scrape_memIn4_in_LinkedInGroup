# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLineEdit, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(518, 410)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.grbUsername = QGroupBox(self.centralwidget)
        self.grbUsername.setObjectName(u"grbUsername")
        self.grbUsername.setGeometry(QRect(70, 40, 381, 61))
        self.lnedtUsername = QLineEdit(self.grbUsername)
        self.lnedtUsername.setObjectName(u"lnedtUsername")
        self.lnedtUsername.setGeometry(QRect(70, 20, 291, 31))
        self.btSubmit = QPushButton(self.centralwidget)
        self.btSubmit.setObjectName(u"btSubmit")
        self.btSubmit.setGeometry(QRect(240, 330, 93, 28))
        self.grbPassword = QGroupBox(self.centralwidget)
        self.grbPassword.setObjectName(u"grbPassword")
        self.grbPassword.setGeometry(QRect(70, 110, 381, 61))
        self.lnedtPassword = QLineEdit(self.grbPassword)
        self.lnedtPassword.setObjectName(u"lnedtPassword")
        self.lnedtPassword.setGeometry(QRect(70, 20, 291, 31))
        self.grbGroupID = QGroupBox(self.centralwidget)
        self.grbGroupID.setObjectName(u"grbGroupID")
        self.grbGroupID.setGeometry(QRect(70, 180, 381, 61))
        self.lnedtGroupID = QLineEdit(self.grbGroupID)
        self.lnedtGroupID.setObjectName(u"lnedtGroupID")
        self.lnedtGroupID.setGeometry(QRect(70, 20, 291, 31))
        self.prgBRun = QProgressBar(self.centralwidget)
        self.prgBRun.setObjectName(u"prgBRun")
        self.prgBRun.setGeometry(QRect(80, 270, 301, 21))
        self.prgBRun.setValue(24)
        self.btDownload = QPushButton(self.centralwidget)
        self.btDownload.setObjectName(u"btDownload")
        self.btDownload.setGeometry(QRect(390, 270, 71, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 518, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.grbUsername.setTitle(QCoreApplication.translate("MainWindow", u"Email or PhoneNumber", None))
        self.lnedtUsername.setText("")
        self.btSubmit.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.grbPassword.setTitle(QCoreApplication.translate("MainWindow", u"PassWord", None))
        self.lnedtPassword.setText("")
        self.grbGroupID.setTitle(QCoreApplication.translate("MainWindow", u"Group ID", None))
        self.lnedtGroupID.setText("")
        self.btDownload.setText(QCoreApplication.translate("MainWindow", u"Download", None))
    # retranslateUi

