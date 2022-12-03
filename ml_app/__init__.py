from flask import Flask , url_for
app = Flask(__name__)
app.config['SECRET_KEY'] = "efc5998af446580ee68ad13fbabcad02"
from ml_app import routes