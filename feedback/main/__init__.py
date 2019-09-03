from flask import Blueprint
 
bp = Blueprint('main', __name__)

from feedback.main import routes