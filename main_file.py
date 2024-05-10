# -*- coding: utf-8 -*-
"""
Author: Nejc Ropič
Python version: 3.9
Date: 10.5.2024
"""

from PyQt5.QtWidgets import QTableWidgetItem, QLabel
from PyQt5.QtGui import QPixmap
from urllib.request import urlopen
from bs4 import BeautifulSoup

class Multi_test_main_func():
    def __init__(self, ui, urls):
        """Naredimo potrebne značke"""
        # spremenljivke in funkcije iz Top_level
        self.ui = ui
        self.urls = urls

        # dictionary for data
        self.database = []

        # lists for usage
        self.url_list = []
        self.temperature_list = []
        self.wind_icon_list = []
        self.wind_speed_list = []
        self.pressure_list = []

    def selectcity(self):
        index = self.ui.citiesComboBox.currentIndex()
        citylink = "https://meteo.arso.gov.si" + self.urls[index]
        page = urlopen(citylink)
        html = page.read().decode("utf-8")
        citydata = BeautifulSoup(html, "html.parser")
        return citydata

    def refreshdata(self):
        """Funkcija, ki poveže GUI z GW_instek"""
        self.getdata()

    def getdata(self):
        self.database = []
        city = self.selectcity()
        # get temperatures
        for i in city.find_all('td', {"class": "t"}):
            self.temperature_list.append(i.get_text())

        # get wind speed
        for i in city.find_all('td', {"class": "ff_val"}):
            self.wind_speed_list.append(i.get_text())

        # get pressure
        for i in city.find_all('td', {"class": "msl"}):
            self.pressure_list.append(i.get_text())

        for i in range(len(self.wind_speed_list)):
            local_database =  {"temperature": self.temperature_list[i],
                       "wind_speed": self.wind_speed_list[i],
                       "pressure": self.pressure_list[i]}
            self.database.append(local_database)

        self.temperature_list = []
        self.wind_speed_list = []
        self.pressure_list = []

    def showdata(self):
        self.getdata()
        data = self.database
        row = 0
        self.ui.cityesTable.setRowCount(len(data))
        for onedata in data:
            self.ui.cityesTable.setItem(row, 1, QTableWidgetItem(onedata["temperature"]))
            self.ui.cityesTable.setItem(row, 2, QTableWidgetItem(onedata["wind_speed"]))
            self.ui.cityesTable.setItem(row, 3, QTableWidgetItem(onedata["pressure"]))
            row = row + 1


