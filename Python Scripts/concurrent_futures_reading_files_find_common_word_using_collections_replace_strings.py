import concurrent.futures
import os,re

def most_common_word(filename):
    regex = re.compile('[^a-zA-Z_0-9]+')
    with open(filename) as f:
        words = f.read().split(" ")
    words = [regex.sub('',word.lower()) for word in words if len(word) >= 5]
    count = Counter(words)

    return count.most_common()[0][0]


results = []
pool = concurrent.futures.ProcessPoolExecutor(max_workers=5)
filenames = ["lines/{}".format(f) for f in os.listdir("lines")]
words = pool.map(most_common_word, filenames)
words = list(words)

common_words = {}
for i in range(len(lengths)):
    common_words[filenames[i].replace("lines/", "")] = words[i]