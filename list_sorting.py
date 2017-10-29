# sorting the list
def sort_list(sam_list):
	# sort the list
	sam_list.sort()
	return sam_list

# print new sorted list
new_list = [1,2,8,9,4,3,2]
sorted_list = sort_list(new_list)
print('Sorted list:', sorted_list)