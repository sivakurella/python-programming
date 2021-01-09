import cProfile
import sqlite3
import threading
import sys

query = "SELECT DISTINCT teamID from Teams inner join TeamsFranchises on Teams.franchID == TeamsFranchises.franchID where TeamsFranchises.active = 'Y';"
conn = sqlite3.connect("lahman2015.sqlite", check_same_thread=False)
cur = conn.cursor()
teams = [row[0] for row in cur.execute(query).fetchall()]

query = "SELECT SUM(HR) FROM Batting WHERE teamId=?"

lock = threading.Lock()


def print_homeruns(team):
    cur = conn.cursor()
    query = "select sum(hr) from batting where teamID = ?;"
    
    cur.execute(query,(team,))
    home_runs = cur.fetchone()[0]
    
    lock.acquire()
    print(team,home_runs,sep=':')
    sys.stdout.flush()
    lock.release()
    return home_runs


for team in teams:
    thread = threading.Thread(target=print_homeruns, args=(team,))
    thread.start()
    thread.join()
    
