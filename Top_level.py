from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import sys
import config
import main_file
import manage_url
import tkinter as tk
from pyqt_gui import Ui_MainWindow
from tkinter_gui import TkinterMain


class GuiInterface:
    def create_main_window(self):
        raise NotImplementedError

    def set_title(self, title):
        raise NotImplementedError

    def start(self):
        raise NotImplementedError


class PyQt5Gui(GuiInterface):
    def __init__(self, url, domain):
        # make instance for main window
        self.url = url
        self.domain = domain
        # main functions
        self.app = QtWidgets.QApplication(sys.argv)
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        # load UI
        self.ui.setupUi(self.main_window)
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
        self.manage_url = manage_url.ManageUrl(self.url)
        # find available cities and list them in combo box
        self.listcities()
        # define instances
        urls = self.manage_url.urlsetup()
        # define main function
        self.main_func = main_file.MainFileDataProcess(self.ui, urls, self.domain)

        # ------------ Connect GUI Elements with functions ---------------------------------#
        # city select
        self.ui.citiesComboBox.currentIndexChanged.connect(self.showdata)
        # data refresh
        self.ui.refreshButton.clicked.connect(self.showdata)
        # ----------------------------------------------------------------------------#

    def listcities(self):
        """List all cities in QComboBox on startup"""
        rows = self.manage_url.listcities()
        for i in rows:
            self.ui.citiesComboBox.addItem(i)

    def showdata(self):
        """Show data when element in QComboBox is selected"""
        index = self.ui.citiesComboBox.currentIndex()
        data = self.main_func.getdata(index)
        city = self.main_func.selectcity(index)

        # display city name in header
        self.ui.cityesTable.horizontalHeaderItem(0).setText(city.find('th', {"class": "meteoSI-header"}).get_text())

        # show data in table
        row = 0
        self.ui.cityesTable.setRowCount(len(data))
        for i in data:
            self.ui.cityesTable.setItem(row, 0, QTableWidgetItem(i["date"]))
            self.ui.cityesTable.setItem(row, 1, QTableWidgetItem(i["temperature"]))
            self.ui.cityesTable.setItem(row, 2, QTableWidgetItem(i["wind_speed"]))
            self.ui.cityesTable.setItem(row, 3, QTableWidgetItem(i["pressure"]))
            row = row + 1


    # functions for displaying gui
    def create_main_window(self):
        return self.main_window

    def set_title(self, title):
        self.main_window.setWindowTitle(title)

    def start(self):
        self.main_window.show()
        sys.exit(self.app.exec_())


# TkinterGUI
class TkinterGui(GuiInterface):
    def __init__(self, url, domain):
        # make instance for main window
        self.url = url
        self.domain = domain
        # main functions
        self.root = tk.Tk()
        self.ui = TkinterMain(self.root, self.url, self.domain)
        self.ui.setupUi()
        self.manage_url = manage_url.ManageUrl(self.url)
        self.table_widgets = []
        # functions
        urls = self.manage_url.urlsetup()
        self.index = 0
        self.main_func = main_file.MainFileDataProcess(self.index, urls, self.domain)
        self.createtable()
        # events
        self.updatecombobox()
        self.updatetable(self.index)
        self.ui.refresh_button.config(command=self.refreshdata)
        self.onmousewheel()

    def updatetable(self, index):
        data = self.main_func.getdata(index)
        # delete previous data
        for widget in self.table_widgets:
            widget.destroy()
        self.table_widgets.clear()
        # display data in the table
        for i, item in enumerate(data, start=4):
            # date
            label_date = tk.Label(self.ui.contentFrame, text=item['date'],
                                  width=30, fg='black', font=('Arial', 10))
            label_date.grid(row=i, column=0)
            self.table_widgets.append(label_date)
            # temperature
            label_temp = tk.Label(self.ui.contentFrame, text=item['temperature'],
                                  width=15, fg='black', font=('Arial', 10))
            label_temp.grid(row=i, column=1)
            self.table_widgets.append(label_temp)
            # wind speed
            label_wind = tk.Label(self.ui.contentFrame, text=item['wind_speed'],
                                  width=20, fg='black', font=('Arial', 10))
            label_wind.grid(row=i, column=2)
            self.table_widgets.append(label_wind)
            # pressure
            label_pressure = tk.Label(self.ui.contentFrame, text=item['pressure'],
                                   width=20, fg='black', font=('Arial', 10))
            label_pressure.grid(row=i, column=3)
            self.table_widgets.append(label_pressure)

    def updatecombobox(self):
        cities = self.manage_url.listcities()

        # the function to get triggered each time you choose something
        def select(event):
            for i in range(0, len(cities)):
                if self.ui.comboBox.get() == cities[i]:
                    self.index = i

            self.updatetable(self.index)
            self.createtable()

        self.ui.comboBox.bind('<<ComboboxSelected>>', select)

    def onmousewheel(self):
        # mousewheel events
        def _on_mousewheel(event):
            self.ui.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        self.ui.canvas.bind_all("<MouseWheel>", _on_mousewheel)

    def createtable(self):
        citydata = self.main_func.selectcity(self.index)
        thead = citydata.find('thead')
        trow = thead.find('tr')
        row_table = []
        # get headers in table
        for i in trow:
            row_table.append(i.get_text())
        headers = [row_table[1], row_table[3], row_table[5], row_table[7]]
        # apply headers in tkinter label
        for column, header in enumerate(headers):
            if column == 0:
                label = tk.Label(self.ui.contentFrame, text=header, width=30,
                                 font=('Arial', 16, 'bold'), fg='black')
            elif column == 1:
                label = tk.Label(self.ui.contentFrame, text=header, width=15,
                                 font=('Arial', 16, 'bold'), fg='black')
            else:
                label = tk.Label(self.ui.contentFrame, text=header, width=20,
                                 font=('Arial', 16, 'bold'), fg='black')
            label.grid(row=3, column=column)

    def refreshdata(self):
        self.main_func.getdata(self.index)

    def create_main_window(self):
        return self.root

    def set_title(self, title):
        self.root.title(title)

    def start(self):
        self.root.mainloop()


class Application:
    def __init__(self, gui):
        self.gui = gui
        self.main_window = self.gui.create_main_window()

    def run(self):
        self.gui.set_title("RLS task")
        self.gui.start()


if __name__ == "__main__":
    # dependencies
    main_url = config.get_main_url()
    main_domain = config.get_domain()
    # Choose the GUI library here, PyQt5Gui() for PyQt5 or TkinterGui() for Tkinter
    gui = TkinterGui(main_url, main_domain)  # Change this to TkinterGui() to switch the GUI framework
    app = Application(gui)
    app.run()
