from db_man import db_create_tables, db_insert_post, db_insert_project, db_select_all, db_delete


from flask import Flask, render_template, request, redirect


app = Flask("blog")
@app.route('/')
def home():
  return render_template('index.html')

    

  
app.run(host='0.0.0.0')