import sqlite3

conn = sqlite3.connect('databases/data/usersdata.db', check_same_thread=False)
cur = conn.cursor()

def create_users_table():
    cur.execute("""CREATE TABLE IF NOT EXISTS userdata (id INTEGER PRIMARY KEY, username VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, privilege INTEGER NOT NULL)""")
    conn.commit()

def delete_user(username):
    cur.execute("DELETE FROM userdata WHERE username = ?", (username))
    conn.commit()

def handle_user(username, password):
    cur.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (username, password))
    if cur.fetchall():
        #services
        #secrets
        return(True)
    else:
        return(False)
    
def insert_user(username, email, password):
    if not cur.execute("SELECT * FROM userdata WHERE username = ?", (username,)).fetchall():
        cur.execute("INSERT INTO userdata (username, email, password, privilege) VALUES (?, ?, ?, ?)", (username, email, password, 0))
        conn.commit()
        return handle_user(username, password)