'''
File: uci.py
Project: uci-py
Created Date: Friday, 17th July 2020 12:49:35 pm
-----
Author: Michael O'Connell
-----
Last Modified: Monday, 20th July 2020 12:53:10 pm
Modified By: Michael O'Connell
'''
import os
import re


class Config(object):

    def __init__(self, config, options):
        self.config = config
        self.options = options

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

    def read_config_file(self, filepath=None):
        if os.path.exists(filepath):
            self.filepath = filepath
            config_file = open(filepath, 'r')
            configs = []
            for line in config_file.readlines():

                if(line[0:6] == "config"):
                    config = line.split(" ")[2]

                    config2 = line.split(" ")[1]

                    configs.append({"config": [re.sub(
                        r'[^a-zA-Z0-9_.]', '', config), re.sub(r'[^a-zA-Z0-9_.]', '', config2)]})

                elif(line.lstrip().startswith("option")):
                    if(not "options" in configs[len(configs)-1]):
                        configs[len(configs) -
                                     1].update({"options": {}})
                    option = line.lstrip().split(" ")

                    # print(option)
                    configs[len(configs)-1]["options"].update(
                        {re.sub(r'[^a-zA-Z0-9_.]', '', option[1]): re.sub(r'[^a-zA-Z0-9_.]', '', option[2])})
            config_file.close()
            self.sections = []
            for i in configs:
                self.sections.append( Config(i["config"], i["options"]))
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
                    strout.append("\toption '%s' '%s'" % (option, config.options[option]))
                strout.append("\n")
            str = "\n"
            x = str.join(strout)
            cf = open(self.filepath, 'w')
            cf.write("# -*- mode: conf -*- \n# \n\n")
            cf.write(x)
            print(x)
