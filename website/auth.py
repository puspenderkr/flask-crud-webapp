from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

from datetime import datetime, timedelta

login_attempts = {}

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if email in login_attempts:
                # If the user has made more than 5 failed attempts in the last 10 minutes,
                # don't allow another attempt
                num_attempts, last_attempt_time = login_attempts[email]
                if num_attempts >= 2 and datetime.now() - last_attempt_time < timedelta(minutes=10):
                    flash('Too many failed login attempts. Please try again later.', category='error')
                    return redirect(url_for('auth.login'))

            if check_password_hash(user.password, password):
                flash("Logged in!", category='success')
                login_user(user, remember=True)

                # If the user has previously made failed login attempts, reset the counter
                if email in login_attempts:
                    del login_attempts[email]

                return redirect(url_for('views.home'))
            else:
                flash('Password is incorrect.', category='error')

                # Increment the number of failed login attempts for this user
                if email in login_attempts:
                    num_attempts, _ = login_attempts[email]
                    login_attempts[email] = (num_attempts + 1, datetime.now())
                else:
                    login_attempts[email] = (1, datetime.now())
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
