import math

def swap(array, pos1, pos2):
    store = array[pos1]
    array[pos1] = array[pos2]
    array[pos2] = store

def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            swap(array, j, j-1)
            j-=1

def binary_search(array, search):
    # initialize
    i,m,z = 0, 0, len(array)-1
    
    # sort you array
    insertion_sort(array)
    
    while i <= z:
        m = math.floor( ((z-i)/2) + i)
        value = array[m]
        if value == search:
            return m
        elif value < search:
            i = m+1
        else:
            z = m-1
            
result = binary_search(times, 56)
        
    