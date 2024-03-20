"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
from .forms import AddPropertyForm
from .models import Property

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route ('/properties', methods=['GET'])
def properties():
    # def get_uploaded_images():
    #     uploaded_images = []

    #     rootdir = os.path.join(app.config['UPLOAD_FOLDER'])
    #     for subdir, dirs, files in os.walk(rootdir):
    #         for file in files:
    #             file_extension = os.path.splitext(file)
    #             if file_extension[1].lower() in ['.png', '.jpg']:
    #                 uploaded_images.append(os.path.join(file))
    #     return uploaded_images
    
    def get_img(filename):
        return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)
    
    props = db.session.execute(db.select(Property)).scalars()

    return render_template('properties.html', props=props, get_img=get_img)

@app.route('/properties/create', methods=['GET', 'POST'])
def newProperty():
    form = AddPropertyForm()

    if form.validate_on_submit():

        image = form.image.data
        filename = secure_filename(image.filename)
        image.save(os.path.join(
            app.config['UPLOAD_FOLDER'], filename
        ))
        
        prop = Property(
            form.title.data,
            form.description.data,
            form.number_of_rooms.data,
            form.number_of_bathrooms.data,
            form.price.data,
            form.propertyType.data,
            form.location.data,
            filename
        )
        db.session.add(prop)
        db.session.commit()
    
        flash('Property Added')
        return redirect(url_for('properties'))

    return render_template('newProperty.html', form=form)

@app.route('/uploads/<filename>')
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
