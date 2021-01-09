import linecache, csv, timeit

def brute_search():
    rows=[]
    i=1
    with open('amounts.csv') as f:
        for row in csv.reader(f):
            if i in (4, 41231, 284400):
                rows.append(row)
                
            i += 1
                
    return rows

def cache_search():
    rows=[]
    for line in (4, 41231, 284400):
        row = linecache.getline('amounts.csv',line)
        split_row = list(csv.reader([row]))
        rows.append(split_row[0])
    return rows

brute = brute_search()
cache = cache_search()

print(timeit.timeit('brute_search()','from __main__ import brute_search', number=50))
print(timeit.timeit('cache_search()','from __main__ import cache_search', number=50))

      