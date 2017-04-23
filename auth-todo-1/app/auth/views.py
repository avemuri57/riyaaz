from flask import render_template


from . import auth
from forms import RegistrationForm
from .. import db
from ..models import User

@auth.route('/login')
def login():
	return render_template('/auth/login.html')

@auth.route('/register',methods=['GET','POST'])
def register():
	form = RegistrationForm()

	if form.validate_on_submit():
		
		user = User(username=form.username.data,
					password=form.password.data)
		db.session.add(user)
		db.session.commit()
		#flash('You have successfully registered! You may now login.')
		return redirect(url_for('auth.login'))
	print(form.errors)
	return render_template('/auth/register.html')