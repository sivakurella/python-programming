import threading
import time
import statistics

def read_emails():
    with open('Emails.csv', mode='r') as f:
        for line in f:
            pass

times=[]
for _ in range(100):
    start_time = time.time()
    read_emails()
    times.append(time.time() - start_time)
    
print(statistics.median(times))

threaded_times=[]
for _ in range(100):
    start_time = time.time()
    t1 = threading.Thread(target=read_emails)
    t1.start()
    t2 = threading.Thread(target=read_emails)
    t2.start()
    t1.join()
    t2.join()
    threaded_times.append(time.time() - start_time)
    
print(statistics.median(threaded_times))