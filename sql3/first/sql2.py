import sqlite3
import time
import thread
import threading

lock = threading.Lock()

conn = sqlite3.connect('test.db', isolation_level="IMMEDIATE", timeout=60, check_same_thread=False)
c = conn.cursor()

# c.execute("create table firms (founded, hq, name, rev, size, type)")
# c.execute("insert into firms ( name ) values (?) ", ("bar", ))
# conn.commit()


def update_normal(information):
    updates = ", ".join(["`" + field + "`" + '=:' + field for field in information.keys() if field != 'name'])
    where = ' WHERE name == :name'
    values = information
    query = 'UPDATE firms SET ' + updates + where
    print query
    conn = sqlite3.connect('test.db', isolation_level="IMMEDIATE", timeout=60, check_same_thread=False)
    c = conn.cursor()
    print "exec"

    try:
        c.execute(query, values)
        time.sleep(3)

        # raise TypeError, "HEHE"
        conn.commit()
    except:
        conn.rollback()
        raise
    finally:
        conn.close()
    print "commit"


def update(information):
    # print information
    # for filed in information.keys():
    #     print filed
    # for key in information:
    #     print key
    updates = ", ".join(["`" + field + "`" + '=:' + field for field in information.keys() if field != 'name'])
    where = ' WHERE name == :name'
    values = information
    query = 'UPDATE firms SET ' + updates + where
    print query

    print "exec"

    try:
        lock.acquire(True)

        time.sleep(3)
        c.execute(query, values)
        # raise TypeError, "HEHE"
        conn.commit()
    except:
        conn.rollback()
        raise
    finally:

        lock.release()

    print "commit"


def update_f1(information):
    # print information
    # for filed in information.keys():
    #     print filed
    # for key in information:
    #     print key
    updates = ", ".join(["`" + field + "`" + '=:' + field for field in information.keys() if field != 'name'])
    where = ' WHERE name == :name'
    values = information
    query = 'UPDATE firms SET ' + updates + where
    print query

    print "exec"

    try:
        c.execute(query, values)
        time.sleep(3)
        # raise TypeError, "HEHE"
        conn.commit()
    except Exception, e:
        print e
    print "commit"


def update_f2(information):
    # print information
    # for filed in information.keys():
    #     print filed
    # for key in information:
    #     print key
    updates = ", ".join(["`" + field + "`" + '=:' + field for field in information.keys() if field != 'name'])
    where = ' WHERE name == :name'
    values = information
    query = 'UPDATE firms SET ' + updates + where
    print query

    print "exec"

    try:

        time.sleep(3)
        # raise TypeError, "HEHE"
        c.execute(query, values)
        conn.commit()
    except Exception, e:
        print e
    print "commit"


def update_f3(information):
    # print information
    # for filed in information.keys():
    #     print filed
    # for key in information:
    #     print key
    updates = ", ".join(["`" + field + "`" + '=:' + field for field in information.keys() if field != 'name'])
    where = ' WHERE name == :name'
    values = information
    query = 'UPDATE firms SET ' + updates + where
    print query

    print "exec"

    try:
        lock.acquire(True)
        c.execute(query, values)
        time.sleep(3)
        # raise TypeError, "HEHE"
        conn.commit()
    except:
        conn.rollback()
    finally:
        lock.release()
    print "commit"


for i in range(10):
    # thread.start_new_thread(update, (dict(name='bar', founded='1062', rev='7 MILLION DOLLARS!'), ))
    # thread.start_new_thread(update_f1, (dict(name='bar', founded='1062', rev='7 MILLION DOLLARS!'), ))
    # thread.start_new_thread(update_f2, (dict(name='bar', founded='1062', rev='7 MILLION DOLLARS!'), ))
    thread.start_new_thread(update_normal, (dict(name='bar', founded='1062', rev='7 MILLION DOLLARS!'), ))

update(dict(name='bar', founded='1062', rev='7 MILLION DOLLARS!'))
# update({})
print c.execute('select * from firms').fetchall()

conn.close()
time.sleep(1000)
