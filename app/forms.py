from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField
from wtforms.validators import InputRequired, Regexp
from flask_wtf.file import FileField, FileRequired, FileAllowed

class AddPropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    number_of_rooms = IntegerField('No. of Rooms', validators=[InputRequired()])
    number_of_bathrooms = IntegerField('No. of Bathrooms', validators=[InputRequired()])
    price = StringField('Price', validators=[InputRequired(), Regexp('^\d{1,3}(,\d{3})*$', message="Invalid number format")])
    propertyType = SelectField('Property Type', choices=[('House', 'House'), ('Apartment', 'Apartment')], validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    image = FileField(validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], 'Only .png, .jpeg, and .jpg files')])