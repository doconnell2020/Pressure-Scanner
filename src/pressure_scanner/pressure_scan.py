"""This program finds the Start and Stop presssure and date and time of a run on Agilent Chemstation.
It then plots the data to give insight into the long term performance of the machine."""

import os
import re
from datetime import datetime
from dateutil.parser import parse
# import matplotlib.pyplot as plt
import plotly.graph_objects as go


chosen_month = input("Please enter the month you wish to search in the format YYYY-MM:")

print("Searching " +str(chosen_month)+'\n'
      "Please wait")

Date = []
start_p = []
stop_p = []

start_finder = re.compile(r'"Start Pressure",\d\d\d\.?\d*')
stop_finder = re.compile(r'"Stop Pressure",\d\d\d\.?\d*')
just_pressure = re.compile(r"\d\d\d\.?\d*")
get_Date = re.compile(r"\d\d-\w\w\w-\d\d, \d\d:\d\d:\d\d")

for folderName, subfolders, filenames in os.walk(
    r"C:\Users\Public\Documents\ChemStation\1\Data\\" +str(chosen_month)
):  # Searches drive in walk function.
    for filename in filenames:
        if filename == "Report00.CSV":  # Report file which contains pressures
            with open(
                str(folderName + "\\" + filename), encoding="utf-16-le"
            ) as f:  # encoding type is necessary
                start_result = start_finder.search(f.read())
                start_p.append(float(just_pressure.search(start_result[0])[0]))

                f.seek(0)
                stop_result = stop_finder.search(f.read())
                stop_p.append(float(just_pressure.search(stop_result[0])[0]))
                # Date finder
                # finds date of folder name
                f.seek(0)
                d_result = get_Date.search(f.read())
                Date.append(parse(d_result.group()))


Date, start_p, stop_p = zip(*sorted(zip(Date, start_p, stop_p)))

Start_Date = Date[0].strftime("%Y/%b/%d")
End_Date = Date[-1].strftime("%Y/%b/%d")




fig = go.Figure()

# Add traces
fig.add_trace(go.Scatter(x=Date, y=start_p,
                    mode='lines+markers',
                    name='Initial Pressure'), )
fig.add_trace(go.Scatter(x=Date, y=stop_p,
                    mode='lines+markers',
                    name='Final Pressure'))
fig.update_layout(hovermode="x unified")
fig.update_layout(title="LCMS-4 " + Start_Date + " to " + End_Date)
fig.update_xaxes(title_text= 'Date')
fig.update_yaxes(title_text= 'Pressure (bar)')
fig.show()
