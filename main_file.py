# -*- coding: utf-8 -*-
"""
Author: Nejc Ropič
Python version: 3.9
Date: 10.5.2024
"""

from PyQt5.QtWidgets import QMessageBox, QLCDNumber, QFileDialog
from PyQt5.QtCore import QTimer
from threading import Event
import os.path
import json
import xmltodict
import requests
###???
class Multi_test_main_func():
    def __init__(self, ui):
        """Naredimo potrebne značke"""
        # spremenljivke in funkcije iz Top_level
        self.ui = ui

    def refreshData(self, gui):
        """Funkcija, ki poveže GUI z GW_instek"""
        #url = requests.get('https://meteo.arso.gov.si/met/en/service2/')



        """with open("test.xml") as xml_file:
            data_dict = xmltodict.parse(xml_file.read())
            # xml_file.close()

            # generate the object using json.dumps()
            # corresponding to json data

            json_data = json.dumps(data_dict)

            # Write the json data to output
            # json file
            with open("data.json", "w") as json_file:
                json_file.write(json_data)"""