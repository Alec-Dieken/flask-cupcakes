from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = "0fedef89556952b5478fd3e883c77301"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user123:password123@localhost:5432/cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from flask_cupcakes import routes