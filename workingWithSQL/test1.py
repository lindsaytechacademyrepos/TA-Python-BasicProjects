import sqlite3

"""
connect to database
"""

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor();
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT, \
        col_lname TEXT, \
        col_email TEXT \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_persons(col_fname,col_lname,col_email) VALUES (?,?,?)", \
                ("Bob","Smith","bsmith@gmail.com"))
    cur.execute("INSERT INTO tbl_persons(col_fname,col_lname,col_email) VALUES (?,?,?)", \
                ("Lindsay","Alexander","linmalex@gmail.com"))
    cur.execute("INSERT INTO tbl_persons(col_fname,col_lname,col_email) VALUES (?,?,?)", \
                ("Ammon","Ford","ammonford@gmail.com"))
    cur.execute("INSERT INTO tbl_persons(col_fname,col_lname,col_email) VALUES (?,?,?)", \
                ("Stephanie","Cole","srcole@gmail.com"))
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname, col_lname, col_email FROM tbl_persons WHERE col_fname = 'Lindsay'")
    varPerson = cur.fetchall()
    for item in varPerson:
        msg="First name: {}\nLast name: {}\nEmail: {}".format(item[0],item[1],item[2])
    print(msg)
    #gotta close DB Browser before it will let you run it
    

