from flask import render_template, request
from models.library import Library
from app import app

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/titles')
def orders():
  return render_template('titles.html', titles=titles)

@app.route('/titles/<int:title_index>')
def title(title_index):
  my_title = get_title(title_index)
  return render_template('title.html', title=my_title)

@app.route('/titles/new')
def new_titles():
  return render_template('new_titles.html')

@app.route('/titles', methods=['POST'])
def save_order():
  form_data = request.form
  title = form_data['title']
  title_author = form_data['title_author']
  title_year = form_data['title_year']
  title_published = form_data['title_published']

  new_title = Pizza(pizza_price, pizza_name, gluten_free, pizza_size)
  add_order(new_pizza)

  return render_template('orders.html', pizzas=pizzas)