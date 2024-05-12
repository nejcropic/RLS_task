# -*- coding: utf-8 -*-
"""
Author: Nejc Ropič
Python version: 3.9
Date: 10.5.2024
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup


class ManageUrl:
    def __init__(self, url):
        self.url = url

    def listcities(self):
        """Function to get all cities available and store them in QCombobox"""
        page = urlopen(self.url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        rows = soup.find_all('tr')
        cities = []
        for row in rows:
            col = row.find('td')
            if col is None:
                continue
            cities.append(col.get_text())
        return cities

    def urlsetup(self):
        """Function to get all cities available"""
        # get city data
        page = urlopen(self.url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        url_list = []
        for i in soup.find_all('a', href=True):
            if i['href'][-12:] == "history.html" or i['href'][-11:] == "latest.html":
                url_list.append(i['href'])
        return url_list
