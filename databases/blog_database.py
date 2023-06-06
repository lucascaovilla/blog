import sqlite3
from sqlite3 import Error

conn = sqlite3.connect('databases/data/blog.db', check_same_thread=False)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY, title VARCHAR(255), text VARCHAR(255), creator VARCHAR(255))")
cur.execute("CREATE TABLE IF NOT EXISTS projects (id INTEGER PRIMARY KEY, title VARCHAR(255), description VARCHAR(255), link VARCHAR(255))")
  
def insert_post(post):
  if not cur.execute("SELECT * FROM posts WHERE title = ?", (post[0],)).fetchall():
    cur.execute("INSERT INTO posts (title, text, creator) VALUES (?, ?, ?)", (post[0], post[1], post[2]))
    conn.commit()
    return True
  else:
    return False

def insert_project(project):
  if not cur.execute("SELECT * FROM projects WHERE title = ?", (project[0],)).fetchall():
    cur.execute("INSERT INTO projects (title, description, link) VALUES (?, ?, ?)", (project[0], project[1], project[2]))
    conn.commit()
    return True
  else:
    return False

def delete_post(title):
  if not cur.execute("SELECT * FROM posts WHERE title = ?", (title,)).fetchall():
    try:
        cur.execute("DELETE from posts WHERE title = ?", (title,))
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print("Error deleting post:", error)

def delete_project(title):
  try:
      cur.execute("DELETE from projects WHERE title = ?", (title,))
      conn.commit()
      conn.close()
  except sqlite3.Error as error:
      print("Error deleting project:", error)
      
def sel_all_posts():
  list_posts = cur.execute("SELECT * FROM posts").fetchall()
  posts = []
  for post in list_posts:
    dict = {'id': post[0], 'title': post[1], 'text': post[2], 'link': post[3]}
    posts.append(dict)
  return posts

def sel_all_projects():
  list_projects = cur.execute("SELECT * FROM projects").fetchall()
  projects = []
  for project in list_projects:
    dict = {'id': project[0], 'title': project[1], 'description': project[2], 'link': project[3]}
    projects.append(dict)
  return projects

# list_posts = [['title1', 'text1', 'test'], ['title2', 'text2', 'test'], ['title3', 'text3', 'test'], ['title4', 'text4', 'test']]
# list_projects = [['title1', 'description1', 'link1'], ['title2', 'description2', 'link2'], ['title3', 'description3', 'link3'], ['title4', 'description4', 'link4']]
# for post in list_posts:
#   insert_post(post)
# for project in list_projects:
#   insert_project(project)

