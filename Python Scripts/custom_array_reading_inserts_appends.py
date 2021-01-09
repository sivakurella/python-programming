class Array():
    def __init__(self, size):
        self.array = np.zeros(size, dtype=np.float64)
        self.size = size
    
    def __getitem__(self, key):
        return self.array[key]
    
    def __setitem__(self, key, value):
        self.array[key] = value
        
    def __len__(self):
        return self.size
    
    def append(self, value):
        self.insert(self.__len__(), value)
        
    def insert(self, key, value):
        if key > self.__len__():
            print('Key: {} provided is outside the length of the array'.format(key)) 
            raise Exception('Key provided is outside the length of the array')
        else:
            new_length = self.__len__()+1
            new_array = np.zeros(new_length, dtype=np.float64)
            for i in range(new_length):
                if i < key:
                    new_array[i] = self.__getitem__(i)
                elif i == key:
                    new_array[i] = value
                else:
                    new_array[i] = self.__getitem__(i-1)
                    
            # lets swap the Array
            self.array = new_array
            
            # lets increase the size
            self.size = new_length
	
	def pop(self, key):
        if key >= self.__len__():
            print('Key: {} provided is outside the length of the array'.format(key)) 
            raise Exception('Key provided is outside the length of the array')
        else:
            new_length = self.__len__() - 1
            new_array = np.zeros(new_length, dtype=np.float64)
            for i in range(self.__len__()):
                if i < key:
                    new_array[i] = self.__getitem__(i)
                elif i == key:
                    removed = self.__getitem__(i)
                else:
                    new_array[i-1] = self.__getitem__(i)
                    
            # lets swap the Array
            self.array = new_array
            
            # lets increase the size
            self.size = new_length
            
            # return removed
            return removed
            

prices = Array(0)

with open('prices.csv', mode='r') as f:
    reader = csv.reader(f)
    header = next(reader)
    for _ in range(100):
        prices.append(float(next(reader)[1]))
                 
            
print(prices.size, prices.array)

prices.insert(50, 646.921081)
print(prices.size, prices.array)
