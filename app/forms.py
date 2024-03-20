from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField
from wtforms.validators import InputRequired, Regexp, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed

class AddPropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired(), Length(max=80)])
    description = TextAreaField('Description', validators=[InputRequired(), Length(max=400)])
    number_of_rooms = IntegerField('No. of Rooms', validators=[InputRequired()])
    number_of_bathrooms = IntegerField('No. of Bathrooms', validators=[InputRequired()])
    price = StringField('Price', validators=[InputRequired(), Length(max=40), Regexp('^\d{1,3}(,\d{3})*$', message="Correct number format is comma separated eg 100,000")])
    propertyType = SelectField('Property Type', choices=[('House', 'House'), ('Apartment', 'Apartment')], validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired(), Length(max=150)])
    image = FileField(validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], 'Only .png, .jpeg, and .jpg files')])