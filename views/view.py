"""" This module is responsible for handling the views of the application. It connects the views to the models and the controllers."""
from PySide6.QtWidgets import QApplication, QMainWindow
from views.login_view import Ui_login_view
from views.main_app_view import Ui_main_app_view


class LoginView(QMainWindow, Ui_login_view):
    """" This class is responsible for handling the login view and the login model. It connects the login view and the login model together."""

    def __init__(self):
        """ Initialize the Login View"""
        super().__init__()
        self.setupUi(self)
        self.username_lineEdit.setFocus()  # Set focus to username_lineEdit

    def show_login_error(self):
        """ Show login error message"""
        print("Error")

    def clear_login_form(self):
        """ Clear login form"""
        self.username_lineEdit.clear()
        self.password_lineEdit.clear()
        self.username_lineEdit.setFocus()  # Set focus to username_lineEdit

    def close_login_window(self):
        """ Close login window """
        self.close()
        print("Open main window")


class MainView(QMainWindow, Ui_main_app_view):
    """" This class is responsible for handling the main application view."""

    def __init__(self):
        """ Initialize the Main View"""
        super().__init__()
        self.setupUi(self,)
