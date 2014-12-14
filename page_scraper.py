#opens a text file (first argument) and implements the regexes found in the text file on a given URL
#(second argument)

import re 
from urllib import request
import sys 

if len(sys.argv) < 3:
	print("Error: not enough arguments given")
	
else:
	filename = sys.argv[1]
	url = sys.argv[2]
	
	r = request.urlopen(url) #first we obtain the source code for the web page
	bytecode = r.read()
	htmlstr = bytecode.decode() #source code for the page
	
	results_file = open("results.txt","w") #this is where we'll write the stuff captured by the regexes

	with open(filename,"r") as read_file:
		for regex in read_file:
			regex = regex.strip('\n')
			result = re.search(regex,htmlstr)
			results_file.write( result.group(1) + '\n' )
			
	results_file.close()
	
			
			
			
			