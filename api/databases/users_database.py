import sqlite3

conn = sqlite3.connect('api/databases/data/usersdata.db', check_same_thread=False)
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS userdata 
            (id INTEGER PRIMARY KEY, 
            username VARCHAR(255) NOT NULL, 
            password VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL)""") 

def delete_user(username):
    if cur.execute("SELECT * FROM userdata WHERE username = ?", (username,)).fetchall():
        cur.execute("DELETE FROM userdata WHERE username = ?", (username))
        conn.commit()

def handle_user(username, password):
    cur.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (username, password))
    if cur.fetchall():
        return(True)
    else:
        return(False)
    
def insert_user(username, password, email):
    if not cur.execute("SELECT * FROM userdata WHERE username = ?", (username,)).fetchall():
        cur.execute("INSERT INTO userdata (username, password, email) VALUES (?, ?, ?)", (username, password, email))
        conn.commit()
        return handle_user(username, password)

conn.commit()