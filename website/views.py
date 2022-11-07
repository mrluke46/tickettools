from flask import Blueprint, render_template

views = Blueprint('views', __name__) # don't have to be the same name as the file name but could be for easier implementation

@views.route('/')
def home():
    return render_template("home.html", version='Version: 0.1.0')

