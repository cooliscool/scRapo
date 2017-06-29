import requests


reqHeaders = {
	"user-agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
	"accept":"application/json",
	"accept-encoding":"gzip, deflate",
	"accept-language":"en-US,en;q=0.8",
};


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
	args = args[0]
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



