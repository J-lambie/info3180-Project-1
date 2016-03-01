from flask.ext.wtf import Form
from wtforms import StringField, BooleanField,TextField,IntegerField,FileField,SelectField
from wtforms.validators import DataRequired,Required




class ProfileForm(Form):
    username = TextField('Username', validators=[Required()])
    first_name = TextField('First Name', validators=[Required()])
    last_name = TextField('Last Name', validators=[Required()])
    age=IntegerField('age',validators=[Required()])
    image        = TextField(u'Image File', validators=[Required()])
    sex= SelectField(u'Sex', choices=['female','male'],validators=[Required()])