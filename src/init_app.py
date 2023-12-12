from decouple import config

from flask import Flask, render_template
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS

# Routes
from src.routes.schedule import schedule_bp

# Database
from src.models.models import db

SECRET_KEY = config('SECRET_KEY')

def init_app():
    """
    This is the factory function that creates the Flask app.
    """
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////temp/luegopago.db'
    app.config['SECRET_KEY'] = SECRET_KEY

    CORS(app)
    db.init_app(app)

    # Blueprints
    app.register_blueprint(schedule_bp)

    # Swagger
    SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
    API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)

    # Call factory function to create our blueprint
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
        API_URL,
        config={  # Swagger UI config overrides
            'app_name': "Luegopago"
        },
    )

    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    
    # Root endpoint
    @app.route("/")
    def index():
        """
        This is the root endpoint of the API.
        ---
        parameters:
        - None
        responses:
        200:
            description: The root endpoint of the API.
        """
        return render_template("index.html")

    return app