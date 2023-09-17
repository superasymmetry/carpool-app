import sqlite3
from pathlib import Path
from flask import Flask, request, render_template

# Create empty database
# Path("database.db").touch()

def store_login_data(uname, psword, fname, lname, eml, res, tel=None):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS database (username STRING PRIMARY KEY, password TEXT, fname TEXT, lname TEXT, telephone TEXT, email TEXT, residence TEXT, dates INTEGER);")
    c.execute("INSERT INTO database (username, password, fname, lname, telephone, email, residence) VALUES (?, ?, ?, ?, ?, ?, ?)", (uname, psword, fname, lname, tel, eml, res))
    conn.commit()
    conn.close()

    return uname

def validate_credentials(uname, psword):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM database WHERE username=?;", [uname])
        usr = c.fetchone()
        print(usr)
        if usr[1]==psword:
            conn.close()
            return True
    except:
        conn.close()
        return False
    
def store_personal_details(fname, lname, telephone, email, residence):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    date = []
    c.execute("INSERT INTO database (fname, lname, telephone, email, residence, dates) VALUES (?,?,?,?,?,?)", (fname, lname, telephone, email, residence, date))

    conn.commit()
    conn.close()

def store_date(date, user):
    user='test'
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM database WHERE username=?;", [user])
    row = c.fetchone()
    date_list=row[7]
    try:
        date_list.append(date)
    # means that there is no list in the cell
    except AttributeError:
        date_list=[date]
    update_query = "UPDATE database SET dates=? WHERE username=?;"
    c.execute(update_query, (date_list, user))
    conn.commit()
    conn.close()