from flask import Flask
from config import DevelopmentConfig

def create_app(config=DevelopmentConfig):

    # Crea una instancia de la aplicacion flask
    app = Flask(__name__)

    # Configura la aplicación con la configuración proporcionada 
    app.config.from_object(config)


    # Importa el objeto de la base de datos desde el módulo 'app'
    from app import db

    # Inicializa la base de datos con la aplicación Flask
    db.init_app(app)

    # Importa los blueprints (módulos) de la aplicación
    from app.auth import auth_bp
    from app.main import main_bp
    from app.prediction import prediction_bp

    # Registra los blueprints en la aplicación
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(prediction_bp)

    # Establece la página de inicio por defecto para la ruta '/'
    app.add_url_rule('/', endpoint='index')

    # Devuelve la aplicación configurada
    return app
