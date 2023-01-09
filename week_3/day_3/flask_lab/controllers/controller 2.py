from app import app
from flask import render_template
from models.order_list import orders

@app.route("/")
def index():
    return render_template("index.html", title="Home", orders=orders)


@app.route("/orders/<index>")
def order(index):
    return render_template("orders.html", title="Orders", order=orders[int(index)])