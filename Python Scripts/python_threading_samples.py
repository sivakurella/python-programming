import threading
import time
import sys

lock = threading.Lock()

def task(team):
    lock.acquire()
    print(team)
    sys.stdout.flush()
    lock.release()
    
for i in range(10):
    indices = range(i*5, (i+1)*5)
    temp_teams = [teams[i] for i in indices]
    print(temp_teams)
    threads = []
    
    for team in temp_teams:
        thread = threading.Thread(target=task, args=(team,))
        thread.start()
        threads.append(thread)
        
    for thread in threads:
        thread.join()
        
    print('Finished batch {}'.format(i))
    
 