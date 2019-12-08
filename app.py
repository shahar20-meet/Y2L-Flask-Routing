from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import *


app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


##### Code here ######
@app.route("/")
def hello_world():
	return render_template("home.html")

@app.route("/s")
def store():
	product = return_all(createThread())
	return render_template("store.html", products = product)

@app.route("/cart")
def cart():

	return render_template("cart.html",product = return_all(createThread()))

@app.route("/about")
def about():
	return render_template("about.html")


@app.route('/add_to_cart/<int:pid>')
def add_to_cart(pid):
	Add_To_Cart(createThread(),pid)
	return redirect(url_for('store'))


#####################


if __name__ == '__main__':
    app.run(debug=True)