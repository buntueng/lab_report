"""Main application controller module. This module contains the main application controller class."""
import os
import bs4
import shutil
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from debugging.debug_logging import logger


class MainApplicationController:
    """Main application controller class. This class is responsible for handling the main application view events."""

    enable_edit = False

    def __init__(self, main_view, session_model) -> None:
        self.main_view = main_view
        self.session_model = session_model
        self.main_view.add_figure_pushButton.clicked.connect(self.add_figure)
        self.main_view.preview_pushButton.clicked.connect(
            self.preview_report)
        self.main_view.new_cytology_pushButton.clicked.connect(
            self.load_new_cytology_report)
        self.main_view.new_nocropsy_pushButton.clicked.connect(
            self.load_new_nocropsy_report)
        self.main_view.load_report_pushButton.clicked.connect(
            self.load_report)
        self.main_view.save_report_pushButton.clicked.connect(
            self.save_report)
        self.main_view.confirm_report_pushButton.clicked.connect(
            self.confirm_report)

        self.main_view.check_report_pushButton.clicked.connect(
            self.check_report)
        self.main_view.signout_pushButton.clicked.connect(self.logout)

    def check_report(self) -> None:
        """Check the report for errors"""
        print("Checking report")

    def confirm_report(self) -> None:
        """Confirm the report and save it to the database server"""
        print("Confirming report")

    def save_report(self) -> None:
        """ save report to database server"""
        print("Saving report")

    def load_new_cytology_report(self) -> None:
        """Load new cytology report template to the main view"""
        print("Loading new cytology report")

    def load_new_nocropsy_report(self) -> None:
        """Load new nocropsy report template to the main view"""
        print("Loading new nocropsy report")

    def load_report(self) -> None:
        """Load report to the main view using open file dialog"""
        print("Loading report")

    def add_figure(self) -> None:
        """ Add figure to the main view using open file dialog"""
        # Open file dialog
        image_file_dialog = QFileDialog(
            self.main_view, "Open Image", "", "Image Files (*.png *.jpg *.bmp)")
        image_file_dialog.setFileMode(QFileDialog.ExistingFiles)
        image_file_dialog.setViewMode(QFileDialog.List)
        image_file_dialog.setAcceptMode(QFileDialog.AcceptOpen)

        if image_file_dialog.exec():
            # Get the selected file path
            file_path = image_file_dialog.selectedFiles()[0]
            # Check if the image is valid
            if file_path:
                # Get the file name from the file path
                file_name = os.path.basename(file_path)
                temp_file_path = os.path.join(
                    self.main_view.temp_dir, file_name)
                # Copy the file to the temporary directory
                shutil.copy(file_path, temp_file_path)

                desired_height = 200
                self.main_view.report_textEdit.insertHtml(
                    f'<img src="{temp_file_path}" height="{desired_height}"')
                # self.main_view.report_textEdit.insertHtml('<br>')
            else:
                logger.info("Invalid image file")
        else:
            logger.debug("No file selected")

    def preview_report(self) -> None:
        """read text from report_textEdit as html and print it to terminal"""
        html_text = self.main_view.report_textEdit.toHtml()
        # html process to get the paragraph text using bs4
        soup = bs4.BeautifulSoup(html_text, 'html.parser')
        paragraphs = soup.find_all('p')
        for paragraph in paragraphs:
            if paragraph.get_text() == '':
                if paragraph.find('img'):
                    all_img = paragraph.find_all('img')
                    for img in all_img:
                        print(img['src'])
            elif paragraph.find('img'):
                # show QmessageBox remind the user
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setInformativeText(
                    "Do not add text and image on the same line. \
                    \n!!! Recheck the report format and try again. !!!")
                msg.setWindowTitle("Report format error")
                msg.exec()
            else:
                print(paragraph.get_text())

    def logout(self) -> None:
        """Logout the user"""
        self.session_model.end_session()
        self.main_view.close()

    def enable_edit_report(self) -> None:
        """Enable the report text edit"""
        self.enable_edit = True
        self.main_view.report_textEdit.setEnabled(self.enable_edit)
