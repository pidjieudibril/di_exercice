import flask
import database_manager # this is our module

app = flask.Flask(__name__)

database_manager.create_database()
@app.route("/")
@app.route("/products")
def products_page():

    data = database_manager.load_database()
    template = open('templates/my_template.jinja', 'r').read()
    css      = open('static/style.css', 'r').read()
    return flask.render_template_string(template, products=data, additional_css=css)


app.run(debug=True)