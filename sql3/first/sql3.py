import sqlite3
import time

conn = sqlite3.connect('test.db', isolation_level="IMMEDIATE", timeout=60, check_same_thread=False)
c = conn.cursor()

# c.execute("create table firms (founded, hq, name, rev, size, type)")
# c.execute("insert into firms ( name ) values (?) ", ("bar", ))
# conn.commit()

print c.execute('select * from firms').fetchall()


def update(information):
    print information
    for filed in information.keys():
        print filed
    for key in information:
        print key
    updates = ", ".join(["`" + field + "`" + '=:' + field for field in information.keys() if field != 'name'])
    where = ' WHERE name == :name'
    values = information
    query = 'UPDATE firms SET ' + updates + where
    print query
    c.execute(query, values)
    print "exec"
    time.sleep(2)
    conn.commit()
    print "commit"


update(dict(name='bar', founded='1062', rev='4 MILLION DOLLARS!'))

print c.execute('select * from firms').fetchall()
