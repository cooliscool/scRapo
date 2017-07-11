#JSONparser.py v0.2
import json
import requests
from scrapfunctions import *

jsonfile = 'atom2.json'

def parseJSON(f):
	with open(f) as data_file:
		return json.load(data_file)


if __name__ == '__main__':

	# Parse JSON and assign variables

	jsondata = parseJSON(jsonfile)


	# parse the root link and jobs . This is considered as a unique case right now .

	isSearch = int (jsondata['search'])
	targetRoot = jsondata['targetRoot']

	if isSearch :
		searchLink = jsondata['searchQuery'] + jsondata['searchSeed']
		rootPage = requests.get(searchLink, headers = reqHeaders).text

	else :
		rootPage = requests.get(targetRoot, headers = reqHeaders).text

	# Start the while loop from parsing jobs

	while True:

		jobs = jsondata['do']

		
