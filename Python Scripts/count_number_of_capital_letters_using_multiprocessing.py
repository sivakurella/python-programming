import multiprocessing

def count_capital_letters(email):
    return len([letter for letter in email if letter.isupper()])

def count_capitals_in_emails(start, finish, conn):
    capital_letters=[]
    for email in emails["RawText"][start:finish]:
        capital_letters.append(count_capital_letters(email))
    
    # send the capital_letters back to parent_conn
    conn.send(capital_letters)
    
    # close the connection
    conn.close()

start = time.time()

pc1, cc1 = multiprocessing.Pipe()
pc2, cc2 = multiprocessing.Pipe()

p1 = multiprocessing.Process(target=count_capitals_in_emails, args=(0, 3972, cc1))
p2 = multiprocessing.Process(target=count_capitals_in_emails, args=(3972, 7946, cc2))
p1.start()
p2.start()

capital_letters1 = pc1.recv()
capital_letters2 = pc2.recv()

for process in [p1, p2]:
    process.join()
    
total = time.time() - start

print(total)