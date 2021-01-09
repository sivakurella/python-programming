def insertion_sort(array):
    counter = 0
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            counter += 1
            swap(array, j, j-1)
            j-=1
    return counter

def binary_search(array, search):
    counter = insertion_sort(array)
    m = 0
    i = 0
    z = len(array) - 1
    while i<= z:
        counter += 1
        m = math.floor(i + ((z - i) / 2))
        if array[m] == search:
            return m
        elif array[m] < search:
            i = m + 1
        elif array[m] > search:
            z = m - 1
    return counter

lengths = [10,100,1000,10000]

counters = []
for i in lengths:
     # We sort in reverse order so we get the worst case performance of the insertion sort.
    first_amounts = sorted(amounts[:i], reverse=True)
    counter = binary_search(first_amounts, -1)
    counters.append(counter)

plt.plot(lengths, counters)