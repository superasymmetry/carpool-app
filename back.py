import psycopg2


def get_connection():
    try:
        return psycopg2.connect(
            database="database_vp6i",
            user="database_vp6i_user",
            password="X7BRPVOM0nXf8UUU2NkbkSG3rZT1DWdd",
            host="dpg-cjsn84m3m8ac73e3eb5g-a",
            port=5432,
        )
    except:
        return False
    

def store_login_data(uname, psword, fname, lname, eml, res, tel=None):
    conn = get_connection()
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS database (username STRING PRIMARY KEY, password TEXT, fname TEXT, lname TEXT, telephone TEXT, email TEXT, residence TEXT, dates INTEGER);")
    c.execute("INSERT INTO database (username, password, fname, lname, telephone, email, residence) VALUES (?, ?, ?, ?, ?, ?, ?)", (uname, psword, fname, lname, tel, eml, res))
    conn.commit()
    conn.close()

    return uname

def validate_credentials(uname, psword):
    conn = get_connection()
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
    conn = get_connection()
    c = conn.cursor()
    date = []
    c.execute("INSERT INTO database (fname, lname, telephone, email, residence, dates) VALUES (?,?,?,?,?,?)", (fname, lname, telephone, email, residence, date))

    conn.commit()
    conn.close()

def store_date(date, user):
    # user='test'
    conn = get_connection()
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