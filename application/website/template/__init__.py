from flask import Flask
def create_app():
    app =Flask(__name__)
    app.config['Secrete_key']='xyz'
    return app