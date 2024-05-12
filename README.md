File for operating with program:

Program structure: 
- Top_level.py - Main file for connecting all GUI libraries and data processing files. Includes:
  - Functions for displaying data of individual GUI
  - 
- main_file.py - File for data processing
- manage_url.py - File to get important data from website before generating GUI
- config.py - File where you can change main link provided to Top_level.py
- pyqt_gui.py, tkinter_gui.py - GUI structure libraries files

Running program:
- Run file in Top_level.py
- Data for all cities will be listed in table
- Select city in ComboBox to display data from last 48 hours
- Refresh data by pressing on "Refresh button"

Testing program:
- In the end of the Top_level.py file, 
  you can choose between the GUI libraries, 
  if you are more familiar with them 
- If wanted, change GUI library in:
  - pyqt_gui.py for PyQt5 Library
  - tkinter_gui.py for Tkinter Library
  - pyside_gui.py for PySide Library (to be created..)
- At top of main_file.py, change logging level to 
  DEBUG instead of ERROR to track errors