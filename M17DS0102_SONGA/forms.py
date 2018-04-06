from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields import StringField
from wtforms.validators import DataRequired



class LocationForm(FlaskForm):
    user = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])

    submit = SubmitField('Log in')