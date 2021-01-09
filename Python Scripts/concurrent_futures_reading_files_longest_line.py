import concurrent.futures
import os, time

pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)
movie_lengths={}

def find_longest_line(filename):
    max_line_length = 0
    max_line = ''
    with open(filename, mode='r') as f:
        for line in f:
            tmp_len = len(line)
            if tmp_len > max_line_length:
                max_line_length = tmp_len
                max_line = line
            
    return max_line, max_line_length

path = 'lines/'
filenames = os.listdir(path)

start_time = time.time()

lengths = list(pool.map(lambda file: find_longest_line(os.path.join(path,file)), filenames))


for i,length in enumerate(lengths):
    movie_lengths[filenames[i]]= length
    
longest_line_movie = max(movie_lengths.keys(), key = lambda k : movie_lengths[k][1])
longest_line = movie_lengths[longest_line_movie][0]

print('Longest line "{movie}" : "{lines}"'.format(movie=longest_line_movie, lines=longest_line))

print(time.time() - start_time)