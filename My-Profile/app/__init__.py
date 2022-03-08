from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()
db = SQLAlchemy()



# Initializing application

def create_app(config_name):
    app = Flask(__name__)
    
    app.config.from_object(config_options[config_name])
 #...
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    #....

    # ....

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    
    
    return app

    # ...

