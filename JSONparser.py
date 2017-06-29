#JSONparser.py
import json
import requests
from pprint import pprint 
from scrapfunctions import *

jsonfile = 'atom.json'

def parseJSON(f):
	with open(f) as data_file:
		return json.load(data_file)


if __name__ == '__main__':

	# Parse JSON and assign variables

	jsondata = parseJSON(jsonfile)
	#pprint (jsondata)
	startlink = jsondata['target']
	searchLink = jsondata['searchQuery']
	searchSeed = jsondata['searchSeed']
	tasksnum =  (len(jsondata['do']))

	

	'''
	do each task in 'do'

	'''

	scrapedData = {}

	for currentTask in range(tasksnum):
		jsonDo = jsondata['do'][currentTask]
		link = searchLink + searchSeed
		linkfeed = [link]
		while True:			
			taskDoRepeated =  (jsonDo['repeated'])
			taskName = jsonDo['name']
			taskIsThereASubTask =  (jsonDo['isThereASubtask'])

			print taskIsThereASubTask

			for sublink in linkfeed :

				# if the link is not complete
				if sublink[0:4]!= 'http':
					sublink = startlink + sublink
				page = requests.get( sublink , headers = reqHeaders).text

				
				# Prepare tuple input for getContent function

				tup = (page,)
				for q in jsonDo['afterSequence'] : 
					tup = tup + (q,)
				tup += ( jsonDo['bet'] , jsonDo['ween'], )

				off = 0
				ln = len(page)

				dat = []

				# Scrap ! 

				while off < ln:
					try :
						val, off = getContent(tup, offset= off)
						dat.append(val)
					except ValueError:
						break

				scrapedData.update({sublink : dat})
				
			print scrapedData

			if taskIsThereASubTask == "True":
				jsonDo = jsonDo['thenDo']
				linkfeed = dat
				scrapedData = {}
				continue
			else:
				break

		
		# if taskDoRepeated:
		# 	length = len(page)


		
