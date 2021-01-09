import threading
import sys

conn = sqlite3.connect("lahman2015.sqlite", check_same_thread=False)
best = {}
lock = threading.Lock()

def best_batter():
    cur = conn.cursor()
    query = '''select playerID, ((H + BB + HBP)/(AB + BB + HBP + cast(SF AS FLOAT)) )  + 
                     ((cast(H as float) + "2B" + 2 * ("3B") + 3 * (cast(HR as float)))/(AB))
    from Batting group by playerID  having (AB) > 100 ORDER BY 2 DESC limit 20;'''
    cur.execute(query)
    rows =  cur.fetchall()
    players = [row[0] for row in rows]
    
    with lock:
        print(rows)
        print('Finished up best batters')
        sys.stdout.flush()
    
    best['batter'] = players

def best_pitcher():
    cur = conn.cursor()
    query = '''select playerID, ((13 * (cast(HR as float)) + 3 * (BB) - 2 * (SO))/(IPOUTS))  + 3.2
    from Pitching group by playerID  having (IPOUTS) > 100 ORDER BY 2 limit 20;'''
    cur.execute(query)
    rows =  cur.fetchall()
    players = [row[0] for row in rows]
    
    with lock:
        print(rows)
        print('Finished up best pitchers')
        sys.stdout.flush()
        
    best['pitcher'] = players

def best_fielder():
    cur = conn.cursor()
    query = '''select playerID, (((cast(A as float)) + (PO))/(G)) 
    from Fielding group by playerID  having (G) > 100 ORDER BY 2 DESC limit 20;'''
    cur.execute(query)
    rows =  cur.fetchall()
    players = [row[0] for row in rows]
    
    with lock:
        print(rows)
        print('Finished up best fielders')
        sys.stdout.flush()
    
    best['fielder'] = players

fs = [best_batter, best_pitcher, best_fielder]
threads = []

for func in fs:
    thread = threading.Thread(target=func)
    thread.start()
    
    threads.append(thread)
    
for thread in threads:
    thread.join()
    
print(best)
    
    


