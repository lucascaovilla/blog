import sqlite3
from sqlite3 import Error



def db_create_table():
  banco = sqlite3.connect('database.db', check_same_thread=False)
  cursor = banco.cursor()
  cursor.execute("CREATE TABLE registers (code text, number text)")
def db_insert(codigo, numero):
  banco = sqlite3.connect('database.db', check_same_thread=False)
  cursor = banco.cursor()
  cursor.execute("INSERT INTO registers VALUES ('"+codigo+"', '"+numero+"')")
  banco.commit()
def db_select_all():
  banco = sqlite3.connect('database.db', check_same_thread=False)
  cursor = banco.cursor()
  cursor.execute("SELECT * FROM registers")
  #print(cursor.fetchall())
  return list(cursor.fetchall())
def db_delete(code):
  banco = sqlite3.connect('database.db', check_same_thread=False)
  cursor = banco.cursor()
  try:
      cursor.execute("DELETE from registers WHERE code = '"+code+"'")
      banco.commit()
      banco.close()
      print("Os dados foram removidos com sucesso")
  except sqlite3.Error as error:
      print("Erro ao excluir:", error)

db_create_table()