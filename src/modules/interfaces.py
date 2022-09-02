import os
import requests
from bs4 import BeautifulSoup


class Module:
    envs = []

    def __init__(self):
        """Retrieves username and password from environment secrets."""

        self.name = self.__class__.__name__.upper()

        try:
            user_env = self.name + '_USER'
            password_env = self.name + '_PASSWORD'
            self.user = os.environ[user_env]
            self.password = os.environ[password_env]
            Module.envs.append(user_env)
            Module.envs.append(password_env)
            self.valid = True
        except KeyError as e:
            print(f"Invalid environment variable {e}")
            self.valid = False

        self.session = requests.Session()
        self.initialized = False

    def run(self, assignments):
        if not self.valid:
            return
        self._init()

        if not self.initialized:
            return print(f"Unable to initialize '{self.name}'")
        self._main(assignments)

    def _init(self):
        """Sets up the web scraper."""

        raise NotImplementedError

    def _main(self, assignments):
        """Parses the webpage for assignments and adds them to ASSIGNMENTS."""

        raise NotImplementedError

    #################################
    #       Helper Functions        #
    #################################
    @staticmethod
    def parse_html(html):
        return BeautifulSoup(html, 'html.parser')
