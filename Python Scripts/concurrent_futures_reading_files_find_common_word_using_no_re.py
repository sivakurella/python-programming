import concurrent.futures
import os, time

pool = concurrent.futures.ProcessPoolExecutor(max_workers=1)
common_words={}

def find_most_common_word(filename):
    words = {}
    with open(filename, mode='r') as f:
        for line in f:
            tmp_words = line.split()
            for word in tmp_words:
                if word in words:
                    words[word] += 1
                else:
                    words[word] = 0
                    
    most_common_word = max(words.keys(), key = lambda k: words[k])
            
    return most_common_word

path = 'lines/'
filenames = os.listdir(path)

start_time = time.time()

words = list(map(lambda file: find_most_common_word(os.path.join(path,file)), filenames[:2]))


for i,word in enumerate(words):
    common_words[filenames[i]]= word
    
    
print(time.time() - start_time)