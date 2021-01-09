def bubble_sort(array):
    swaps = 1
    length = len(array)
    while swaps > 0:
        swaps=0
        for i in range(length-1):
            if array[i+1] < array[i]:
                swap(array,i,i+1)
                swaps += 1
            
first_amounts = amounts[:10]
bubble_sort(first_amounts)
    