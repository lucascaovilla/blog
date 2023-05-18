from databases.blog_database import db_create_tables, db_insert_post, db_insert_project, db_select_all, db_delete
from flask import Flask, render_template, request, redirect, url_for, jsonify
from time import time
import json
from databases.users_database import handle_admin
import hashlib

app = Flask("blog")


@app.route('/', methods=['GET', 'POST'])
def home():
  #text = request.args.get('button_text')
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
      
      if request.args.get('op_id') == 'Login' or request.args.get('op_id') == 'login':
        username = request.args.get('username')
        password = hashlib.sha256(request.args.get('password').encode()).hexdigest()
        print("----------")
        print(username)
        print("----------")
        print(password)
        print("----------")
        status = handle_admin(username, password)
        return jsonify({'status': status.decode()})
      
      
    if request.method == 'POST':
      card_text = json.loads(request.data).get('text')

      new_text = f'I got {card_text}'
      print(new_text)
      return jsonify({'data': new_text})

  return render_template('index.html')


app.run(host='0.0.0.0')
