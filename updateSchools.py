import pandas as pd
import numpy as np
import json
import os
from ../tech-team-database/libOverview.py import tplib

#initialize tplib object (idk how to self initialize hmm):
tpl = tplib.tplib()

schoolNames = #table of school names?

allSchoolData = {}
#loop through schools:
for school in schoolNames:
    tableName = "[" + school + "] Tree Request Form"
    dataWanted = [] #list of column names
    df = tpl.getTable(tableName, dataWanted)

    #add df to big dictionary:
    allSchoolData[school] = df

#dump into json
fileName = "./static/allSchoolData.json"
with open(fileName, "w") as f:
    json.dump(schoolData,f,indent=4)