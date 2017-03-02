# To scrap links from google search 
# Google generates search database through web spidering, why can't we scrap google ?

import requests

googleSearchQuery 	= 'moochingal'
page 				= requests.get('https://www.google.co.in/search?q=' + googleSearchQuery)

links 	= page.text.split('<h3 class="r">') # first split to get the tiles 
links 	= links[1:10] #not taking all the links

for link in links:
	chunks = link.split(' ')
	shorts 	= chunks[1].split('&amp;')
	url		= shorts[0][13:]
	if url[:4] == 'http': # print only if it is an http url 
		print url + '\n'	