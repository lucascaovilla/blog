from db_man import db_create_tables, db_insert_post, db_insert_project, db_select_all, db_delete
from flask import Flask, render_template, request, redirect , url_for,  jsonify
from time import time
import json

app = Flask("blog")
@app.route('/', methods = ['GET', 'POST'])
def home():
  #text = request.args.get('button_text')
  
  
  if request.is_json:
  
    if request.method == 'GET':
      if request.args.get('button_text') == 'Posts':
        posts = db_select_all('posts')
        posts_list = []
        for post in posts:
          post = list(post)
          posts_list.append(post)
        print(posts_list)
        return jsonify({'posts': posts_list})
  
    if request.method == 'GET':
      if request.args.get('button_text') == 'Projects':
        return jsonify({'projects': db_select_all('projects')})
    
    if request.method == 'POST':
      card_text = json.loads(request.data).get('text')
      new_text = f'I got {card_text}'
      return jsonify({'data': new_text})
  
  return render_template('index.html')


    

  
app.run(host='0.0.0.0')