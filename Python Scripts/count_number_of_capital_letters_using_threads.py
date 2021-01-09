import threading

capital_letters1 = []
capital_letters2 = []

def calc_calpital_letters(start, finish, capital_letters):
    for text in emails['RawText'].iloc[start:finish]:
        capital_letters.append(len([char for char in text if char.isupper()]))
        
start_time = time.time()
t1 = threading.Thread(target=calc_calpital_letters, args=(0,3972,capital_letters1))
t1.start()
t2 = threading.Thread(target=calc_calpital_letters, args=(3972,7946,capital_letters2))
t2.start()
t1.join()
t2.join()
total = time.time() - start_time

print(total)
