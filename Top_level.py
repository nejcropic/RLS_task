# -*- coding: utf-8 -*-
"""
Author: Nejc Ropič
Python version: 3.9
Date: 10.5.2024
"""

from PyQt5 import QtWidgets
import sys
import config
import main_file
import manage_url
from gui_template import Ui_MainWindow


class TopLeveL(QtWidgets.QMainWindow):
    def __init__(self, ui, url, domain, parent=None):
        super(TopLeveL, self).__init__(parent)
        # make instance for main window
        self.ui = ui
        self.url = url
        self.domain = domain
        # load UI
        self.ui.setupUi(self)
        # call functions for connections with GUI
        self.setup_ui_logic()
        # open window in max size - uncomment if wanted
        # self.showMaximized()
        # show data on start
        self.showdata()
        # adjust width
        self.ui.cityesTable.setColumnWidth(0, 300)
        self.ui.cityesTable.setColumnWidth(1, 150)
        self.ui.cityesTable.setColumnWidth(2, 200)
        self.ui.cityesTable.setColumnWidth(3, 200)

    def setup_ui_logic(self):
        self.manage_url = manage_url.ManageUrl(self.ui, self.url)
        # find available cities and list them in combo box
        self.manage_url.listcities()
        # define instances
        urls = self.manage_url.urlsetup()
        # define main function
        self.main_func = main_file.MainFileDataProcess(self.ui, urls, self.domain)

        # ------------ Povezava gumbov z UI---------------------------------#
        # city select
        self.ui.citiesComboBox.currentIndexChanged.connect(self.showdata)
        # data refresh
        self.ui.refreshButton.clicked.connect(self.refreshdata)
        # ----------------------------------------------------------------------------#

    def showdata(self):
        """Show data when element in QComboBox is selected"""
        self.main_func.showdata()

    def refreshdata(self):
        """Function for data refresh"""
        self.main_func.refreshdata()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_ui = Ui_MainWindow()
    main_url = config.get_main_url()
    main_domain = config.get_domain()
    window = TopLeveL(main_ui, main_url, main_domain)
    window.setWindowTitle("RLS task app")
    window.show()
    sys.exit(app.exec_())