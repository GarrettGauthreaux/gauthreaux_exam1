from flask import Flask

def create_app():
    app = Flask(__name__)

    # This import is at the bottom of the function to avoid circular imports
    from app import routes

    return app