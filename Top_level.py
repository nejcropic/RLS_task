# -*- coding: utf-8 -*-
"""
Author: Nejc Ropič
Python version: 3.9
Date: 10.5.2024
"""

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QThread
from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys
import requests
import main_file
from gui_template import Ui_MainWindow


class FIRST_TEST(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(FIRST_TEST, self).__init__(parent)
        self.url = 'https://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/en/observation_si/index.html'
        # izdelamo glavno okno
        self.ui = Ui_MainWindow()
        # naložimo UI
        self.ui.setupUi(self)
        # kličemo funkcijo za logične povezave v GUI
        self.setup_ui_logic()
        # odpremo okno v največji možni velikosti
        # self.showMaximized()
        # show data on start
        self.showdata()
    def setup_ui_logic(self):
        # Definiramo instance
        urls = self.urlsetup()
        # Definiramo glavno funkcijo
        self.main_func = main_file.Multi_test_main_func(self.ui, urls)

        # ------------ Povezava gumbov z UI---------------------------------#
        # City Select
        self.ui.citiesComboBox.currentIndexChanged.connect(self.showdata)
        # Data Refresh
        self.ui.refreshButton.clicked.connect(self.refreshdata)
        # ----------------------------------------------------------------------------#

    def urlsetup(self):
        page = urlopen(self.url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        url_list = []
        for i in soup.find_all('a', href=True):
            if i['href'][-12:] == "history.html":
                url_list.append(i['href'])

        return url_list



    ###########################################################################################################
    # COM-PORT povezave
    def showdata(self):
        """Poveže/Odklopi GW_Instek"""
        self.main_func.showdata()

    def refreshdata(self):
        """Poveže/Odklopi GW_Instek"""
        self.main_func.refreshdata()





###########################################################################################################
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FIRST_TEST()
    window.setWindowTitle("RLS task app")
    window.show()
    sys.exit(app.exec_())