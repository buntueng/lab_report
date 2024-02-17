# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_view.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_login_view(object):
    def setupUi(self, login_view):
        if not login_view.objectName():
            login_view.setObjectName(u"login_view")
        login_view.resize(346, 127)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(login_view.sizePolicy().hasHeightForWidth())
        login_view.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(login_view)
        self.centralwidget.setObjectName(u"centralwidget")
        self.username_lineEdit = QLineEdit(self.centralwidget)
        self.username_lineEdit.setObjectName(u"username_lineEdit")
        self.username_lineEdit.setGeometry(QRect(20, 30, 171, 22))
        self.password_lineEdit = QLineEdit(self.centralwidget)
        self.password_lineEdit.setObjectName(u"password_lineEdit")
        self.password_lineEdit.setGeometry(QRect(20, 80, 171, 22))
        self.username_label = QLabel(self.centralwidget)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setGeometry(QRect(20, 10, 61, 16))
        self.password_label = QLabel(self.centralwidget)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setGeometry(QRect(20, 60, 61, 16))
        self.login_button = QPushButton(self.centralwidget)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(210, 30, 111, 71))
        login_view.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(login_view)
        self.statusbar.setObjectName(u"statusbar")
        login_view.setStatusBar(self.statusbar)

        self.retranslateUi(login_view)

        QMetaObject.connectSlotsByName(login_view)
    # setupUi

    def retranslateUi(self, login_view):
        login_view.setWindowTitle(QCoreApplication.translate("login_view", u"Login page", None))
        self.username_label.setText(QCoreApplication.translate("login_view", u"Username", None))
        self.password_label.setText(QCoreApplication.translate("login_view", u"Password", None))
        self.login_button.setText(QCoreApplication.translate("login_view", u"Login", None))
    # retranslateUi

