'''
File: configFileTest.py
Project: tests
Created Date: Friday, 17th July 2020 1:49:45 pm
-----
Author: Michael O'Connell
-----
Last Modified: Friday, 17th July 2020 3:46:44 pm
Modified By: Michael O'Connell
'''

import os, pprint

import pytest

from ucipy import uci


def test_uci_readfile():
    test = uci.ConfigFile().read_config_file("tests/testconfig") 
    #pprint.pprint(test)
    assert test != "Error", "Failed to read file"

def test_uci_fileParse():
    test = uci.ConfigFile().read_config_file("tests/testconfig") 
    assert test[2]["config"][0] == "IRI", "Failed to parse file"
    assert test[2]["config"][1] == "telemetry", "Failed to parse file"
    assert test[2]["config"][1] == "telemetry", "Failed to parse file"
    assert test[0]["options"]["base_dir"] == 'mntsdcardincoming', "Failed to parse file"

    
if __name__ == "__main__":
    test_uci_readfile()
    test_uci_fileParse()