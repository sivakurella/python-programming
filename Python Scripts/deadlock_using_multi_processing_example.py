import multiprocessing

db_lock = multiprocessing.Lock()
stdout_lock = multiprocessing.Lock()

def write_to_database(data, db_lock, stdout_lock):
    stdout_lock.acquire()
    print("Writing {} lines of data to the database.".format(len(data)))
    db_lock.acquire()
    db_write(data)
    db_lock.release()
    stdout_lock.release()


def read_from_database(db_lock, stdout_lock):
    db_lock.acquire()
    data = db_read()

    stdout_lock.acquire()
    print("Read {} lines of data from the database.".format(len(data)))
    stdout_lock.release()
    db_lock.release()

p1 = multiprocessing.Process(target=read_from_database, args=(db_lock, stdout_lock))
p2 = multiprocessing.Process(target=write_to_database, args=(data, db_lock, stdout_lock))


p1.start()
p2.start()