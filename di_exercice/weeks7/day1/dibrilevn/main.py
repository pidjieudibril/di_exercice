import flask
app = flask.Flask(__name__)
@app.route('/')
def index():
    return "Hello, World!"
@app.route('/home/<username>')
def name(username):
    return "Hello, !"