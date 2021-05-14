Agilent HPLC/LCMS Pressure Scanner
======

File system walker which reads specific files (named Report00.CSV) containing the start and end pressure of a HPLC or LCMS run on the Agilent Chemstation software.

Installation
------------

Download the pressure_scanner.py file 
Ensure the appropriate libraries are installed as seen in the import statements:
os
re
datetime
pip install python-dateutil plotly

Quickstart Guide
----------------

Locate the PATH to your own data folders and edit the source code as required.

Note: The output settings in the Report setting of any and all Methods on your Chemstation Software must be set to generate .CSV files to work properly.
This is what the scanner is looking for. Ensure this setting is set up appropriately before using the program.

Contribute
----------
I would like to see this developed further to monitor standard injections using similar report files and pro-actively detect degradation in these standard injections. 
This could be achieved by monitoring the height, width, slope and retention time of these standrd injections and determining if they are moving to OOS criteria. 

If you'd like to contribute to Agilent HPLC/LCMS Pressure Scanner, check out https://github.com/doconnell2020/pressure_scanner
