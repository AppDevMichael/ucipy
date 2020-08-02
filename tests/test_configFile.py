'''
File: configFileTest.py
Project: tests
Created Date: Friday, 17th July 2020 1:49:45 pm
-----
Author: Michael O'Connell
-----
Last Modified: Sunday, 2nd August 2020 4:34:51 pm
Modified By: Michael O'Connell
'''

import os, pprint

#import pytest

from ucipy import uci


def test_uci_readfile():
    test = uci.ConfigFile()
    test.read_config_file("./testconfig") 
    print(test.sections[1])
    #assert test == "Error", "Failed to read file"

# def test_uci_fileParse():
#     test = uci.ConfigFile()
#     test.read_config_file("tests/testconfig") 
#     section = test.sections
#     assert section[2].config[0] == "telemetry", "Failed to parse file"
#     assert section[2].config[1] == "IRI", "Failed to parse file"
#     assert section[0].options["base_dir"] == 'mntsdcardincoming', "Failed to parse file"

# def test_uci_save():
#     test = uci.ConfigFile()
#     test.read_config_file("tests/testconfig") 
#     test.save()

    
if __name__ == "__main__":
    test_uci_readfile()
    # test_uci_fileParse()
    # test_uci_save()