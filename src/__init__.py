from flask import Flask

#routes
#from .routes import blablabla

app = Flask(__name__)


def init_app(config):  
    #congiguration
    app.config.from_object(config)
    
    #blueprints
    #app.register_blueprint(blablabla)
    
    return app

