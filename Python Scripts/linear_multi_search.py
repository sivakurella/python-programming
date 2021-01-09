def linear_multi_search(array, search):
    indexes = []
    length = len(array[0])
    print(length)
    for i in range(length):
        if array[0][i] == search[0] and array[1][i] == search[1]:
            indexes.append(i)
            
    return indexes

transactions = [times, amounts]
results = linear_multi_search(transactions,[56,10.84])
#(transactions[0][284806], transactions[1][284806])
    