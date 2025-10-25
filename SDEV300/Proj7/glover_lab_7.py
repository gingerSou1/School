"""
__filename__ = "glover_lab_7.py"
__coursename__ = "SDEV 300 - Building Secure Python Applications"
__author__ = "Corey Glover"
__copyright__ = "None"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Corey Glover"
__email__ = "cglover35@student.umgc.edu"

Site hosted off URL for http://localhost:8080/glover_lab_7)
"""
import functools
import secrets
from datetime import datetime
import re
import csv
from passlib.hash import sha256_crypt
from flask import Flask, render_template, request, redirect, session, url_for
from flask_login import LoginManager
from requests import Session

APP = Flask(__name__, static_url_path="/static")
login_manager = LoginManager()
login_manager.init_app(APP)
login_manager.login_view = 'login'

APP.config['SESSION_PERMANENT'] = False
APP.config['SESSION_TYPE'] = 'filesystem'
APP.config['SECRET_KEY'] = secrets.token_hex(16)
Session()

TIME_NOW = datetime.now()
DATE_TIME = TIME_NOW.strftime("%B %d, %Y, %H:%M:%S")


@login_manager.user_loader
def load_user(user_name):
    """function for login manager"""
    return user_name

# @login_manager.unauthorized_handler
# def handle_needs_login():
#     flash("Login Successful.")
#     next = url_for(request.endpoint, **request.view_args)
#     return redirect(url_for('login', next=next))


def login_required(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if "email" not in session:
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)
    return secure_function


def user_exists():
    """Function to check if user already exists"""
    with open('userRegister.csv', 'r') as read_file:
        email = request.form['user_email']
        file_read = csv.reader(read_file)
        file_array = list(file_read)
        for a_email in file_array:
            if email in a_email[2]:
                error_msg = "User email already registered. Please login."
            return render_template('/lab7_register.html', error=error_msg)


@APP.route('/lab7_register.html', methods=['GET', 'POST'])
def user_register():
    """Function to register user"""
    success = False
    error_msg = None
    if request.method == 'POST':
        with open('userRegister.csv', 'w') as in_file:
            verify_email = r'\b[A-Z a-z 0-9._%+-]+@[A-Z a-z 0-9.-]' \
                           r'+\.[A-Z|a-z]{2,}\b'
            verify_first_name = r'^[a-z\'A-Z]{2,30}$.*'
            verify_last_name = r'^[a-z\'A-Z]+(-[a-zA-Z]+)?$'
            verify_password = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*' \
                              r'[@$!%*#?&])[A-Za-z\d@$!#%*?&]{12,256}$'
            if re.fullmatch(verify_password, request.form['password']):
                if re.fullmatch(verify_first_name, request.form['first_name']):
                    if re.fullmatch(verify_last_name, request.form
                    ['last_name']):
                        if re.fullmatch(verify_email, request.form
                        ['user_email']):
                            user_exists()
                            if request.form['password'] == \
                                    request.form['repass']:
                                password = request.form['password']
                                sha256_crypt.hash(password)
                                field_names = ['user_name', 'password',
                                               'user_email', 'first_name',
                                               'last_name']
                                writer = csv.DictWriter(in_file, fieldnames=
                                field_names, delimiter=",")
                                writer.writerow({'user_name': request.form
                                ['user_name'], 'user_email': request.form
                                ['user_email'], 'password': request.form
                                ['password'], 'first_name': request.form
                                ['first_name'], 'last_name': request.form
                                ['last_name']})
                                success = True
                            else:
                                error_msg = "Passwords do not match. " \
                                            "Try again."
                        else:
                            error_msg = "Verify email format. Try again."
                    else:
                        error_msg = "Verify Last Name. Try again."
                else:
                    error_msg = "Verify First Name. Try again."
            else:
                error_msg = "Password must be at least 12 characters, " \
                            "1 uppercase, 1 lowercase, 1 number, and " \
                            "1 special character."
    if success is True and error_msg is None:
        return redirect("login_land.html")
    return render_template('lab7_register.html', error_msg=error_msg)


@APP.route('/lab7_login.html', methods=['GET', 'POST'])
def login():
    """Function to login"""
    login_error = None
    if request.method == 'POST':
        user = request.form['user_name']
        password = request.form['password']
        # next_url = request.form.get("next")
        with open('userRegister.csv', 'r') as read_file:
            if user == '' or password == '':
                login_error = "Field cannot be blank."
            else:
                file_read = csv.reader(read_file)
                file_array = list(file_read)
                for a_user in file_array:
                    if user in a_user[0] or password in a_user[1]:
                        session["user"] = user
                        # if next_url:
                        #     return redirect(next_url)
                        # return redirect('lab7_register.html')
                        return render_template('login_land.html')
                    else:
                        login_error = 'Please check login credentials ' \
                                        'and try again.'
                        raise IndexError
    return render_template('/lab7_login.html', error=login_error)


@APP.route('/')
@APP.route('/lab7_web.html')
def main():
    """ Main function """
    return render_template('lab7_web.html', datetime=DATE_TIME)


@APP.route('/lab7_1.html')
# @login_required
def page_2():
    """ Function to call second page in HTML"""
    return render_template('lab7_1.html', datetime=DATE_TIME)


@APP.route('/lab7_2.html')
# @login_required
def page_3():
    """ Function to call third page in HTML"""
    return render_template('lab7_2.html', datetime=DATE_TIME)


@APP.route('/login_land.html')
@login_required
def page_4():
    """Function to call landing page in HTML"""
    return render_template('login_land.html', datetime=DATE_TIME)


if __name__ == "__main__":
    APP.run(host='127.0.0.1', port=8080, debug=True)
