#JSONparser.py
import json
from pprint import pprint 


jsonfile = 'atom.json'

def parseJSON(f):
	with open(f) as data_file:
		return json.load(data_file)


if __name__ == '__main__':
	jsondata = parseJSON(jsonfile)

	#pprint (jsondata)

	startlink = jsondata['target']
	searchLink = jsondata['searchQuery']
	searchSeed = jsondata['searchSeed']

	tasksnum =  (len(jsondata['do']))	

	'''
	do each task in 'do'

	'''

	for currentTask in range(tasksnum):
		doRepeated = jsondata['do'][currentTask]['repeated']
		if len(jsondata['do'][currentTask]['thenDo']) > 0:
			isThereASubTask = True
		else:
			isThereASubTask = False

	