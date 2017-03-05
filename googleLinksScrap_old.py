
# To scrap links from google search 
# Google generates search database through web spidering, why can't we scrap google ?


import requests

vendors = {
	0 : 'www.amazon.in',
	1 : 'paytm.com',
	2 : 'www.flipkart.com',
	3 : 'www.snapdeal.com'
}

reqHeaders = {
	"user-agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
	"accept":"application/json",
	"accept-encoding":"gzip, deflate",
	"accept-language":"en-US,en;q=0.8",
};


def getVendor(url):
	return url.split('/')[2]

def getContent(page, key1, key2):
	a = page.index(key1)
	b = page.index(key2, a + len(key1)  )
	ret = page[a + len(key1) :b]
	return ret.lstrip()

def getContentAfter(page, after, key1, key2):
	try : 
		z = page.index(after)
	except ValueError:
		return ''
	a = page.index(key1, z + len(after))
	b = page.index(key2, a + len(key1)  )
	ret = page[a + len(key1) :b]
	return ret.lstrip()

def scrapVendor(url, vendorNumber):

	author 	= ''
	price	= 0
	imageLink = ''
	productDescription =''
	frequentlyBoTo = {}
	metaDescription = ''
	metaKeywords = ''

	# amazon
	if vendorNumber == 0 :
		# filter amazon unique product pages from amazon search results
		if (url.find('/dp/')== -1) :
			return ''

		# get the page
		page = requests.get(url, headers= reqHeaders)
		print url + '\n'

		#heading 
		heading = getContent(page.text, 'class="a-size-large">', '<')
		print heading + '\n'

		#price
		try:
			price = getContent(page.text,'<span class="currencyINR">&nbsp;&nbsp;</span>', '<')
		except ValueError:
			return 'product unavailable'
		print price + '\n'
		
		#image
		image = getContent(page.text, 'data-a-dynamic-image="{&quot;', '&quot;:')
		print image + '\n'

		#metadescription
		metaDescription = getContent(page.text, '<meta name="description" content="', '" />')
		metaDescription = metaDescription.replace('Amazon.in', 'MrBooksOnline.com')
		print metaDescription + '\n'

		#metaKeywords
		metaKeywords = getContent(page.text, '<meta name="keywords" content="' , '" />')
		print metaKeywords + '\n'

		#product description 
		if (page.text.find('Product Description') >0) :
			productDescription = getContentAfter(page.text, '<div id="productDescription" class="a-section a-spacing-small">', '<p>', '</p>')
			print productDescription

		
		print '------***end***------'

def getBookDetails(url):
	
	try :
		vendorNumber = vendors.values().index(getVendor(url))
	except ValueError :
		vendorNumber = -1

	if vendorNumber > -1 :

		rtn = getVendor(url) + ' ' + str(vendorNumber)
		return scrapVendor(url, vendorNumber)

	else :
		return 'unknown vendor'

	# now, we've found the vendor
	# going on with parsing code for each vendor separate. 






googleSearchQuery 	= 'physics for medical entrance amazon'
page 				= requests.get('https://www.google.co.in/search?q=' + googleSearchQuery)

links 	= page.text.split('<h3 class="r">') # first split to get the tiles 
links 	= links[2:] #not taking all the links

for link in links:
	chunks  = link.split(' ')
	shorts 	= chunks[1].split('&amp;')
	url		= shorts[0][13:]
	print '\n'
	if url[:4] == 'http': # print only if it is an http url 
		print getBookDetails(url)