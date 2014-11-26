#searches through a text file with entries of the form name, phone number, address
#each line represent one person, uses regex to extract data

import re #regexp
import sys #for command line arguments

if len(sys.argv) < 2 :
	print("Error, no file given")

else:	
	filename = sys.argv[1] #the first argument is actually address_book.py
	
	names=[]
	phone_numbers=[]
	address=[]
	
	with open(filename, "r") as textfile:
	
		for line in textfile:
			match = re.search('^([^\d]+)\s(\d+)\s([\w\s,]+)$', line) #this regex captures all three properties
			names.append( match.group(1) )
			phone_numbers.append( match.group(2) )
			address.append( match.group(3))
			
	print( names )
	print( phone_numbers )
	print( address )
			
			
			
			