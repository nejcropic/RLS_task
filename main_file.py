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


class MainFileDataProcess:
    def __init__(self, ui, urls, domain):
        """Naredimo potrebne značke"""
        # instances from Top_level
        self.ui = ui
        self.urls = urls
        self.domain = domain

        # dictionary for data
        self.database = []

        # lists for usage
        self.url_list = []
        self.date_list = []
        self.temperature_list = []
        self.wind_icon_list = []
        self.wind_speed_list = []
        self.pressure_list = []

    def selectcity(self, index):
        """Funcion for city selection from combobox"""
        # selecting city
        citylink = self.domain + self.urls[index]
        page = urlopen(citylink)
        html = page.read().decode("utf-8")
        citydata = BeautifulSoup(html, "html.parser")
        return citydata

    def getdata(self, index):
        """"Function for extracting data from website"""
        self.database = []
        city = self.selectcity(index)

        # get date
        for i in city.find_all('td', {"class": "meteoSI-th"}):
            self.date_list.append(i.get_text())

        # get temperatures
        for i in city.find_all('td', {"class": "t"}):
            self.temperature_list.append(i.get_text())

        # get wind speed
        for i in city.find_all('td', {"class": "ff_val"}):
            self.wind_speed_list.append(i.get_text())

        # get pressure
        for i in city.find_all('td', {"class": "msl"}):
            text = i.get_text()

            # text can return "*\n\t\t" before number
            try:
                text = int(text)
            except ValueError:
                todelete = list(text)
                del todelete[:4]
                text = ''.join(todelete)

            if text == "":
                text = "nA"

            self.pressure_list.append(str(text))

        # store each row of data in dictionary
        for i in range(len(self.wind_speed_list)):
            local_database =  {
                "date": self.date_list[i],
                "temperature": self.temperature_list[i],
                "wind_speed": self.wind_speed_list[i],
                "pressure": self.pressure_list[i]}
            # store individual dict(row) in table
            self.database.append(local_database)

        # clear table data
        self.date_list = []
        self.temperature_list = []
        self.wind_speed_list = []
        self.pressure_list = []

        return self.database

