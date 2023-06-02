import sqlite3
from sqlite3 import Error

conn = sqlite3.connect('databases/data/blog.db', check_same_thread=False)
cursor = conn.cursor()

def db_create_tables():
  cursor.execute("CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY, post_title TEXT, post_text TEXT, post_link TEXT)")
  cursor.execute("CREATE TABLE IF NOT EXISTS projects (id INTEGER PRIMARY KEY, project_title TEXT, project_description TEXT, project_link text)")
  
def db_insert_post(post):
  title = post[0]
  text = post[1]
  link = post[2]
  cursor.execute("INSERT INTO posts VALUES ('"+title+"', '"+text+"', '"+link+"')")
  conn.commit()

def db_insert_project(project):
  title = project[0]
  description = project[1]
  link = project[2]
  cursor.execute("INSERT INTO projects VALUES ('"+title+"', '"+description+"', '"+link+"')")
  conn.commit()

def db_delete(table, index):
  try:
      cursor.execute("DELETE from '"+table+"' WHERE id = '"+index+"'")
      conn.commit()
      conn.close()
      print("Data has been successfully deleted")
  except sqlite3.Error as error:
      print("Error deleting:", error)
      
def sel_all_posts():
  list_posts = cursor.execute("SELECT * FROM posts").fetchall()
  posts = []
  for post in list_posts:
    dict = {'id': post[0], 'title': post[1], 'text': post[2], 'link': post[3]}
    posts.append(dict)
  return posts

def sel_all_projects():
  list_projects = cursor.execute("SELECT * FROM projects").fetchall()
  projects = []
  for project in list_projects:
    dict = {'id': project[0], 'title': project[1], 'description': project[2], 'link': project[3]}
    projects.append(dict)
  return projects

#list_posts = [['title1', 'text1', 'link1'], ['title2', 'text2', 'link2'], ['title3', 'text3', 'link3'], ['title4', 'text4', 'link4']]

#list_projects = [['title1', 'description1', 'link1'], ['title2', 'description2', 'link2'], ['title3', 'description3', 'link3'], ['title4', 'description4', 'link4']]

#db_create_tables()

# for post in list_posts:
#   db_insert_post(post)
  
# for project in list_projects:
#   db_insert_project(project)

# for i in range(20):
#   db_delete('posts', str(i+1))
#   db_delete('projects', str(i+1))


