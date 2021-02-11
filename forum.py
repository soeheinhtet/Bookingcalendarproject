import sqlite3 as sql
from os import path

ROOT= path.dirname(path.relpath(__file__))

def create_forum(fname,lname,phonenum,email,dd):
    con=sql.connect(path.join(ROOT,'database.db'))
    cur=con.cursor()
    print ('First Name=' + fname)
    print('Last Name=' + lname)
    print('Phone Number=' + phonenum)
    print('E-mail=' + email)
    print('Date=' + dd)
    cur.execute('insert into forum(fname,lname,phonenum,email,dd) values(?,?,?,?,?)',(fname,lname,phonenum,email,dd))
    con.commit()
    con.close()

def get_reservedList(date):
    con=sql.connect(path.join(ROOT,'database.db'))
    cur=con.cursor()
    date_query = '"' + str(date) +'"'
    cur.execute('select fname, lname from forum where dd=' + date_query )
    reserved_list=cur.fetchall()
    return reserved_list

def get_allreserved(date):
    con=sql.connect(path.join(ROOT,'database.db'))
    cur=con.cursor()
    cur.execute('select * from forum')
    all_reservedlist=cur.fetchall()
    return all_reservedlist

