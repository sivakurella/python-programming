import concurrent.futures
import os, time

pool = concurrent.futures.ThreadPoolExecutor(max_workers=1)
movie_lengths={}

def calc_num_rows(filename):
    line_nums = 0
    with open(filename, mode='r') as f:
        for line in f:
            line_nums += 1
            
    return line_nums

path = 'lines/'
filenames = os.listdir(path)

start_time = time.time()

lengths = list(pool.map(lambda file: calc_num_rows(os.path.join(path,file)), filenames))


for i,length in enumerate(lengths):
    movie_lengths[filenames[i]]= length
    
most_lines_tuple = sorted(movie_lengths.items(), key = lambda x: x[1], reverse=True)[0]
most_lines =most_lines_tuple[0]

print('Most lines "{movie}" : {lines}'.format(movie=most_lines_tuple[0], lines=most_lines_tuple[1]))

print(time.time() - start_time)