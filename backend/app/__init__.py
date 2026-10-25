import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

from .models import db
from .routes import api

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

    db.init_app(app)
    CORS(app)
    app.register_blueprint(api)

    with app.app_context():
        db.create_all()

    return app