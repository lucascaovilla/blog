import sqlite3
import hashlib



conn = sqlite3.connect('databases/databases/usersdata.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS userdata (id INTEGER PRIMARY KEY, username VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL)")



username1, password1 = "mike123", hashlib.sha256("mikepassword".encode()).hexdigest()
username2, password2 = "john123", hashlib.sha256("johnpassword".encode()).hexdigest()
username3, password3 = "peter123", hashlib.sha256("peterpassword".encode()).hexdigest()
username4, password4 = "tony123", hashlib.sha256("tonypassword".encode()).hexdigest()

# cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
# cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
# cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
# cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))

conn.commit()


def handle_admin(username, password):
    conn = sqlite3.connect("databases/databases/usersdata.db")
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (username, password))
    
    if cur.fetchall():
        #services
        #secrets
        return("Login successfull!".encode())
    else:
        return("Login failed!".encode())