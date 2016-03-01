from flask.ext.wtf import Form
from wtforms import StringField, BooleanField,TextField,IntegerField,FileField,SelectField
from wtforms.validators import DataRequired,Required




class ProfileForm(Form):
    username = TextField('Username', validators=[Required()])
    first_name = TextField('First Name', validators=[Required()])
    last_name = TextField('Last Name', validators=[Required()])
    age=IntegerField('age',validators=[Required()])
    image= FileField('Image File', validators=[Required()])
    sex= SelectField('Sex', choices=[('Female','female'),('Male','male')],validators=[Required()])