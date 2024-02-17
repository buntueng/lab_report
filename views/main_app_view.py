# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'main_app_view.ui'
##
# Created by: Qt User Interface Compiler version 6.6.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
                               QMenu, QMenuBar, QPushButton, QSizePolicy,
                               QSpacerItem, QStatusBar, QTextEdit, QVBoxLayout,
                               QWidget)
import resources.resource_file_rc


class Ui_main_app_view(object):
    def setupUi(self, main_app_view):
        if not main_app_view.objectName():
            main_app_view.setObjectName(u"main_app_view")
        main_app_view.resize(1283, 780)
        icon = QIcon()
        icon.addFile(u":/icons/icons/report.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        main_app_view.setWindowIcon(icon)
        self.actionCytology_Report = QAction(main_app_view)
        self.actionCytology_Report.setObjectName(u"actionCytology_Report")
        self.actionNecropsy_Report = QAction(main_app_view)
        self.actionNecropsy_Report.setObjectName(u"actionNecropsy_Report")
        self.actionSave_on_This_PC = QAction(main_app_view)
        self.actionSave_on_This_PC.setObjectName(u"actionSave_on_This_PC")
        self.actionSave_on_Server = QAction(main_app_view)
        self.actionSave_on_Server.setObjectName(u"actionSave_on_Server")
        self.actionLoad_from_this_PC = QAction(main_app_view)
        self.actionLoad_from_this_PC.setObjectName(u"actionLoad_from_this_PC")
        self.actionLoad_from_Server = QAction(main_app_view)
        self.actionLoad_from_Server.setObjectName(u"actionLoad_from_Server")
        self.actionConfirm_Report = QAction(main_app_view)
        self.actionConfirm_Report.setObjectName(u"actionConfirm_Report")
        self.actionApprove_Report = QAction(main_app_view)
        self.actionApprove_Report.setObjectName(u"actionApprove_Report")
        self.centralwidget = QWidget(main_app_view)
        self.centralwidget.setObjectName(u"centralwidget")
        self.page_widget = QWidget(self.centralwidget)
        self.page_widget.setObjectName(u"page_widget")
        self.page_widget.setGeometry(QRect(10, 10, 128, 721))
        self.page_widget.setStyleSheet(u"QWidget{\n"
                                       "	background-color: rgb(33, 200, 255);\n"
                                       "}")
        self.verticalLayout = QVBoxLayout(self.page_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.page_widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer_6 = QSpacerItem(
            20, 94, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.add_figure_pushButton = QPushButton(self.page_widget)
        self.add_figure_pushButton.setObjectName(u"add_figure_pushButton")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/add-image.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.add_figure_pushButton.setIcon(icon1)

        self.verticalLayout.addWidget(self.add_figure_pushButton)

        self.description_pushButton = QPushButton(self.page_widget)
        self.description_pushButton.setObjectName(u"description_pushButton")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/messages_white.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.description_pushButton.setIcon(icon2)

        self.verticalLayout.addWidget(self.description_pushButton)

        self.verticalSpacer_2 = QSpacerItem(
            20, 108, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.confirm_report_pushButton = QPushButton(self.page_widget)
        self.confirm_report_pushButton.setObjectName(
            u"confirm_report_pushButton")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/notifications_white.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.confirm_report_pushButton.setIcon(icon3)

        self.verticalLayout.addWidget(self.confirm_report_pushButton)

        self.verticalSpacer_4 = QSpacerItem(
            28, 338, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.sign_out_pushButton = QPushButton(self.page_widget)
        self.sign_out_pushButton.setObjectName(u"sign_out_pushButton")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/log_out_white.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.sign_out_pushButton.setIcon(icon4)

        self.verticalLayout.addWidget(self.sign_out_pushButton)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(140, 10, 1131, 721))
        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 1111, 91))
        self.widget.setStyleSheet(u"QWidget{\n"
                                  "	background-color: rgb(50, 50, 255);\n"
                                  "}\n"
                                  "QPushButton{\n"
                                  "color: rgb(0, 0,0);\n"
                                  "background-color: rgb(50, 255, 50);\n"
                                  "}\n"
                                  "\n"
                                  "QLabel{\n"
                                  "	color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "QLineEdit{\n"
                                  "	background-color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QTextEdit{\n"
                                  "background-color: rgb(255, 255, 255);\n"
                                  "}")
        self.case_number_label = QLabel(self.widget)
        self.case_number_label.setObjectName(u"case_number_label")
        self.case_number_label.setGeometry(QRect(10, 10, 81, 16))
        self.case_number_lineEdit = QLineEdit(self.widget)
        self.case_number_lineEdit.setObjectName(u"case_number_lineEdit")
        self.case_number_lineEdit.setGeometry(QRect(90, 10, 121, 22))
        self.case_info_textEdit = QTextEdit(self.widget)
        self.case_info_textEdit.setObjectName(u"case_info_textEdit")
        self.case_info_textEdit.setEnabled(False)
        self.case_info_textEdit.setGeometry(QRect(10, 40, 1091, 41))
        self.search_pushButton = QPushButton(self.widget)
        self.search_pushButton.setObjectName(u"search_pushButton")
        self.search_pushButton.setGeometry(QRect(220, 10, 75, 21))
        self.report_textEdit = QTextEdit(self.widget_3)
        self.report_textEdit.setObjectName(u"report_textEdit")
        self.report_textEdit.setEnabled(False)
        self.report_textEdit.setGeometry(QRect(10, 110, 1111, 601))
        main_app_view.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main_app_view)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1283, 22))
        self.menuCreate_Report = QMenu(self.menubar)
        self.menuCreate_Report.setObjectName(u"menuCreate_Report")
        self.menuManage_Report = QMenu(self.menubar)
        self.menuManage_Report.setObjectName(u"menuManage_Report")
        main_app_view.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main_app_view)
        self.statusbar.setObjectName(u"statusbar")
        main_app_view.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuCreate_Report.menuAction())
        self.menubar.addAction(self.menuManage_Report.menuAction())
        self.menuCreate_Report.addAction(self.actionCytology_Report)
        self.menuCreate_Report.addAction(self.actionNecropsy_Report)
        self.menuManage_Report.addAction(self.actionSave_on_This_PC)
        self.menuManage_Report.addAction(self.actionLoad_from_this_PC)
        self.menuManage_Report.addAction(self.actionSave_on_Server)
        self.menuManage_Report.addAction(self.actionLoad_from_Server)

        self.retranslateUi(main_app_view)

        QMetaObject.connectSlotsByName(main_app_view)
    # setupUi

    def retranslateUi(self, main_app_view):
        main_app_view.setWindowTitle(QCoreApplication.translate(
            "main_app_view", u"Report generator", None))
        self.actionCytology_Report.setText(QCoreApplication.translate(
            "main_app_view", u"Cytology Report", None))
        self.actionNecropsy_Report.setText(QCoreApplication.translate(
            "main_app_view", u"Necropsy Report", None))
        self.actionSave_on_This_PC.setText(QCoreApplication.translate(
            "main_app_view", u"Save on This PC", None))
        self.actionSave_on_Server.setText(QCoreApplication.translate(
            "main_app_view", u"Save on Server", None))
        self.actionLoad_from_this_PC.setText(QCoreApplication.translate(
            "main_app_view", u"Load from this PC", None))
        self.actionLoad_from_Server.setText(QCoreApplication.translate(
            "main_app_view", u"Load from Server", None))
        self.actionConfirm_Report.setText(QCoreApplication.translate(
            "main_app_view", u"Confirm Report", None))
        self.actionApprove_Report.setText(QCoreApplication.translate(
            "main_app_view", u"Approve Report", None))
        self.label.setText(QCoreApplication.translate(
            "main_app_view", u"Laboratory report", None))
        self.add_figure_pushButton.setText(
            QCoreApplication.translate("main_app_view", u"Add Figure", None))
        self.description_pushButton.setText(
            QCoreApplication.translate("main_app_view", u"Description", None))
        self.confirm_report_pushButton.setText(
            QCoreApplication.translate("main_app_view", u"Confirm Report", None))
        self.sign_out_pushButton.setText(
            QCoreApplication.translate("main_app_view", u"Sign Out", None))
        self.case_number_label.setText(QCoreApplication.translate(
            "main_app_view", u"Case Number", None))
        self.search_pushButton.setText(
            QCoreApplication.translate("main_app_view", u"Search", None))
        self.menuCreate_Report.setTitle(QCoreApplication.translate(
            "main_app_view", u"Create Report", None))
        self.menuManage_Report.setTitle(QCoreApplication.translate(
            "main_app_view", u"Load and Save", None))
    # retranslateUi
