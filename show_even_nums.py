"""list of integers, some even some odd
write a function that returns indexes of all the integers that are even

i : [1,2,3,4,6,8]
o : [1, 3, 4, 5]



 def function(lst):

"""

def show_even_nums(list):
	even_list = []
	for i in range(len(list)):
		if list[i] % 2 == 0:
			even_list.append(i)
	return even_list

print show_even_nums([1,2,3,4,6,8])

print show_even_nums([1,2,3,4,6,8,8,6])

print show_even_nums([])