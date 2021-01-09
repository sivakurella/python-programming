import os
quotes = {}

files = os.listdir('lines/')

for file in files:
    if file.replace('.txt','') == '':
        print(file)
    with open('lines/'+file, mode='r') as f:
        data = f.read()
        
    quotes[file.replace('.txt','')] = data
    
