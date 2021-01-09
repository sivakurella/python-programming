search_list = ['apple', 'orange', 'pear', 'fig', 'passionfruit']

def search(strings, term, index=0):
    if strings[0] == term:
        return index
    elif len(strings) <= 1:
        return -1
    index += 1
    return search(strings[1:], term, index)
        
apple_index = search(search_list, 'apple')
pear_index = search(search_list, 'pear')
foo_index = search(search_list, 'foo')
        