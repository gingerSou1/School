"""
__filename__ = "glover_lab_6.py"
__coursename__ = "SDEV 300 - Building Secure Python Applications"
__author__ = "Corey Glover"
__copyright__ = "None"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Corey Glover"
__email__ = "cglover35@student.umgc.edu"

Site hosted off URL for http://localhost:8080/glover_lab_6)
"""
from datetime import datetime
from flask import Flask, render_template

APP = Flask(__name__, static_url_path="/static")

TIME_NOW = datetime.now()
DATE_TIME = TIME_NOW.strftime("%B %d, %Y, %H:%M:%S")


@APP.route('/glover_lab_6')
def main():
    """ Main function - uses HTML template to draw page """
    return render_template('lab6_web.html', datetime=DATE_TIME)


@APP.route('/lab_6_1.html')
def page_2():
    """ Function to call second page in HTML"""
    return render_template('lab_6_1.html', datetime=DATE_TIME)


@APP.route('/lab_6_2.html')
def page_3():
    """ Function to call third page in HTML"""
    return render_template('lab_6_2.html', datetime=DATE_TIME)


if __name__ == "__main__":
    APP.run(host='127.0.0.1', port=8080, debug=True)
