f = open('random_integers.txt', 'r')
random_integers = [int(line) for line in f.readlines()]

import math

def merge(left_list, right_list):
	sorted=[]
	
	while left_list and right_list:
		if left_list[0] < right_list[0]:
			sorted.append(left_list.poo(0))
		else:
			sorted.append(right_list.pop(0))
	
	sorted += left_list
	sorted += right_list
	
	return sorted

def merge_sort(unsorted):
    # Implement the recursion logic here.
    # You can use the `merge` function described in the example from
    # Part 1.
    length = len(unsorted)
    midpoint = math.ceil(length/2)
    if length == 1:
        return unsorted

    sorted = merge(merge_sort(unsorted[:midpoint]), merge_sort(unsorted[midpoint:]))
    return sorted

random_sorted = merge_sort(random_integers)