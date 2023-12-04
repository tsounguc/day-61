import os

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField

from login_form import LoginForm

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.secret_key = os.environ.get("secret_key", "Couldn't find secret_key")


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
