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

	# if isSearch == 1 :
	# 	searchLink = jsondata['searchQuery'] + jsondata['searchSeed']
	# 	rootPage = requests.get(searchLink, headers = reqHeaders).text
	#
	# else :
	# 	rootPage = requests.get(targetRoot, headers = reqHeaders).text

	# Start the while loop from parsing jobs

	while True:

		jobs = jsondata['do']

		if len(jobs) > 0 :
			for job in jobs:

				# Get the requirements and type of job

				doRepeatedly = int(job['repeated'])
				isThereASubtask = int(job['isThereASubtask'])
				wannaSave = int(job['saveThis'])
				name = job['name']

				# TODO : say what is page

				#
				# Parsing the data, whatever it is .
				#

				tup = (page,)
				for q in job['afterSequence'] :
					tup = tup + (q,)
				tup += ( job['bet'] , job['ween'], )

				off = 0
				ln = len(page)

				dat = []

					# Scrap !

				while off < ln:
					try :
						val, off = getContent(tup, offset= off)
						dat.append(val)
						if doRepeatedly == 0:
							break
					except ValueError:
						break

				print (dat) # Log scraped things4

				# If there is a subtask for the corresponding scrap,
				# add each link and its job to queue.
				#

				if isThereASubtask == 1 :
					# TODO: define a queue and level too

					for link in dat :
						queue.append( {level, link , job['do']})

				#
				# Save or not , depending on wannaSave
				#

				if wannaSave == 1:

					# TODO : define a dictionary of all scrap data

					for d in dat :
						dictionary.add({ ,name , d})
