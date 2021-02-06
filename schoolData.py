import pandas as pd
import numpy as np
import json
import os

path = "/Users/joyhe208/desktop/tree-plenish/UpdatedTreeRequests/School List.html"
df = pd.read_html(path)[0]
schools = {}
for school in df.itertuples():
    name = str(school[2])
    if(name!='nan' and name!='School Name'):
        schools[name.strip()] = {'Tree Requests': school[3], 'Tree Goal': school[4], 'Tree Progress': school[5]}

with open('schoolData.json', 'w') as f:
    json.dump(schools, f, indent=4)