from flask import Flask
from .extensions import ma
from .models import db
from .blueprints.members import members_bp
from .blueprints.books import books_bp
from .blueprints.loans import loans_bp

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name}')

    #initialize extensions
    ma.init_app(app)
    db.init_app(app)

    #Register Blueprints
    app.register_blueprint(members_bp, url_prefix='/members')
    app.register_blueprint(books_bp, url_prefix="/books")
    app.register_blueprint(loans_bp, url_prefix="/loans")


    return app