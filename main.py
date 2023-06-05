from databases.blog_database import sel_all_posts, sel_all_projects
from databases.users_database import handle_admin
   
from flask import Flask, render_template, request, redirect, url_for, jsonify, session
import json
import hashlib


app = Flask("blog")
app.secret_key = "blog"

@app.route('/')
def home():
    if request.args.get('projects') == 'projects':     
        return render_template('index.html', projects = sel_all_projects())
    return render_template('index.html', posts = sel_all_posts())

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('account.html')

@app.route("/action",methods=["POST","GET"])
def action():
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()
        if handle_admin(username, password):
            session['logged_in'] = True
            session['username'] = username
            msg = 'Success! Welcome ' + username
            return jsonify(msg)
        else:
               msg = 'No-data'
               return jsonify(msg)
    return render_template('account.html')

 
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
  
app.run(host='0.0.0.0')
