from flask import Flask, request
from flask_cors import CORS

from models import setup_db

def create_app(test_config=None):
    # Create and configure the app 
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE, PATCH,OPTIONS')
        return response
    
    @app.route('/')
    def landing_page():
        return "Hello"
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run()