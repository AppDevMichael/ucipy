'''
File: uci.py
Project: uci-py
Created Date: Friday, 17th July 2020 12:49:35 pm
-----
Author: Michael O'Connell
-----
Last Modified: Friday, 17th July 2020 1:37:36 pm
Modified By: Michael O'Connell
'''


class ConfigFile():
    """
    ConfigFile Class for interacting with UCI formatted config files
    """

    def __init__(self, filepath=None):
        """
        __init__ Reads UCI formatted file and puts them into a list of objects

        Args:
            filepath (string, optional): The path to a config file. Defaults to None.
        """

        self.filepath = filepath
        if self.filepath:
            self.sections = self.read_config_file()
