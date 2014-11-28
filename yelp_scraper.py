#given a yelp web page url as a command line argument, this script extracts soem useful information from the Yelp web page
#and stores it in a dictionary

import re 
from urllib import request
import sys 

if len(sys.argv) < 2:
	print("Error: no website given")
	
else:
	results = {}
	
	yelp_url = sys.argv[1] #the regexes will act on the web page source code
	r = request.urlopen(yelp_url) #first we obtain the source code for the web page
	bytecode = r.read()
	htmlstr = bytecode.decode() #source code for the Yelp page
	
	restauraunt_name = re.search('itemprop="name">\s*([^<]+\w)\s*<', htmlstr) #the \w removes trailing whitespace
	restauraunt_name = restauraunt_name.group(1)
	results['Name'] = restauraunt_name
	
	address = re.search('\<address\>\s*((\d+)([\w\s\.]+),([\w\s\.]+),\s(\w{2})\s(\d{5}))\s*<', htmlstr)
	full_address = address.group(1)
	results['Address'] = full_address
	
	yelp_rating = re.search('\["attrrating", "([\d\.]+)"\]', htmlstr)
	yelp_rating  = yelp_rating.group(1)
	results['Yelp rating'] = yelp_rating
	
	print(results)
	
	
	
	
	
	