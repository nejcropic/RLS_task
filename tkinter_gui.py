# -*- coding: utf-8 -*-
"""
Author: Nejc Ropič
Python version: 3.9
Date: 10.5.2024
"""

from tkinter import *
from tkinter.ttk import *
import manage_url


class TkinterMain:
    def __init__(self, root, url, domain):
        self.root = root
        self.url = url
        self.domain = domain

    def setupUi(self):
        self.root.geometry('1400x900')
        self.manage_url = manage_url.ManageUrl(self.url)

        # styles for elements
        style = Style()
        style.configure("RefreshButton.TButton", font=('calibri', 10, 'bold'))
        style.map('RefreshButton.TButton', foreground=[('active', '!disabled', 'black')],
                  background=[('active', 'black')])

        # frame for grid layout
        self.frame = Frame(self.root)
        self.frame.grid(row=0, column=0, sticky="nsew")

        # Canvas and scrollbar
        self.canvas = Canvas(self.frame)
        self.scrollbar = Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # frame for scrollable content
        self.contentFrame = Frame(self.canvas)
        self.contentFrame.bind("<Configure>", lambda e: self.updatescrollregion())

        # Combobox for data selection
        n = StringVar()
        self.comboBox = Combobox(self.contentFrame, width=30, textvariable=n)
        self.createcombobox()

        # Refresh Button
        self.refresh_button = Button(self.contentFrame, text="Refresh", style="RefreshButton.TButton")
        self.refresh_button.grid(column=3, row=1)  # Placing the button below the comb

        # resizing configuration
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)

        # pack widgets in window
        self.canvas.create_window((0, 0), window=self.contentFrame, anchor="nw")
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")

    # functions for gui elements
    def createcombobox(self):
        cities = self.manage_url.listcities()
        self.comboBox.configure(values=cities)
        self.comboBox.grid(column=1, row=1, pady=25)
        self.comboBox.current(1)

    def updatescrollregion(self):
        """ Function for updating scroll region everytime content is changed """
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
