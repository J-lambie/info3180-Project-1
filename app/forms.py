from flask.ext.wtf import Form
from wtforms import StringField, BooleanField,TextField,IntegerField,FileField,SelectField
from wtforms.validators import DataRequired,Required


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class ProfileForm(Form):
    first_name = TextField('First Name', validators=[Required()])
    last_name = TextField('Last Name', validators=[Required()])
    age=IntegerField('age',validators=[Required()])
    image        = FileField(u'Image File', validators=[Required()])
    sex= SelectField(u'Sex', choices=['female','male'])