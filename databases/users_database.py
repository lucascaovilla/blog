import sqlite3
import hashlib


conn = sqlite3.connect('databases/data/usersdata.db', check_same_thread=False)
cur = conn.cursor()



def create_users_table():
    cur.execute("CREATE TABLE IF NOT EXISTS userdata (id INTEGER PRIMARY KEY, username VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL)")
    conn.commit()

def insert_user(username, password):
    password = hashlib.sha256(password.encode()).hexdigest()
    cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username, password))
    conn.commit()

def delete_user(username):
    cur.execute("DELETE FROM userdata WHERE username = '"+username+"'")
    conn.commit()

def handle_admin(username, password):
    cur.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (username, password))
    if cur.fetchall():
        #services
        #secrets
        return(True)
    else:
        return(False)
    