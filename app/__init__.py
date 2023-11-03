from flask import Flask
from config import DevelopmentConfig

def create_app(config=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config)

    from app import db

    # Inicia la base de datos
    db.init_app(app)

    from app.auth import auth_bp
    from app.main import main_bp
    from app.prediction import prediction_bp

    # Creacion de blueprint
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(prediction_bp)

    # Establecer la pagina de inicio por defecto
    app.add_url_rule('/', endpoint='index')


    return app
