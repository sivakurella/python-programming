from multiprocessing import Pool
import time

# create a pool for 2 workers
p = Pool(2)

def calc_capital_letters(text):
    return len([c for c in text if c.isupper()])

start_time = time.time()

capital_letters = p.map(calc_capital_letters,['Siva','Kurella'])

total = time.time() - start_time

print(total)