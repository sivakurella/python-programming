import sqlite3

memory = sqlite3.connect(':memory:') # create a memory database
disk = sqlite3.connect('lahman2015.sqlite')

dump = "".join([line for line in disk.iterdump() if "Batting" in line])
memory.executescript(dump)

cur = memory.cursor()

query = "SELECT DISTINCT teamID from Teams inner join TeamsFranchises on Teams.franchID == TeamsFranchises.franchID where TeamsFranchises.active = 'Y';"

teams = [row[0] for row in cur.execute(query).fetchall()]

def calculate_runs(teams):
    home_runs =[]
    query = "select sum(hr) from batting where teamID = ?;"
    for team in teams:
        cur.execute(query,(team,))
        home_runs.append(cur.fetchone()[0])
    return home_runs

cProfile.run('home_runs = calculate_runs(teams)')