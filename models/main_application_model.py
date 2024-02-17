""" This module contains the main application model. It is responsible for managing the state of the application."""


class MainApplicationModel:
    """ This is the main application model. It is responsible for managing the state of the application."""

    def __init__(self):
        """ This is the main application model. It is responsible for managing the state of the application. """
        self.session_active = False

    def start_session(self):
        """ This method is called when the user logs in. It sets the session_active attribute to True."""
        self.session_active = True

    def end_session(self):
        """ This method is called when the user logs out. It sets the session_active attribute to False."""
        self.session_active = False
