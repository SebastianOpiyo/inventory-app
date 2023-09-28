# Flask API
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle://username:password@localhost:xe'  # Replace with your Oracle connection details
db = SQLAlchemy(app)

from api import routes
