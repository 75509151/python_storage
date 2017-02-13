import sqlite3
import time


def add_company(c, name, age=20, addr="", salary=10000000):

    sql = "INSERT INTO COMPANY (NAME, AGE, ADDRESS, SALARY) \
            VALUES (?, ?, ?, ?);"
    try:
        c.execute(sql, (name, age, addr, salary))
        # c.commit()
    except Exception as e:
        print e
        # raise e


conn = sqlite3.connect('test.db', isolation_level="IMMEDIATE", timeout=60, check_same_thread=False)
cursor = conn.cursor()

try:
    # conn.execute('''CREATE TABLE COMPANY
    #    (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    #    NAME           TEXT    NOT NULL,
    #    AGE            INT     NOT NULL,
    #    ADDRESS        CHAR(50),
    #    SALARY         REAL);''')
    # print "Table created successfully"

    # conn.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) \
    #       VALUES ( 'Paul', 32, 'California', 20000.00 )")

    # conn.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) \
    #       VALUES ( 'Allen', 25, 'Texas', 15000.00 )")

    # conn.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) \
    #       VALUES ( 'Teddy', 23, 'Norway', 20000.00 )")

    # add_company(conn, "jay")
    add_company(conn, "jay2", age="sdgsgf")
    conn.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) \
          VALUES ('fsdfsdfsdf', 25, 'Rich-Mond ', 65000.00 )")
    # conn.commit()
    print "insert success"
    rs = conn.execute("SELECT * FROM COMPANY").fetchall()
    for r in rs:
        print r
except Exception as e:
    print e
    raise e

while True:
    time.sleep(1)
