from flask import Flask
from config import DevelopmentConfig

def create_app(config=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config)

    from app import db

    db.init_app(app)

    from app.auth import auth_bp
    from app.main import main_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    # Establecer la página de inicio por defecto
    app.add_url_rule('/', endpoint='index')


    return app
