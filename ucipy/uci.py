'''
File: uci.py
Project: uci-py
Created Date: Friday, 17th July 2020 12:49:35 pm
-----
Author: Michael O'Connell
-----
Last Modified: Monday, 20th July 2020 12:19:27 pm
Modified By: Michael O'Connell
'''
import os
import re


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
            self.configs = []
            for line in config_file.readlines():

                if(line[0:6] == "config"):
                    config = line.split(" ")[2]

                    config2 = line.split(" ")[1]

                    self.configs.append({"config": [re.sub(
                        r'[^a-zA-Z0-9_.]', '', config), re.sub(r'[^a-zA-Z0-9_.]', '', config2)]})

                elif(line.lstrip().startswith("option")):
                    if(not "options" in self.configs[len(self.configs)-1]):
                        self.configs[len(self.configs) -
                                     1].update({"options": {}})
                    option = line.lstrip().split(" ")

                    # print(option)
                    self.configs[len(self.configs)-1]["options"].update(
                        {re.sub(r'[^a-zA-Z0-9_.]', '', option[1]): re.sub(r'[^a-zA-Z0-9_.]', '', option[2])})
            config_file.close()
            return(self.configs)
        else:
            return("Error")

    def save(self):

        if(self.configs):
            strout = []

            for config in self.configs:
                strout.append(
                    "config " + config["config"][1] + " '" + config["config"][0] + "'")
                for option in config["options"].keys():
                    strout.append("\toption '%s' '%s'" % (option, config["options"][option]))
                strout.append("\n")
            str = "\n"
            x = str.join(strout)
            cf = open(self.filepath, 'w')
            cf.write("# -*- mode: conf -*- \n# \n\n")
            cf.write(x)
            print(x)