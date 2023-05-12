import sqlite3
from sqlite3 import Error


#create the db and the tables for posts and projects
def db_create_tables():
  banco = sqlite3.connect('blog.db', check_same_thread=False)
  cursor = banco.cursor()
  cursor.execute("CREATE TABLE IF NOT EXISTS posts (id text, post_title text, post_text text, post_link text)")
  cursor.execute("CREATE TABLE IF NOT EXISTS projects (id text, project_title, project_description text, project_link text)")
  
#insert data into posts
def db_insert_post(post):
  index = str(len(db_select_all('posts')) + 1)
  title = post[0]
  text = post[1]
  link = post[2]
  banco = sqlite3.connect('blog.db', check_same_thread=False)
  cursor = banco.cursor()
  cursor.execute("INSERT INTO posts VALUES ('"+index+"', '"+title+"', '"+text+"', '"+link+"')")
  banco.commit()

#insert data into projects
def db_insert_project(project):
  index = str(len(db_select_all('projects')) + 1)
  title = project[0]
  description = project[1]
  link = project[2]
  banco = sqlite3.connect('blog.db', check_same_thread=False)
  cursor = banco.cursor()
  cursor.execute("INSERT INTO projects VALUES ('"+index+"', '"+title+"', '"+description+"', '"+link+"')")
  banco.commit()
  
#select all data from a certain table
def db_select_all(table):
  banco = sqlite3.connect('blog.db', check_same_thread=False)
  cursor = banco.cursor()
  cursor.execute("SELECT * FROM '"+table+"'")
  #print(cursor.fetchall())
  return list(cursor.fetchall())

#delete a row from a given table based on the given index
def db_delete(table, index):
  banco = sqlite3.connect('blog.db', check_same_thread=False)
  cursor = banco.cursor()
  try:
      cursor.execute("DELETE from '"+table+"' WHERE id = '"+index+"'")
      banco.commit()
      banco.close()
      print("Data has been successfully deleted")
  except sqlite3.Error as error:
      print("Error deleting:", error)
      
db_create_tables()

list_posts = [['title1', 'text1', 'link1'], ['title2', 'text2', 'link2'], ['title3', 'text3', 'link3'], ['title4', 'text4', 'link4']]

list_projects = [['title1', 'description1', 'link1'], ['title2', 'description2', 'link2'], ['title3', 'description3', 'link3'], ['title4', 'description4', 'link4']]


# for post in list_posts:
#   db_insert_post(post)
  
# for project in list_projects:
#   db_insert_project(project)

# for i in range(20):
#   db_delete('posts', str(i+1))
#   db_delete('projects', str(i+1))


