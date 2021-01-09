import numpy as np
import csv

class Array():
    def __init__(self, size):
        self.array = np.zeros(size, dtype=np.float64)
        self.size = size
    
    def __getitem__(self, key):
        return self.array[key]
    
    def __setitem__(self,key,value):
        self.array[key] = value

prices= Array(10)
with open('prices.csv', mode='r') as f:
    reader = csv.reader(f)
    header = next(reader)
    for _ in range(10):
        prices[_] = float(next(reader)[1])
        
        
prices[0]