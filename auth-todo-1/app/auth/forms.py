from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, EqualTo

from ..models import User


class RegistrationForm(FlaskForm):
	username = StringField('username',validators=[DataRequired()])
	password = PasswordField('password', validators=[DataRequired()])
	confirm_password = PasswordField('confirmPassword')

	def validate_username(self,field):
		if User.query.filter_by(username=field.data).first():
			raise ValidationError("Username Already in Use")