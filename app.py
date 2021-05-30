from flask import Flask, render_template

app = Flask(__name__)

all_posts = [
    { 'title': 'Post 1', 'content': 'Post 1 ka content'},
    { 'title': 'Post 2', 'content': 'Post 2 ka content'},
    { 'title': 'Post 3', 'content': 'Post 2 ka content'},
    { 'title': 'Post 4', 'content': 'Post 2 ka content'}
    ]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/posts')
def getPosts():
    return render_template("posts.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)