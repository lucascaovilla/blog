from databases.blog_database import sel_all_posts, sel_all_projects, insert_post, insert_project
from databases.users_database import handle_user, insert_user
   
from flask import Flask, render_template, request, redirect, jsonify, session
import hashlib


app = Flask("blog")
app.secret_key = "blog"

@app.route('/')
def home():
    if request.args.get('projects') == 'projects':     
        return render_template('index.html', render_projects = True, projects = sel_all_projects())
    if request.args.get('about') == 'about':     
        return render_template('index.html', about = True)
    return render_template('index.html', render_posts = True, posts = sel_all_posts())

@app.route("/create-account",methods=["POST","GET"])
def create_account():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()
        if insert_user(username, email, password):
            session['logged_in'] = True
            session['username'] = username
            msg = 'Success! Welcome ' + username
        else:
            msg = 'No-data'
        return jsonify(msg)
    
@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()
        if handle_user(username, password):
            session['logged_in'] = True
            session['username'] = username
            msg = 'Success! Welcome ' + username
        else:
            msg = 'No-data'
        return jsonify(msg)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route("/create-post",methods=["POST","GET"])
def create_post():
    if request.method == 'POST':
        username = session['username']
        title = request.form['title']
        text = request.form['text']
        if insert_post([title, text, username]):
            session['logged_in'] = True
            msg = 'Posted successfully!'
        else:
            msg = 'No-data'
        return jsonify(msg)
    
app.run(host='0.0.0.0')
