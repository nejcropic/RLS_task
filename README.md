RLS_task is a Python GUI program which collects 
and displays the environment  data  from: 
https://meteo.arso.gov.si/met/en/service2/.

Running program:
- Run file in Top_level.py
- Data for all cities will be listed in table
- Select city in ComboBox to display data from last 48 hours
- Refresh data by pressing on "Refresh button"

Program structure: 
- Top_level.py - Main file for connecting all GUI libraries and data processing files. Includes:
  - Functions for displaying data of individual GUI
  - Some functions for processing
- main_file.py - File for main data processing
- manage_url.py - File to get important data from website before generating GUI
- config.py - File where you can change main link provided to Top_level.py
- pyqt_gui.py, tkinter_gui.py - GUI structure libraries files
- if wanted, change GUI library in:
  - pyqt_gui.py for PyQt5 Library
  - tkinter_gui.py for Tkinter Library

Testing program:
- In config.py file: choose GUI library, logging level for tracking errors and link
