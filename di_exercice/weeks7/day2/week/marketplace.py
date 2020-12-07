from flask import Flask, render_template

app = flask.Flask(__name__)
@app.route("/")

def accueil():
     return render_template("template/accueil.html")

@app.route("/products")
def products():
    return render_template("template/products.html")

    data = database_manager.load_database()
    template = open('templates/accueil.html', 'r').read()
    css = open('static/style.css', 'r').read()
    return flask.render_template_string(template, products=data, additional_css=css)

@app.route("/product/<product_id>")
def details():
    return render_template("template/details.html")

app.run(debug=True)