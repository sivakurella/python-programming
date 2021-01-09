import concurrent.futures
import os, time, collections

#pool = concurrent.futures.ProcessPoolExecutor(max_workers=1)
common_words={}

def find_most_common_word(filename):
    with open(filename, mode='r') as f:
        tmp_words = f.read().split()
        c = collections.Counter(tmp_words)
                    
    most_common_word = c.most_common(1)[0][0]
            
    return most_common_word

path = 'lines/'
filenames = os.listdir(path)

start_time = time.time()

words = list(map(lambda file: find_most_common_word(os.path.join(path,file)), filenames[:2]))


for i,word in enumerate(words):
    common_words[filenames[i]]= word
    
    
print(time.time() - start_time)