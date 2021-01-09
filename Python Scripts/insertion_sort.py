def insertion_sort(array):
    length = len(array)
    for i in range(length):
        j=i
        while j > 0 and array[j-1] > array[j]:
            swap(array,j-1,j)
            j -= 1
            
first_amounts = amounts[:10]
insertion_sort(first_amounts)