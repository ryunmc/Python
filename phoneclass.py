#phonebook will consist of people (which will be a class itself)
phonebook = []

class people():
	def __init__(self,name,phone_number,address):
		people.name=name #all of these parameters are strings
		people.phone_number=phone_number
		people.address=address
		
Ryan = people("Ryan","0831696511","6 Tirol Close")

phonebook.append(Ryan)

print( phonebook[0].phone_number) 