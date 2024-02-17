""" Login Model handles the database connection and authentication """
import os
import yaml
import mariadb
from debugging.debug_logging import logger


class LoginModel:
    """" Login Model handles the database connection and authentication """

    def __init__(self) -> None:
        """ Initialize the Login Model """
        self.user_info = []
        config_path = os.path.join(os.path.dirname(__file__), 'config.yml')
        self.db_connector = None
        self.config_params = None
        if os.path.exists(config_path):
            with open(config_path, 'r', encoding='utf-8') as yamfile:
                self.config_params = yaml.safe_load(yamfile)
        else:
            logger.error("Config file not found")

        if len(self.config_params) > 0:
            try:
                self.db_connector = mariadb.connect(
                    host=str(self.config_params['server_ip']),
                    database=str(self.config_params['database_name']),
                    port=self.config_params['server_port'],
                    user=str(self.config_params['username']),
                    password=str(self.config_params['password']))
            except mariadb.Error as e:
                logger.error("Error connecting to the database: %s", e)

    def connect_database(self) -> bool:
        """ Connect to the database"""
        logger.info("Connecting to the database")
        db_status = False
        if self.db_connector:
            try:
                self.db_connector.connect()
                db_status = True
            except mariadb.Error as e:
                logger.error("Error connecting to the database: %s", e)
        return db_status

    def authenticate(self, username, password) -> list:
        """" Authenticate the user if user are in employee table return the user information"""
        logger.info("Authenticating user")
        user_info = []
        if self.db_connector:
            cursor = self.db_connector.cursor()
            cursor.execute(
                self.config_params['data_query']['get_user_info'], (username, password))
            user_info = cursor.fetchall()
        return user_info
