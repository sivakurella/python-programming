def binary_search(array, search):
    array.sort()
    m = 0
    i = 0
    z = len(array) - 1
    while i<= z:
        m = math.floor(i + ((z - i) / 2))
        if array[m] == search:
            return m
        elif array[m] < search:
            i = m + 1
        elif array[m] > search:
            z = m - 1
    return m

def fuzzy_match(array, lower, upper, m):
    j, l, matches = m , m+1, []
    while j > 0:
        value = array[j]
        if lower <= value <= upper:
            matches.append(value)
            
        j -= 1
        
    while l < len(array):
        value = array[l]
        if lower <= value <= upper:
            matches.append(value)
            
        l += 1
        
    return matches

m = binary_search(amounts, 150)
matches = fuzzy_match(amounts, 100, 2000, m)

print(matches[:10])