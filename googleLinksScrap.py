
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

'''
# TODO : combine all three types of getContent functions

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

def getContentAfterAfter(page, after, after2, key1, key2):
	try : 
		z = page.index(after)
		y = page.index(after2, z + len(after))
		a = page.index(key1, y + len(after2))
		b = page.index(key2, a + len(key1)  )
		ret = page[a + len(key1) :b]
		return ret.lstrip()
	except ValueError:
		return ''
'''
def getContent(*args, **kwargs):
	# documentation :
	# args is a tuple of params
	# args[1] : source content
	# last two params should be the strings , in between whom the target data is present
	# everything in between args[1] and last two params will be the content preceding the 
	# 	target in the same order

	# you can set a start offset for defining from where to start the search in source.
	# now the function returns location where target is found along with the target.
	# offset should be specified as 'offset=<integer>'
	# return value is (target_string, location_in_source)
	w = 0
	z = 0
	n = len(args)
	
	if kwargs.iteritems() >0 :
		for k,w in kwargs.iteritems():
			if (k == 'offset') & (type(w) == int):
				z_o = w
			else:
				print 'offset didn\'t work'
	

	for i in range (1,n):
		try :
			z_o = z 
			z = args[0].index(args[i], z_o + w)
			w = len(args[i])
		except ValueError:
			return ''

	return ( args[0][ (z_o + len(args[n-2]) ) : z].lstrip() , z_o )

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
		heading = getContent(page.text, 'class="a-size-large">', '<')[0]
		print heading + '\n'

		#price
		try:
			price = getContent(page.text,'<span class="currencyINR">&nbsp;&nbsp;</span>', '<')[0]
		except ValueError:
			return 'product unavailable'
		print price + '\n'
		
		#image
		image = getContent(page.text, 'data-a-dynamic-image="{&quot;', '&quot;:')[0]
		print image + '\n'

		#metadescription
		metaDescription = getContent(page.text, '<meta name="description" content="', '" />')[0]
		metaDescription = metaDescription.replace('Amazon.in', 'MrBooksOnline.com')
		print metaDescription + '\n'

		#metaKeywords
		metaKeywords = getContent(page.text, '<meta name="keywords" content="' , '" />')[0]
		print metaKeywords + '\n'

		#product description 
		if (page.text.find('Product Description') >0) :
			productDescription = getContent(page.text, '<div id="productDescription" class="a-section a-spacing-small">', '<p>', '</p>')[0]
			print productDescription

		#author
		author = getContent(page.text, '<span class="author', '<a class', '>', '<' )[0]
		print author

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
links 	= links[2:3] #not taking all the links

for link in links:
	chunks  = link.split(' ')
	shorts 	= chunks[1].split('&amp;')
	url		= shorts[0][13:]
	print '\n'
	if url[:4] == 'http': # print only if it is an http url 

		print getBookDetails(url)
