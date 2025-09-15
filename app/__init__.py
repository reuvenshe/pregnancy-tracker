from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # רישום blueprint
    from .main import main_bp
    app.register_blueprint(main_bp)

    # ✨ יצירת טבלאות אם הן לא קיימות
    with app.app_context():
        db.create_all()

    return app
