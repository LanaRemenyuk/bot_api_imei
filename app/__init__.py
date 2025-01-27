from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker

db = SQLAlchemy()

Session = scoped_session(sessionmaker())

def create_app():
    app = Flask(__name__)

    app.config.from_object('app.config.Config')

    db.init_app(app)
    
    with app.app_context():
        from app.routes.imei_routes import api_bp
        app.register_blueprint(api_bp) 
        db.create_all()
    
    return app
