from flask import Flask, render_template, flash, request, session
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import os
import re

from sqlalchemy.orm import sessionmaker
from model import engine, User

app = Flask(__name__)


class ReusableForm(Form):
    name = StringField('Name:', validators=[validators.required()])
    email = StringField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
    password = StringField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "You are Logged In....!  <a href='/logout'>Logout</a>"


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.method == 'POST':
        username = str(request.form['username'])
        print("\nUsername", username)
        password = str(request.form['password'])
        print("\nPassword", password)
        n = len(password)

        if 6 <= n < 15:

            password_scores = {0: 'Horrible', 1: 'Weak', 2: 'Medium', 3: 'Strong'}
            password_strength = dict.fromkeys(['has_upper', 'has_lower', 'has_num'], False)

            if re.search(r'[A-Z]', password):
                password_strength['has_upper'] = True
            if re.search(r'[a-z]', password):
                password_strength['has_lower'] = True
            if re.search(r'[0-9]', password):
                password_strength['has_num'] = True

            score = len([b for b in password_strength.values() if b])

            print('\nThe Entered Password is %s' % password_scores[score])

            if score == 1:
                print("\n The Password don't contain a Number")

            if score == 2:
                print("\n The Password don't contain an Uppercase")

            if score == 3:
                print("\n The Password is Strong, you are good to GO....")

                if request.form['password'] == password and request.form['username'] == username:
                    session['logged_in'] = True
                    Session = sessionmaker(bind=engine)
                    s = Session()
                    psd = s.query(User).add_columns(User.username, User.id, User.password).all()
                    print(psd)
                    return render_template("table.html", data=psd)

                else:
                    flash('Invalid password!')

        else:
            print('\nThe Entered password is less or greater than 6 and 15 characters.\n')
            flash('Wrong password!')

        return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

# Routing for accessing the Database page
@app.route("/table", methods=['GET', 'POST'])
def fill_table():
    psd = session.query(User).join(User.id, User.username, User.password).all()
    print(psd)
    return render_template("table.html", data=psd)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = ReusableForm(request.form)
    print(form.errors)

    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        server = request.form['email']

        n = len(password)

        if 6 <= n < 15:

            password_scores = {0: 'Horrible', 1: 'Weak', 2: 'Medium', 3: 'Strong'}
            password_strength = dict.fromkeys(['has_upper', 'has_lower', 'has_num'], False)

            if re.search(r'[A-Z]', password):
                password_strength['has_upper'] = True
            if re.search(r'[a-z]', password):
                password_strength['has_lower'] = True
            if re.search(r'[0-9]', password):
                password_strength['has_num'] = True

            score = len([b for b in password_strength.values() if b])

            print('\nThe Entered Password is %s' % password_scores[score])

            if form.validate():
                flash('Thanks for the Registration ' + name)
                if score == 1:
                    print("\n The Password don't contain a Number")
                    flash('Error: The Password do not contain a Number. ')

                if score == 2:
                    print("\n The Password don't contain an Uppercase")
                    flash('Error: The Password do not contain an Uppercase. ')

                if score == 3:
                    print("\n The Password is Strong, you are good to GO....")
                    flash('Great!: The Password is Strong, you are good to GO.... ')

                    print(name, " ", password, " ", server)
            else:
                flash('Error: All the form fields are required. ')

    return render_template('register.html', form=form)


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
    app.run(debug=True, port=4000)
