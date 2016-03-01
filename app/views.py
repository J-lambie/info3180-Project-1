"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://wecrerkzeug.pocoo.org/documentation/

This file creates your application.
"""
import os,time
from flask import render_template, request, redirect, url_for,jsonify,g,session
from app import db

from flask.ext.wtf import Form 
from wtforms.fields import TextField # other fields include PasswordField 
from wtforms.validators import Required, Email
from app.models import Myprofile
from app.forms import ProfileForm

from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from app import oid, lm


def request_wants_json():
    best = request.accept_mimetypes \
        .best_match(['application/json', 'text/html'])
    return best == 'application/json' and \
        request.accept_mimetypes[best] > \
        request.accept_mimetypes['text/html']

@app.before_request
def before_request():
    g.user = current_user
    db.create_all()
    
###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/profile/', methods=['POST','GET'])
def profile_add():
    if request.method == 'POST':
        username = request.form['username']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age=request.form['age']
        image=request.files['image']
        sex=request.form['sex']
        imagename = image.filename
        image.save(os.path.join("app/static/img/", imagename))
        # write the information to the database
        newprofile = Myprofile(username=username,
                               first_name=first_name,
                               last_name=last_name,
                               age=age,
                               sex=sex,
                               image=imagename)
        db.session.add(newprofile)
        db.session.commit()
    
        return "{} {} was added to the database".format(request.form['first_name'],
                                             request.form['last_name'])
        
    form = ProfileForm()
    return render_template('profile_add.html',
                           form=form)

@app.route('/profiles/',methods=["POST","GET"])
def profile_list():
    profiles = Myprofile.query.all()
    if request_wants_json():
        return jsonify(profiles=[x.to_json() for x in profiles])
    return render_template('profile_list.html',
                            profiles=profiles)

@app.route('/profile/<int:userid>')
def profile_view(userid):
    times=time.strftime("%a, %d %b  %Y")
    profile = Myprofile.query.get(id)
    if request_wants_json():
        return jsonify(profile.userid,profile.username,profile.age,profile.sex)
    return render_template('profile_view.html',profile=profile,time=times)


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request

def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")
