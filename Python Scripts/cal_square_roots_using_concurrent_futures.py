import concurrent.futures
nums = [1,10,20,50]

pool = concurrent.futures.ProcessPoolExecutor(max_workers=5)
roots = list(pool.map(lambda x: math.sqrt(x), nums))

print(roots)