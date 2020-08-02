'''
File: uci.py
Project: uci-py
Created Date: Friday, 17th July 2020 12:49:35 pm
-----
Author: Michael O'Connell
-----
Last Modified: Sunday, 2nd August 2020 4:47:00 pm
Modified By: Michael O'Connell
'''
import os
import re
import shlex
from pprint import pprint


class Config(object):

    def __init__(self, config, options):
        self.config = config
        self.options = options


class Section():

    def __init__(self, type, name, options: dict, lists: dict):
        self.name = name
        self.type = type
        self.options = options
        self.lists = lists
        # pprint(name)
        # pprint(type)
        # print(lists)
        # pprint(lists)

    def __str__(self):
        if(self.lists == []):
            dict = {"config": [self.name, self.type], "options": self.options}
        else:
            dict = {"config": [self.name, self.type],
                    "options": self.options, "lists": self.lists}
        return dict.__str__()


class ConfigFile():
    """
    ConfigFile Class for interacting with UCI formatted config files
    """
    sections = []

    def __init__(self, filepath: str = '') -> str:
        """
        __init__ Reads UCI formatted file and puts them into a list of objects

        Args:
            filepath (str, optional): The path to a config file. Defaults to ''.
        """

        self.filepath = filepath
        if not self.filepath == '':
            self.sections = self.read_config_file()

    def parseConfFile(self, file: _io.TextIOWrapper):
        """
        parseConfFile Parses the raw text input from the file into section objects

        Args:
            file (_io.TextIOWrapper): Contents of the config file
        """
        options = {}
        config = []
        lists = {}
        for line in file:
            if(line.lstrip() != ''):
                if(line and line.lstrip()[0] == '#'):
                    # TODO: read comments to place back on save
                    pass
                else:
                    parts = shlex.split(line)
                    if(parts[0] == 'config'):
                        if(config):
                            tmp = Section(config[0], config[1], options, lists)
                            self.sections.append(tmp)
                            options = {}
                            config = []
                            lists = {}
                        config = parts[1:]
                    elif(parts[0] == 'option'):
                        options.update({parts[1]: parts[2]})
                    elif(parts[0] == 'list'):
                        if(not parts[1] in lists):
                            lists.update({parts[1]: [parts[2]]})
                        else:
                            lists[parts[1]].append(parts[2])

    def read_config_file(self, filepath: str):
        """
        read_config_file Reads and parses the config file into objects

        Args:
            filepath (str): The path to the configuration file
        """
        if os.path.exists(filepath):
            self.filepath = filepath
            config_file = open(filepath, 'r')
            print(type(config_file))
            self.parseConfFile(config_file)
            return(self.sections)
        else:
            return("Error")

    def save(self):

        if(self.sections):
            strout = []

            for config in self.sections:
                strout.append(
                    "config " + config.config[1] + " '" + config.config[0] + "'")
                for option in config.options.keys():
                    strout.append("\toption '%s' '%s'" %
                                  (option, config.options[option]))
                strout.append("\n")
            str = "\n"
            x = str.join(strout)
            cf = open(self.filepath, 'w')
            cf.write("# -*- mode: conf -*- \n# \n\n")
            cf.write(x)
            print(x)
