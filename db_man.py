import sqlite3
from sqlite3 import Error


#create the db and the tables for posts and projects
def db_create_tables():
  banco = sqlite3.connect('blog.db', check_same_thread=False)
  cursor = banco.cursor()
  cursor.execute("CREATE TABLE posts (index, post_title, post_text, post_info, post_link)")
  cursor.execute("CREATE TABLE projects (index, project_title, project_description, project_link)")
  
#insert data into posts
def db_insert_post(index, title, text, info, link):
  banco = sqlite3.connect('database.db', check_same_thread=False)
  cursor = banco.cursor()
  cursor.execute("INSERT INTO posts VALUES ('"+index+"', '"+title+"', '"+text+"', '"+info+"', '"+link+"')")
  banco.commit()

#insert data into projects
def db_insert_project(index, title, description, link):
  banco = sqlite3.connect('database.db', check_same_thread=False)
  cursor = banco.cursor()
  cursor.execute("INSERT INTO projects VALUES ('"+index+"', '"+title+"', '"+description+"', '"+link+"')")
  banco.commit()
  
#select all data from a certain table
def db_select_all(table):
  banco = sqlite3.connect('database.db', check_same_thread=False)
  cursor = banco.cursor()
  cursor.execute("SELECT * FROM '"+table+"'")
  #print(cursor.fetchall())
  return list(cursor.fetchall())

#delete a row from a given table based on the given index
def db_delete(table, index):
  banco = sqlite3.connect('database.db', check_same_thread=False)
  cursor = banco.cursor()
  try:
      cursor.execute("DELETE from '"+table+"' WHERE index = '"+index+"'")
      banco.commit()
      banco.close()
      print("Data has been successfully deleted")
  except sqlite3.Error as error:
      print("Error deleting:", error)