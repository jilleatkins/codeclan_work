from events.app import app
from models.events import Event
from flask import render_template


@app.route('/')
def index():
  return render_template('index.html')