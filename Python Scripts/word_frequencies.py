import concurrent.futures
import os,re,collections

def word_frequencies(filename):
    regex = re.compile('[^a-zA-Z_0-9]+')
    with open(filename) as f:
        data = f.read().lower()
    
    words = regex.sub(' ', data).split()
    words = [word for word in words if len(word) >= 5]
    word_count = collections.Counter(words)

    return word_count


results = []
pool = concurrent.futures.ProcessPoolExecutor(max_workers=5)
filenames = ["lines/{}".format(f) for f in os.listdir("lines")]
word_counts = pool.map(word_frequencies, filenames)
word_counts = list(word_counts)

total_word_counts = collections.Counter()
for word_count in word_counts:
    total_word_counts += word_count
    
top_200 = total_word_counts.most_common(200)

