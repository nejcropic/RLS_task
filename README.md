RLS_task is a Python GUI program which collects 
and displays the environment  data  from: 
https://meteo.arso.gov.si/met/en/service2/.

Running program:
- Run following commands in terminal in following order to run program and install all dependencies:
  - python -m venv venv (if you dont have virtual environment previously installed)
  - venv\Scripts\activate
  - pip install git+https://github.com/nejcropic/RLS_task.git
  - (if you already installed program but code is changed later, run this command) pip install --upgrade --force-reinstall git+https://github.com/nejcropic/RLS_task.git
  - rls_task

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
