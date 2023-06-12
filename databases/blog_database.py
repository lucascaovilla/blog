import sqlite3
from sqlite3 import Error

conn = sqlite3.connect('databases/data/blog.db', check_same_thread=False)
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS posts 
            (ident INTEGER PRIMARY KEY, 
            creator VARCHAR(255) NOT NULL, 
            datetime DATETIME NOT NULL, 
            id VARCHAR(255) NOT NULL, 
            title VARCHAR(255) NOT NULL, 
            text VARCHAR(255) NOT NULL)""")

cur.execute("""CREATE TABLE IF NOT EXISTS projects 
            (id INTEGER PRIMARY KEY, 
            title VARCHAR(255), 
            description VARCHAR(255), 
            link VARCHAR(255))""")


def insert_post(post):
  if not cur.execute("SELECT * FROM posts WHERE title = ?", (post[3],)).fetchall():
    cur.execute("""INSERT INTO posts (creator, datetime, id, title, text) VALUES (?, ?, ?, ?, ?)""", (post[0], post[1], post[2], post[3], post[4]))
    conn.commit()
    return True
  else:
    return False

def select_post(post_id):
    post_data = cur.execute("SELECT * FROM posts WHERE id = (?)", (post_id,)).fetchall()[0]
    post = {'ident': post_data[0], 'creator': post_data[1], 'datetime': post_data[2], 'id': post_data[3], 'title': post_data[4], 'text': post_data[5]}
    return post

def delete_post(title):
  if cur.execute("SELECT * FROM posts WHERE title = ?", (title,)).fetchall():
    try:
        cur.execute("DELETE from posts WHERE title = ?", (title,))
        conn.commit()

    except sqlite3.Error as error:
        print("Error deleting post:", error)
        
def sel_all_posts():
    list_posts = cur.execute("SELECT * FROM posts").fetchall()
    posts = []
    for post in list_posts:
      dict = {'ident': post[0], 'creator': post[1], 'datetime': post[2], 'id': post[3], 'title': post[4], 'text': post[5]}
      posts.append(dict)
    return posts


def insert_project(project):
  if not cur.execute("SELECT * FROM projects WHERE title = ?", (project[0],)).fetchall():
    cur.execute("INSERT INTO projects (title, description, link) VALUES (?, ?, ?)", (project[0], project[1], project[2]))
    conn.commit()
    return True
  else:
    return False

def select_project(project_id):
    project_data = cur.execute("SELECT * FROM projects WHERE id = (?)", (project_id,)).fetchall()[0]
    project = {'ident': project_data[0], 'title': project_data[1], 'description': project_data[2], 'link': project_data[3]}
    return project

def delete_project(title):
  try:
      cur.execute("DELETE from projects WHERE title = ?", (title,))
      conn.commit()
  except sqlite3.Error as error:
      print("Error deleting project:", error)

def sel_all_projects():
    list_projects = cur.execute("SELECT * FROM projects").fetchall()
    projects = []
    for project in list_projects:
      dict = {'id': project[0], 'title': project[1], 'description': project[2], 'link': project[3]}
      projects.append(dict)
    return projects

text= "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Bibendum ut tristique et egestas quis ipsum suspendisse ultrices. Sit amet nulla facilisi morbi tempus iaculis urna id. Nisi scelerisque eu ultrices vitae auctor. Velit egestas dui id ornare. Nunc aliquet bibendum enim facilisis gravida neque. Vitae justo eget magna fermentum iaculis eu non diam. Nunc aliquet bibendum enim facilisis gravida. In metus vulputate eu scelerisque felis. Nibh sed pulvinar proin gravida. Egestas purus viverra accumsan in nisl nisi.Placerat vestibulum lectus mauris ultrices eros in cursus turpis massa. Ultricies tristique nulla aliquet enim tortor at. Sodales ut etiam sit amet nisl purus. Praesent semper feugiat nibh sed pulvinar proin. Odio facilisis mauris sit amet massa vitae tortor condimentum. Auctor neque vitae tempus quam pellentesque nec. Diam vulputate ut pharetra sit. Sed odio morbi quis commodo odio aenean sed adipiscing diam. Arcu non sodales neque sodales ut etiam sit amet nisl. Orci dapibus ultrices in iaculis nunc sed.Faucibus in ornare quam viverra orci sagittis eu. Euismod in pellentesque massa placerat duis. Egestas integer eget aliquet nibh. Nisi vitae suscipit tellus mauris. Viverra justo nec ultrices dui sapien eget mi. Diam ut venenatis tellus in metus. Nibh venenatis cras sed felis eget velit. Morbi tristique senectus et netus et malesuada fames ac. Morbi tristique senectus et netus et malesuada. Nibh praesent tristique magna sit amet purus gravida. A diam sollicitudin tempor id eu nisl nunc mi ipsum. Risus commodo viverra maecenas accumsan lacus vel facilisis. Porttitor lacus luctus accumsan tortor posuere ac. Morbi quis commodo odio aenean sed adipiscing. Consequat mauris nunc congue nisi vitae suscipit tellus. Diam maecenas sed enim ut sem viverra aliquet eget.Suspendisse sed nisi lacus sed viverra tellus in hac. Pretium nibh ipsum consequat nisl vel pretium lectus quam. Ullamcorper eget nulla facilisi etiam dignissim. Semper risus in hendrerit gravida rutrum quisque non. Enim nulla aliquet porttitor lacus luctus accumsan tortor posuere ac. Aenean et tortor at risus viverra. Vulputate eu scelerisque felis imperdiet. Porta nibh venenatis cras sed felis eget velit. Malesuada nunc vel risus commodo. Et netus et malesuada fames. Turpis massa tincidunt dui ut ornare lectus sit. Luctus venenatis lectus magna fringilla. Sollicitudin tempor id eu nisl. Neque gravida in fermentum et. Urna nec tincidunt praesent semper feugiat nibh sed pulvinar.Ridiculus mus mauris vitae ultricies leo integer. Mattis molestie a iaculis at erat pellentesque adipiscing. Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit sed. Massa tempor nec feugiat nisl pretium fusce id. Auctor elit sed vulputate mi. Nec nam aliquam sem et. Sed viverra ipsum nunc aliquet bibendum enim facilisis gravida neque. Quis risus sed vulputate odio. Sit amet consectetur adipiscing elit ut aliquam. Quis auctor elit sed vulputate mi sit amet. Ultricies tristique nulla aliquet enim tortor. At volutpat diam ut venenatis tellus. Odio ut enim blandit volutpat maecenas. Posuere urna nec tincidunt praesent semper feugiat nibh sed pulvinar.Ac turpis egestas integer eget aliquet nibh. In vitae turpis massa sed elementum tempus egestas. Fermentum iaculis eu non diam phasellus vestibulum. Tempus quam pellentesque nec nam aliquam sem et. Nunc pulvinar sapien et ligula ullamcorper malesuada proin libero nunc. Nulla aliquet porttitor lacus luctus accumsan tortor. Rhoncus aenean vel elit scelerisque. Eu sem integer vitae justo. Viverra mauris in aliquam sem fringilla ut. Morbi tristique senectus et netus et malesuada. Suscipit tellus mauris a diam. Sed libero enim sed faucibus turpis in. Pellentesque pulvinar pellentesque habitant morbi tristique senectus et netus. Pulvinar neque laoreet suspendisse interdum consectetur libero id faucibus nisl. Odio ut enim blandit volutpat maecenas volutpat blandit. Donec et odio pellentesque diam volutpat commodo. Magnis dis parturient montes nascetur ridiculus mus mauris vitae ultricies. Nec nam aliquam sem et tortor consequat. Iaculis at erat pellentesque adipiscing commodo elit at imperdiet. Auctor elit sed vulputate mi sit amet mauris commodo quis.Massa massa ultricies mi quis hendrerit dolor magna. Dolor sit amet consectetur adipiscing. Turpis egestas maecenas pharetra convallis. Metus vulputate eu scelerisque felis imperdiet proin. Euismod lacinia at quis risus sed vulputate odio ut enim. Duis at consectetur lorem donec massa. Habitasse platea dictumst vestibulum rhoncus. Aliquet risus feugiat in ante metus dictum. Fringilla est ullamcorper eget nulla facilisi etiam dignissim diam quis. Quam pellentesque nec nam aliquam. Volutpat blandit aliquam etiam erat velit scelerisque in dictum. Scelerisque mauris pellentesque pulvinar pellentesque habitant. Sit amet massa vitae tortor condimentum lacinia quis.Donec et odio pellentesque diam volutpat commodo sed egestas. Mi sit amet mauris commodo quis imperdiet massa tincidunt. Ornare arcu odio ut sem nulla pharetra diam. Faucibus et molestie ac feugiat sed. Eu scelerisque felis imperdiet proin fermentum. Quisque non tellus orci ac auctor. Porttitor massa id neque aliquam. Sapien faucibus et molestie ac feugiat. Quis vel eros donec ac odio tempor orci dapibus ultrices. Leo vel fringilla est ullamcorper eget. Magna fringilla urna porttitor rhoncus dolor purus. Sit amet consectetur adipiscing elit duis tristique. Nisl purus in mollis nunc. Nascetur ridiculus mus mauris vitae ultricies leo. Ultrices tincidunt arcu non sodales neque. Ultricies mi eget mauris pharetra et ultrices neque ornare aenean. Diam maecenas ultricies mi eget mauris pharetra et ultrices. Eu feugiat pretium nibh ipsum consequat nisl vel pretium. Faucibus a pellentesque sit amet porttitor eget dolor morbi non.Sit amet volutpat consequat mauris nunc congue nisi vitae. Tortor at risus viverra adipiscing at in tellus integer feugiat. Quis vel eros donec ac odio. Pellentesque habitant morbi tristique senectus et. Lacinia at quis risus sed vulputate odio. Massa massa ultricies mi quis. Vel fringilla est ullamcorper eget nulla. Massa ultricies mi quis hendrerit dolor magna. Volutpat blandit aliquam etiam erat velit scelerisque in dictum non. At in tellus integer feugiat scelerisque. Purus ut faucibus pulvinar elementum. Nibh praesent tristique magna sit amet. Penatibus et magnis dis parturient montes. Dictum non consectetur a erat nam at lectus urna.Id eu nisl nunc mi. Tortor posuere ac ut consequat semper viverra. Amet commodo nulla facilisi nullam. Risus sed vulputate odio ut enim blandit. Pulvinar pellentesque habitant morbi tristique senectus et. Lectus sit amet est placerat in. Sem et tortor consequat id. Dictum non consectetur a erat nam at lectus. Semper feugiat nibh sed pulvinar. Nisl rhoncus mattis rhoncus urna neque viverra. Ultrices in iaculis nunc sed. Nullam ac tortor vitae purus faucibus ornare suspendisse. Aliquam eleifend mi in nulla posuere sollicitudin aliquam ultrices sagittis. Erat pellentesque adipiscing commodo elit at imperdiet dui accumsan. Aliquet nibh praesent tristique magna sit. Ultricies integer quis auctor elit sed.Semper quis lectus nulla at volutpat diam ut. Sit amet nulla facilisi morbi tempus iaculis urna id. Dignissim cras tincidunt lobortis feugiat vivamus at. Adipiscing elit ut aliquam purus sit amet luctus. In ornare quam viverra orci sagittis. Libero enim sed faucibus turpis in. Congue nisi vitae suscipit tellus mauris a. Egestas integer eget aliquet nibh praesent tristique. Amet nulla facilisi morbi tempus iaculis urna. Magna eget est lorem ipsum dolor.Eget mi proin sed libero enim. Arcu non sodales neque sodales. Parturient montes nascetur ridiculus mus. Eros in cursus turpis massa tincidunt dui ut. Tristique risus nec feugiat in fermentum posuere urna nec tincidunt. Tortor posuere ac ut consequat semper viverra. Pellentesque habitant morbi tristique senectus et. Magna eget est lorem ipsum. Interdum velit euismod in pellentesque massa. Vitae tortor condimentum lacinia quis vel. Adipiscing vitae proin sagittis nisl. Vulputate dignissim suspendisse in est ante in nibh. Lectus sit amet est placerat in egestas erat imperdiet sed. Parturient montes nascetur ridiculus mus mauris. Laoreet id donec ultrices tincidunt arcu. Donec ultrices tincidunt arcu non sodales neque. Rhoncus mattis rhoncus urna neque. Ornare massa eget egestas purus viverra accumsan in. Habitant morbi tristique senectus et netus. Pellentesque id nibh tortor id.Et tortor consequat id porta nibh venenatis cras sed felis. Enim eu turpis egestas pretium. In tellus integer feugiat scelerisque varius morbi enim nunc faucibus. Nisl vel pretium lectus quam id leo. Ullamcorper morbi tincidunt ornare massa eget. Non pulvinar neque laoreet suspendisse interdum consectetur libero. Integer vitae justo eget magna. Laoreet suspendisse interdum consectetur libero id faucibus nisl tincidunt. Tempus imperdiet nulla malesuada pellentesque elit eget gravida cum sociis. Cras ornare arcu dui vivamus arcu. Vitae sapien pellentesque habitant morbi tristique senectus et netus. Sit amet consectetur adipiscing elit. Ullamcorper malesuada proin libero nunc. Enim neque volutpat ac tincidunt vitae semper. Ornare lectus sit amet est placerat in egestas. Vehicula ipsum a arcu cursus vitae congue mauris. Mauris a diam maecenas sed enim ut sem. Cursus turpis massa tincidunt dui ut ornare lectus. Rhoncus dolor purus non enim. Hac habitasse platea dictumst vestibulum rhoncus est.Ante metus dictum at tempor commodo ullamcorper a. Sit amet justo donec enim. In cursus turpis massa tincidunt dui ut ornare lectus sit. Scelerisque in dictum non consectetur a erat nam. Viverra maecenas accumsan lacus vel. In eu mi bibendum neque egestas congue quisque egestas diam. Id diam maecenas ultricies mi eget. Dictum at tempor commodo ullamcorper a lacus vestibulum sed. Ac turpis egestas integer eget. Tincidunt vitae semper quis lectus nulla at.Malesuada proin libero nunc consequat interdum. Volutpat odio facilisis mauris sit amet massa vitae. Accumsan tortor posuere ac ut. Tristique risus nec feugiat in fermentum posuere. Elementum pulvinar etiam non quam lacus suspendisse faucibus. Felis bibendum ut tristique et egestas quis ipsum suspendisse. Scelerisque eu ultrices vitae auctor. Consectetur adipiscing elit ut aliquam purus sit. Et malesuada fames ac turpis egestas integer. Urna molestie at elementum eu. Porttitor eget dolor morbi non arcu risus quis varius. Sit amet mattis vulputate enim nulla. Varius sit amet mattis vulputate enim nulla aliquet porttitor lacus. Non nisi est sit amet facilisis magna. Laoreet id donec ultrices tincidunt arcu non sodales neque sodales. Sit amet nisl suscipit adipiscing bibendum est ultricies integer quis."

for i in range(5):
  i = str(i+1)
  #delete_post('title'+i)
  #delete_project('title'+i)
  insert_post(('creator'+i, 'datetime'+i, 'id'+i, 'title'+i, text))
  insert_project(('title'+i, text, 'link'+i))
  
