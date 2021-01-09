import threading
import sys

conn = sqlite3.connect("lahman2015.sqlite", check_same_thread=False)
best = {}
lock = threading.Lock()

def best_batter():
    cur = conn.cursor()
    query = '''select playerID, ((sum(H) + SUM(BB) + SUM(HBP))/(sum(AB) + sum(BB) + sum(HBP) + sum(cast(SF AS FLOAT))))  + 
                     ((sum(cast(H as float)) + sum("2B") + 2 * sum("3B") + 3 * sum(cast(HR as float)))/sum(AB))
    from Batting group by playerID  having sum(AB) > 100 ORDER BY 2 DESC limit 20;'''
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
    query = '''select playerID, ((13 * sum(cast(HR as float)) + 3 * SUM(BB) - 2 * SUM(SO))/sum(IPOUTS))  + 3.2
    from Pitching group by playerID  having sum(IPOUTS) > 100 ORDER BY 2 limit 20;'''
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
    query = '''select playerID, ((sum(cast(A as float)) + SUM(PO))/sum(G)) 
    from Fielding group by playerID  having sum(G) > 100 ORDER BY 2 DESC limit 20;'''
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
    
    


