import numpy as np

def simple_hash(key):
    key = str(key)
    code = ord(key[0])
    return code % 20

class HashTable():
    
    def __init__(self, size):
        self.array = np.zeros(size, dtype=np.object)
        self.size = size
    
    def __getitem__(self, key):
        ind = simple_hash(key)
        for k,v in self.array[ind]:
            if key == k:
                return v
    
    def __setitem__(self, key, value):
        ind = simple_hash(key)
        replace = True
        if not isinstance(self.array[ind], list):
            self.array[ind] = []
            replace = None
            
        if not replace:
            self.array[ind].append((key,value))
        else:
            for p,(k,v) in enumerate(self.array[ind]):
                if key == k:
                    self.array[ind][p] = (key,value)
        
hash_table = HashTable(20)

file_names = ['xmen','xmenoriginswolverine']

for file in file_names:
    with open('lines/' + file + '.txt', mode='r') as f:
        hash_table[file] = f.read()
        
        
hash_table['xmen']