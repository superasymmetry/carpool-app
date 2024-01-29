import psycopg2


def get_connection():
    try:
        conn = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="Ab200708",
            host="localhost",
            port=5432,
        )
    except:
        return False
    

def store_login_data(uname, psword, fname, lname, eml, res, tel=None):
    conn = psycopg2.connect(database="postgres",user="postgres",password="Ab200708",host="localhost",port=5432,)
    c = conn.cursor()
    # c.execute("CREATE TABLE IF NOT EXISTS database (username STRING PRIMARY KEY, password TEXT, fname TEXT, lname TEXT, telephone TEXT, email TEXT, residence TEXT, dates INTEGER);")
    c.execute("INSERT INTO carpool (username, psword, fname, lname, telephone, email, residence) VALUES (%s, %s, %s, %s, %s, %s, %s)",
          (uname, psword, fname, lname, tel, eml, res))
    conn.commit()
    conn.close()

    return uname

def validate_credentials(uname, psword):
    conn = psycopg2.connect(database="postgres",user="postgres",password="Ab200708",host="localhost",port=5432,)
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM carpool WHERE username= ANY(%s)", [[uname]])
        usr = c.fetchone()
        print(usr)
        if usr[1]==psword:
            conn.close()
            return True
    except:
        conn.close()
        return False
    
def store_personal_details(fname, lname, telephone, email, residence):
    conn = psycopg2.connect(database="postgres",user="postgres",password="Ab200708",host="localhost",port=5432,)
    c = conn.cursor()
    date = []
    # c.execute("INSERT INTO carpool1 (fname, lname, telephone, email, residence, dates) VALUES (?,?,?,?,?,?)", (fname, lname, telephone, email, residence, date))
    c.execute("INSERT INTO carpool (fname, lname, telephone, email, residence, dates) VALUES (%s, %s, %s, %s, %s, %s)",
          (fname, lname, telephone, email, residence, date))

    conn.commit()
    conn.close()

def store_date(date, user):
    # user='test'
    conn = psycopg2.connect(database="postgres",user="postgres",password="Ab200708",host="localhost",port=5432,)
    c = conn.cursor()
    c.execute("SELECT * FROM carpool WHERE username=ANY(%s);", [[user]])
    row = c.fetchone()
    a=row[0]
    print(a)
    # try:
    #     c.execute("UPDATE carpool1 SET dates=%s WHERE user=%s",[date,a])
    # # means that there is no value in the cell
    # except AttributeError:
    #     return False
    update_query = "UPDATE carpool SET dates=%s WHERE username=%s"
    c.execute(update_query, (date, user))
    conn.commit()
    conn.close()

    return True
