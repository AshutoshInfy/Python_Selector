def create_list():    #  defines the create_list function
	
	#  1. takes a string input of items to add to the list, e.g.: "1,2,3,4,5"
	#  2. then splits the string at the character ',' turning it into a list
	#  3. finally returns the list to the user
	
	return input("Enter list items, seperated by a ','\n > ").split(",")
	
if __name__ == "__main__":    #  when the program is run
	new_list = create_list()    #  create a new list
	print(new_list)    #  print the newly created list
	
