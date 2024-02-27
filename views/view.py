"""" This module is responsible for handling the views of the application. It connects the views to the models and the controllers."""
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtWidgets import QLineEdit
from views.login_view import Ui_login_view
from views.main_app_view import Ui_main_app_view
from PySide6.QtGui import QImage
from debugging.debug_logging import logger
import os
import tempfile
import shutil


class LoginView(QMainWindow, Ui_login_view):
    """" This class is responsible for handling the login view and the login model. It connects the login view and the login model together."""

    def __init__(self) -> None:
        """ Initialize the Login View"""
        super().__init__()
        self.setupUi(self)
        self.username_lineEdit.setFocus()  # Set focus to username_lineEdit
        self.password_lineEdit.setEchoMode(
            QLineEdit.Password)  # Set echo mode to Password

    def show_login_error(self) -> None:
        """ Show login error message"""
        print("Error")

    def clear_login_form(self) -> None:
        """ Clear login form"""
        self.username_lineEdit.clear()
        self.password_lineEdit.clear()
        self.username_lineEdit.setFocus()  # Set focus to username_lineEdit

    def close_login_window(self) -> None:
        """ Close login window """
        self.close()
        print("Open main window")


class MainView(QMainWindow, Ui_main_app_view):
    """" This class is responsible for handling the main application view."""

    def __init__(self):
        """ Initialize the Main View"""
        super().__init__()
        self.setupUi(self,)
        self.temp_dir = tempfile.mkdtemp(prefix="reg_desk")
        self.report_textEdit.setEnabled(True)
        # Set the font size
        self.report_font = self.report_textEdit.font()
        # Replace 12 with your desired font size
        self.report_font.setPointSize(16)
        self.report_textEdit.setFont(self.report_font)

    def __del__(self) -> None:
        # Remove the temporary directory
        if os.path.exists(self.temp_dir):
            os.rmdir(self.temp_dir)
