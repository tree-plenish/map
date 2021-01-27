import folium
from folium import *
import pandas as pd
import numpy as np
import json
import os

spreadsheetPath = '/Users/joyhe208/desktop/tree-plenish/demographics/stats.html'

demographics = pd.read_html(spreadsheetPath)[0]

#dataframe with just the states of each school
all_states = demographics.loc[:,['A', 'B']].drop([0],axis=0)

state_data = {}

#generating dictionary with state and number of schools in that state
for state in all_states.itertuples():
	if(state[2] in state_data.keys()):
		state_data[state[2]]['NumSchools'] = state_data[state[2]]['NumSchools']+1
		state_data[state[2]]['Schools'].append(state[1])
	else:
		state_data[state[2]]={'NumSchools': 1, 'Schools': []}
		state_data[state[2]]['Schools'].append(state[1])
#print(state_data)

frequencies = [state_data[state]['NumSchools'] for state in state_data.keys()]
firstQuart = np.percentile(frequencies, 25)
thirdQuart = np.percentile(frequencies, 75)

str1 = 'var firstQuartile = ' + str(firstQuart) + ';'
str2 = 'var thirdQuartile = ' + str(thirdQuart) + ';'

#adding the frequency variable from this 50 states json
with open('states.json', 'r') as f:
	states_geo = json.load(f)
	for state in states_geo['features']:
		if(state['properties']['NAME'] in state_data.keys()):
			state['properties']['NUMSCHOOLS'] = state_data[state['properties']['NAME']]['NumSchools']
			state['properties']['SCHOOLS'] = state_data[state['properties']['NAME']]['Schools']
		else:
			state['properties']['NUMSCHOOLS'] = 0
			state['properties']['SCHOOLS'] = []

with open('newStates.json', 'w') as f:
	f.write('var statesData = ')
	json.dump(states_geo, f, indent=4)
	f.write(';')
	f.write('\n')
	f.write(str1)
	f.write('\n')
	f.write(str2)

os.rename('newStates.json', 'states.js')






