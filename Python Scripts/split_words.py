import re, time
word = 'siva   kurella! Hello word siva'

start_time = time.time()
for _ in range(1000):
    words = re.sub(' +',' ',word).split()
print(time.time() - start_time)


start_time = time.time()
for _ in range(1000):
    words = word.split()
print(time.time() - start_time)