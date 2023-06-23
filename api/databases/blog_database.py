import sqlite3
from sqlite3 import Error


conn = sqlite3.connect('api/databases/data/blog.db', check_same_thread=False)
cur = conn.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS posts 
            (ident INTEGER PRIMARY KEY, 
            creator VARCHAR(255) NOT NULL, 
            datetime DATETIME NOT NULL, 
            id VARCHAR(255) NOT NULL, 
            title VARCHAR(255) NOT NULL, 
            text VARCHAR(255) NOT NULL)""")

cur.execute("""CREATE TABLE IF NOT EXISTS projects 
            (id INTEGER PRIMARY KEY, 
            title VARCHAR(255), 
            description VARCHAR(255), 
            link VARCHAR(255))""")

def insert_post(post):
  if not cur.execute("SELECT * FROM posts WHERE title = ?", (post[3],)).fetchall():
    cur.execute("""INSERT INTO posts (creator, datetime, id, title, text) VALUES (?, ?, ?, ?, ?)""", (post[0], post[1], post[2], post[3], post[4]))
    conn.commit()
    return True
  else:
    return False

def select_post(post_id):
    post_data = cur.execute("SELECT * FROM posts WHERE id = (?)", (post_id,)).fetchall()[0]
    print("\n")
    print(post_data)
    print("\n")
    print(cur.execute("SELECT * FROM posts WHERE id = (?)", (post_id,)).fetchall())
    print("\n")
    post = {'ident': post_data[0], 'creator': post_data[1], 'datetime': post_data[2], 'id': post_data[3], 'title': post_data[4], 'text': post_data[5]}
    return post

def delete_post(title):
  if cur.execute("SELECT * FROM posts WHERE title = ?", (title,)).fetchall():
    try:
        cur.execute("DELETE FROM posts WHERE title = ?", (title,))
        conn.commit()

    except sqlite3.Error as error:
        print("Error deleting post:", error)
        
def sel_all_posts():
    list_posts = cur.execute("SELECT * FROM posts").fetchall()
    posts = []
    for post in list_posts:
      dict = {'ident': post[0], 'creator': post[1], 'datetime': post[2], 'id': post[3], 'title': post[4], 'text': post[5]}
      posts.append(dict)
    return posts


def insert_project(project):
  if not cur.execute("SELECT * FROM projects WHERE title = ?", (project[0],)).fetchall():
    cur.execute("INSERT INTO projects (title, description, link) VALUES (?, ?, ?)", (project[0], project[1], project[2]))
    conn.commit()
    return True
  else:
    return False

def select_project(project_id):
    project_data = cur.execute("SELECT * FROM projects WHERE id = (?)", (project_id,)).fetchall()[0]
    project = {'ident': project_data[0], 'title': project_data[1], 'description': project_data[2], 'link': project_data[3]}
    return project

def delete_project(title):
  try:
      cur.execute("DELETE from projects WHERE title = ?", (title,))
      conn.commit()
  except sqlite3.Error as error:
      print("Error deleting project:", error)

def sel_all_projects():
    list_projects = cur.execute("SELECT * FROM projects").fetchall()
    projects = []
    for project in list_projects:
      dict = {'id': project[0], 'title': project[1], 'description': project[2], 'link': project[3]}
      projects.append(dict)
    return projects


conn.commit()