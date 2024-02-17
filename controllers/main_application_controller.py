class MainApplicationController:
    def __init__(self, main_view, session_model):
        self.main_view = main_view
        self.session_model = session_model

    def logout(self):
        self.session_model.end_session()
        self.main_view.close()
