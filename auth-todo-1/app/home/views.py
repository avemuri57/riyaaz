from flask import render_template

from . import home

@home.route('/')
def hello():
	return render_template('home/index.html')