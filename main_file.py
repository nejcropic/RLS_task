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
import numpy as np
import logging

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='app.log',  # Log messages are written to this file
                    filemode='w')  # 'w' for overwrite; use 'a' to append


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
        self.wind_direction_list = []
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
        errors = []
        error_num = 0
        for i in city.find_all('td', {"class": "t"}):
            try:
                temp = float(i.get_text())
                item = str(temp)
            # html returns &nbsp (nonbreaking space) if there is no data
            except (ValueError, TypeError) as e:
                error_num = error_num + 1
                errors.append(e)
                if len(errors) > 1:
                    if errors[len(errors)-1] == e:
                        errors.pop()
                temp = np.nan
            self.temperature_list.append(item)
        if error_num > 0:
            logging.warning("Errors converting temperature:")
            for err in errors:
                logging.warning("- %s", err)

        # get wind direction
        errors = []
        error_num = 0
        for i in city.find_all('td', {"class": "ddff_icon"}):
            direction = i.find('img')
            try:
                direction = direction['src'][33:-4]
                item = str(direction)
            # html returns &nbsp (nonbreaking space) if there is no data
            except (ValueError, TypeError) as e:
                error_num = error_num + 1
                errors.append(e)
                if len(errors) > 1:
                    if errors[len(errors)-1] == e:
                        errors.pop()
                direction = np.nan
            self.wind_direction_list.append(item)
        if error_num > 0:
            logging.warning("Errors converting wind direction:")
            for err in errors:
                logging.warning("- %s", err)

        # get wind speed
        errors = []
        error_num = 0
        for i in city.find_all('td', {"class": "ff_val"}):
            try:
                speed = float(i.get_text())
                item = str(speed)
            # html returns &nbsp (nonbreaking space) if there is no data
            except (ValueError, TypeError) as e:
                error_num = error_num + 1
                errors.append(e)
                if len(errors) > 1:
                    if errors[len(errors)-1] == e:
                        errors.pop()
                speed = np.nan
            self.wind_speed_list.append(item)
        if error_num > 0:
            logging.warning("Errors converting wind speed:")
            for err in errors:
                logging.warning("- %s", err)

        # get pressure
        errors = []
        error_num = 0
        for i in city.find_all('td', {"class": "msl"}):
            text = i.get_text()
            # text can return "*\n\t\t" before number
            try:
                text = int(text)
                item = str(text)
            except (ValueError, TypeError) as e:
                todelete = list(text)
                del todelete[:4]
                text = ''.join(todelete)
                error_num = error_num + 1
                errors.append(e)
                if len(errors) > 1:
                    if errors[len(errors)-1] == e:
                        errors.pop()

            if text == "":
                text = np.nan
                item = str(text)
            self.pressure_list.append(str(text))
        if error_num > 0:
            logging.warning("Errors converting pressure:")
            for err in errors:
                logging.warning("- %s", err)

        # store each row of data in dictionary
        for i in range(len(self.wind_speed_list)):
            local_database =  {
                "date": self.date_list[i],
                "temperature": self.temperature_list[i],
                "wind_direction": self.wind_direction_list[i],
                "wind_speed": self.wind_speed_list[i],
                "pressure": self.pressure_list[i]}
            # store individual dict(row) in table
            self.database.append(local_database)

        # clear table data
        self.date_list = []
        self.temperature_list = []
        self.wind_direction_list = []
        self.wind_speed_list = []
        self.pressure_list = []

        return self.database

