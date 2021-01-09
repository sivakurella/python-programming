import matplotlib.pyplot as plt

def selection_sort(array):
    counter = 0 
    for i in range(len(array)):
        lowest_index = i
        for z in range(i, len(array)):
            counter += 1
            if array[z] < array[lowest_index]:
                lowest_index = z
        swap(array, lowest_index, i)
        
    return counter

lengths = [10,100,1000,10000]
counters = []

for length  in lengths:
    first_amounts = amounts[:length]
    counters.append(selection_sort(first_amounts))
    
plt.plot(lengths, counters)