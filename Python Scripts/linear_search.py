def linear_search(array, search):
    i = 0
    indexes = []
    for item in array:
        if item == search:
            indexes.append(i)
        i += 1
    return indexes

sevens = linear_search(times, 7)
    