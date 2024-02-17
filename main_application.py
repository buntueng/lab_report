""" This is the main application file. It is the entry point of the application. It creates the application and starts the event loop. It also creates the models, views and controllers and connects them together. """

import sys
from PySide6.QtWidgets import QApplication
from controllers.login_controller import LoginController
from controllers.main_application_controller import MainApplicationController
from models.login_model import LoginModel
from models.main_application_model import MainApplicationModel
from views.view import MainView, LoginView
from debugging.debug_logging import logger


if __name__ == "__main__":
    logger.info('Starting the application')

    app = QApplication(sys.argv)

    login_view = LoginView()
    main_view = MainView()
    login_model = LoginModel()
    main_application_model = MainApplicationModel()

    login_controller = LoginController(login_view, login_model)
    main_controller = MainApplicationController(
        main_view, main_application_model)

    login_controller.login_status.success.connect(
        lambda: main_view.show())  # lambda is intentional, do not modify

    login_view.show()
    sys.exit(app.exec())
