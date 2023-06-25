from flask import Blueprint, render_template


blueprint = Blueprint('main', __name__, template_folder="templates", static_folder='static')


@blueprint.get('/')
def homepage():
    return render_template("home.html")
