# -*- coding: utf-8 -*-
"""
Author: Nejc Ropič
Python version: 3.9
Date: 10.5.2024
"""

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QThread, QTimer
import sys
import requests
import main_file
from gui_template import Ui_MainWindow


class FIRST_TEST(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(FIRST_TEST, self).__init__(parent)
        # izdelamo glavno okno
        self.ui = Ui_MainWindow()
        # naložimo UI
        self.ui.setupUi(self)
        # kličemo funkcijo za logične povezave v GUI
        self.setup_ui_logic()
        # odpremo okno v največji možni velikosti
        #self.showMaximized()

    def setup_ui_logic(self):
        ###???
        """Naredimo povezave z gumbi"""
        # Definiramo instance za vsako okno z nastavitvami posebej
        #self.gpd = gpd3303s.GPD3303S()



        # Definiramo glavno funkcijo
        self.main_func = main_file.Multi_test_main_func(self.ui)

        # ----------------------------------------------------------------------------#
        ###Povezava gumbov za test z UI

        # Vnos/Izbris podatkov za avtomatsko vnašanje parametrov
        self.ui.refreshButton.clicked.connect(self.refreshData)

        # ----------------------------------------------------------------------------#


    ###########################################################################################################
    # COM-PORT povezave
    ###???
    def refreshData(self):
        """Poveže/Odklopi GW_Instek"""
        self.main_func.refreshData(self.ui)





###########################################################################################################
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FIRST_TEST()
    window.setWindowTitle("RLS task app")
    window.show()
    sys.exit(app.exec_())