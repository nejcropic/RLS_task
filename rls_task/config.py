# -*- coding: utf-8 -*-
"""
Author: Nejc Ropič
Python version: 3.9
Date: 10.5.2024
"""

# Choose which GUI is implemented:
# "pyqt" for PyQt5 or "tkinter" for Tkinter
GUI = "pyqt"
# Choose logging level: debug, warning, info, error, critical
LEVEL = "error"

# Service URL
SERVICE_URL = 'https://meteo.arso.gov.si/met/en/service2/'
# Main URL
MAIN_URL = 'https://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/en/observation_si/index.html'
# Domain from website URL where database is stored - link is selected in main_file.py/selectcity()
DOMAIN_URL = 'https://meteo.arso.gov.si/'


def get_service_url():
    return SERVICE_URL


def get_main_url():
    return MAIN_URL


def get_domain():
    return DOMAIN_URL


def get_gui():
    return GUI


def get_logging_level():
    return LEVEL
