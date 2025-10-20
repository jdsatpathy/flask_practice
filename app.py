from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import DecimalField, RadioField, SelectField, TextAreaField, FileField
from wtforms.validators import InputRequired
from werkzeug.security import generate_password_hash
import traceback
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


class MyForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    submit = SubmitField('Submit', validators=None)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form_page')
def form_page():
    form = MyForm()
    return render_template('form.html', form=form)


@app.route('/form_submit', methods=['GET', 'POST'])
def on_form_submit():
    form = MyForm()

    if form.validate_on_submit():
        return render_template('form_result.html', form=form)



@app.route('/link1')
def link1():
    return {"a": "apple", "b": "ball", "c": "cat"}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
