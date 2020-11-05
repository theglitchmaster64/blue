from flask import Blueprint, render_template

blue = Blueprint('blue',__name__,template_folder='templates')

@blue.route('/blue')
def blue():
    return render_template('blue.html')
