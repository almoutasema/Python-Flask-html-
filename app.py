from flask import Flask, render_template
from data import posts

app = Flask(__name__)
posts = posts()

# Define a route for the root URL "/"
@app.route('/')
def home():
    return render_template('home.html')



@app.route('/about')
def about():
    return render_template('about.html')






@app.route('/blogger')
def blogger():
    return render_template('blogger.html', posts = posts)



@app.route('/post/<string:id>/')
def posts(id):
    return render_template('post.html', id=id)



if __name__ == '__main__':
    app.run(debug=True)
