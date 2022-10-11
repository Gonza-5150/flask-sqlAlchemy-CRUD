from flask import Blueprint, render_template

contacts = Blueprint('contacts', __name__)

@contacts.route ("/")
def render():
    return render_template('index.html')

@contacts.route("/new")
def add_contact():
    return "<h3>Saving Contact</h3>"

@contacts.route("/update")
def update():
    return "<h3>update Contact</h3>"

@contacts.route("/delete")
def delete():
    return "<h3>delete Contact</h3>"

@contacts.route ("/about")
def about():
    return render_template('about.html')