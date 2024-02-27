# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_app_view.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
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
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_main_app_view(object):
    def setupUi(self, main_app_view):
        if not main_app_view.objectName():
            main_app_view.setObjectName(u"main_app_view")
        main_app_view.resize(1360, 870)
        icon = QIcon()
        icon.addFile(u":/icons/icons/report.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.page_widget.setGeometry(QRect(10, 10, 161, 831))
        self.page_widget.setMinimumSize(QSize(0, 721))
        self.page_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(33, 200, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(80,170,255);\n"
"	border: 2px solid black;\n"
"	height: 30px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.page_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.new_cytology_pushButton = QPushButton(self.page_widget)
        self.new_cytology_pushButton.setObjectName(u"new_cytology_pushButton")

        self.verticalLayout.addWidget(self.new_cytology_pushButton)

        self.new_nocropsy_pushButton = QPushButton(self.page_widget)
        self.new_nocropsy_pushButton.setObjectName(u"new_nocropsy_pushButton")

        self.verticalLayout.addWidget(self.new_nocropsy_pushButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.add_figure_pushButton = QPushButton(self.page_widget)
        self.add_figure_pushButton.setObjectName(u"add_figure_pushButton")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/add-image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_figure_pushButton.setIcon(icon1)

        self.verticalLayout.addWidget(self.add_figure_pushButton)

        self.preview_pushButton = QPushButton(self.page_widget)
        self.preview_pushButton.setObjectName(u"preview_pushButton")

        self.verticalLayout.addWidget(self.preview_pushButton)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.load_report_pushButton = QPushButton(self.page_widget)
        self.load_report_pushButton.setObjectName(u"load_report_pushButton")

        self.verticalLayout.addWidget(self.load_report_pushButton)

        self.save_report_pushButton = QPushButton(self.page_widget)
        self.save_report_pushButton.setObjectName(u"save_report_pushButton")

        self.verticalLayout.addWidget(self.save_report_pushButton)

        self.confirm_report_pushButton = QPushButton(self.page_widget)
        self.confirm_report_pushButton.setObjectName(u"confirm_report_pushButton")

        self.verticalLayout.addWidget(self.confirm_report_pushButton)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.check_report_pushButton = QPushButton(self.page_widget)
        self.check_report_pushButton.setObjectName(u"check_report_pushButton")

        self.verticalLayout.addWidget(self.check_report_pushButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.signout_pushButton = QPushButton(self.page_widget)
        self.signout_pushButton.setObjectName(u"signout_pushButton")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/log_out_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.signout_pushButton.setIcon(icon2)

        self.verticalLayout.addWidget(self.signout_pushButton)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(180, 10, 1171, 831))
        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 1161, 121))
        self.widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(50, 50, 255);\n"
"}\n"
"QPushButton{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(80,170,255);\n"
"	border: 2px solid black;\n"
"	height: 50px;\n"
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
        self.case_number_lineEdit.setGeometry(QRect(10, 30, 181, 31))
        self.case_info_textEdit = QTextEdit(self.widget)
        self.case_info_textEdit.setObjectName(u"case_info_textEdit")
        self.case_info_textEdit.setEnabled(False)
        self.case_info_textEdit.setGeometry(QRect(10, 70, 1141, 41))
        self.search_pushButton = QPushButton(self.widget)
        self.search_pushButton.setObjectName(u"search_pushButton")
        self.search_pushButton.setGeometry(QRect(200, 10, 121, 51))
        self.report_textEdit = QTextEdit(self.widget_3)
        self.report_textEdit.setObjectName(u"report_textEdit")
        self.report_textEdit.setEnabled(False)
        self.report_textEdit.setGeometry(QRect(10, 140, 1151, 681))
        main_app_view.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(main_app_view)
        self.statusbar.setObjectName(u"statusbar")
        main_app_view.setStatusBar(self.statusbar)

        self.retranslateUi(main_app_view)

        QMetaObject.connectSlotsByName(main_app_view)
    # setupUi

    def retranslateUi(self, main_app_view):
        main_app_view.setWindowTitle(QCoreApplication.translate("main_app_view", u"Report generator", None))
        self.actionCytology_Report.setText(QCoreApplication.translate("main_app_view", u"Cytology Report", None))
        self.actionNecropsy_Report.setText(QCoreApplication.translate("main_app_view", u"Necropsy Report", None))
        self.actionSave_on_This_PC.setText(QCoreApplication.translate("main_app_view", u"Save on This PC", None))
        self.actionSave_on_Server.setText(QCoreApplication.translate("main_app_view", u"Save on Server", None))
        self.actionLoad_from_this_PC.setText(QCoreApplication.translate("main_app_view", u"Load from this PC", None))
        self.actionLoad_from_Server.setText(QCoreApplication.translate("main_app_view", u"Load from Server", None))
        self.actionConfirm_Report.setText(QCoreApplication.translate("main_app_view", u"Confirm Report", None))
        self.actionApprove_Report.setText(QCoreApplication.translate("main_app_view", u"Approve Report", None))
        self.new_cytology_pushButton.setText(QCoreApplication.translate("main_app_view", u"New Cytology Report", None))
        self.new_nocropsy_pushButton.setText(QCoreApplication.translate("main_app_view", u"New Nocropsy Report", None))
        self.add_figure_pushButton.setText(QCoreApplication.translate("main_app_view", u"Add Figure", None))
        self.preview_pushButton.setText(QCoreApplication.translate("main_app_view", u"Preview Report", None))
        self.load_report_pushButton.setText(QCoreApplication.translate("main_app_view", u"Load Report", None))
        self.save_report_pushButton.setText(QCoreApplication.translate("main_app_view", u"Save Report", None))
        self.confirm_report_pushButton.setText(QCoreApplication.translate("main_app_view", u"Confirm Report", None))
        self.check_report_pushButton.setText(QCoreApplication.translate("main_app_view", u"Check reports", None))
        self.signout_pushButton.setText(QCoreApplication.translate("main_app_view", u"Sign Out", None))
        self.case_number_label.setText(QCoreApplication.translate("main_app_view", u"Case Number", None))
        self.search_pushButton.setText(QCoreApplication.translate("main_app_view", u"Search", None))
    # retranslateUi

