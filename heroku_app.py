import os, firebase_conf, collections
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
firebase = firebase_conf.fb()
db = firebase.database()


@app.route('/')
def index():
    data1 = {"name": "Morty"}
    data2 = {"name": "Rick"}
    data3 = {"name": "Summer"}
    data4 = {"age": 5}
    data5 = {"name": "Morty"}
    # db.child("users").push(data3)
    # db.child("users").child("Morty").push(data4)

    #users = db.child("users").get()
    # for user in users.each():
    #     print("key: " + user.key())

    #print("db call: " + str(users))
    #return users.value()
    #return render_template('landing.html', users=users.val())
    return render_template('landing.html')

@app.route('/', methods=['POST'])
def new_playlist():
    name = request.form['playlist-name']
    obj = db.child("playlist").push({"name": name})
    return redirect(url_for('get_play', playid=list(obj.values())[0]))

@app.route('/playlist/<playid>', methods=['GET'])
def get_play(playid):
    playlist = db.child("playlist").child(playid).get()
    return render_template('playlist.html', current_url=request.url, name=playlist.val()['name'])

@app.route('/playlist/<playid>', methods=['POST'])
def post_play(playid):

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
