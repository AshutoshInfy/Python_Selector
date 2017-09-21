#Python Selector Program BETA
#Created by Lewis Watson (aka Wo)

def createlist():
	user_list = []
	print("")
	loops = int(input("How many items do you wish to select from? "));
	print("")

	if loops <1:
		print("Please select a valid number of list items.")
		createlist();

	else:
		while loops != 0:
			loops = loops - 1;
			user_input = input("Select Item: ");
			user_list = user_list + [user_input];

		print("You have selected " + str(len(user_list)) + " items.")
		print("");
		selector(user_list);

def selector(user_list):
	print(user_list)
	print("END OF PROGRAM")


  

createlist();