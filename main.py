from databases.blog_database import db_create_tables, db_insert_post, db_insert_project, db_select_all, db_delete
from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from time import time
import json
from databases.users_database import handle_admin
import hashlib


app = Flask("blog")
app.secret_key = "blog"

@app.route('/', methods=['GET', 'POST'])
def home():
  session['logged_in'] = False
  if request.is_json:

    if request.method == 'GET':
      print()
      print("receiving request")
      print()
      if request.args.get('button_text') == 'Posts' or request.args.get('button_text') == 'posts':
        print(db_select_all('posts'))
        return jsonify({'posts': db_select_all('posts')})
      
      if request.args.get('button_text') == 'Projects' or request.args.get('button_text') == 'projects':
        print(db_select_all('projects'))        
        return jsonify({'projects': db_select_all('projects')})
     
    # if request.method == 'POST':
    #   card_text = json.loads(request.data).get('text')

    #   new_text = f'I got {card_text}'
    #   print(new_text)
    #   return jsonify({'data': new_text})

  return render_template('index.html')

@app.route('/admin')
def admin():
  session['logged_in'] = False
  return render_template('admin.html')

@app.route("/action",methods=["POST","GET"])
def action():

    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()
        print(username)
        print(password)
        
    
        if handle_admin(username, password):
            print('logged')
            session['logged_in'] = True
            session['username'] = username
            msg = 'success'
        else:
               msg = 'No-data'
           
    return jsonify(msg)   
 
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
  
app.run(host='0.0.0.0')
