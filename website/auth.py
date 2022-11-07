from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from os import path
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    #data = request.form
    #print(data)
    if request.method == 'POST' :
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user :
            if check_password_hash(user.password, password) : # comparing two given parameters
                flash('Logged in Successfully!', category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, please try again', category='error')
        else:
            flash("Password or the username (Email address) might incorrect", category= 'error')

    return render_template("login.html", text ="Testing", version='Version: 0.1.0')

@auth.route('/logout')
def logout():
    return render_template("logout.html", version='Version: 0.1.0')

@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
    if request.method == 'POST' :
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email is already exit!", category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2 :
            flash('Password don\'t match!', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 character.', category='error')
        else:
            new_user = User(email =email, first_name = firstName, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully!', category='success')
            return redirect(url_for('views.home'))
    return render_template("sign_up.html", version='Version: 0.1.0')