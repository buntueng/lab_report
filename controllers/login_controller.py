from PySide6.QtCore import Signal, QObject
from debugging.debug_logging import logger


class Communicate(QObject):
    """
    The main propose of Communicate class is create an object that inheritate from QObject and Signal.
    """
    success = Signal()


class LoginController:
    """ This class is responsible for handling the login view and the login model. It connects the login view and the login model together."""

    def __init__(self, login_view, user_model):
        """ Initialize the Login Controller"""
        self.login_view = login_view
        self.user_model = user_model
        self.login_view.login_button.clicked.connect(self.login)
        self.login_view.username_lineEdit.returnPressed.connect(self.login)
        self.login_view.password_lineEdit.returnPressed.connect(self.login)
        self.login_status = Communicate()

        self.user_info = []

    def login(self):
        """ This method is called when the login button is clicked. It gets the username and password from the login view and calls the authenticate method of the user model. If the authentication is successful, it closes the login window."""
        username = self.login_view.username_lineEdit.text()
        password = self.login_view.password_lineEdit.text()

        if not username == "" and not password == "":
            self.user_info = self.user_model.authenticate(username, password)
            if len(self.user_info) == 1:
                logger.info(self.user_info)
                self.login_status.success.emit()
                self.login_view.close_login_window()
            else:
                self.login_view.clear_login_form()
        else:
            pass
