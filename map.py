import folium
from folium import *
import pandas as pd
import numpy as np
import json
import os

spreadsheetPath = '/Users/joyhe208/desktop/tree-plenish/demographics/stats.html'

demographics = pd.read_html(spreadsheetPath)[0]

#dataframe with just the states of each school
all_states = demographics.loc[:,'B'].drop([0],axis=0)

state_frequency = {}

#generating dictionary with state and number of schools in that state
for state in all_states:
	if(state in state_frequency.keys()):
		state_frequency[state] = state_frequency[state]+1
	else:
		state_frequency[state] = 1

#adding the frequency variable from this 50 states json
with open('states.json', 'r') as f:
	states_geo = json.load(f)
	for state in states_geo['features']:
		if(state['properties']['NAME'] in state_frequency.keys()):
			state['properties']['NUMSCHOOLS'] = state_frequency[state['properties']['NAME']]

with open('newStates.json', 'w') as f:
	json.dump(states_geo, f, indent=4)

os.remove('states.json')
os.rename('newStates.json', 'states.json')




