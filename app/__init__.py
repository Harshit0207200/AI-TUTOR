# app/__init__.py

from dotenv import load_dotenv
import os
import yaml
from flask import Flask
from logger import CustomLogger  # Import your custom logger

# ---------------------------------------------------------
# LOAD ENVIRONMENT VARIABLES BEFORE ANY OTHER IMPORTS
# ---------------------------------------------------------
load_dotenv()
print("🔥 __init__.py loaded ENV:", os.getenv("GROQ_API_KEY"))

class AppConfig:
    """Class to handle application configuration."""
    
    def __init__(self):
        self.config = self.load_config()
    
    def load_config(self):
        """Load configuration from config.yaml."""
        with open('config/config.yaml', 'r') as file:
            config = yaml.safe_load(file)
        
        # Replace API key placeholder with actual value from .env
        if 'api' in config and 'key' in config['api']:
            config['api']['key'] = os.getenv('GROQ_API_KEY')  # Or remove if unused
        
        return config


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__, template_folder='templates')

    # Load configuration
    app_config = AppConfig()
    app.config.update(app_config.config)

    # Set up logging
    logger = CustomLogger().get_logger()
    logger.info("Flask application starting...")

    # ---------------------------------------------------------
    # IMPORT ROUTES ONLY AFTER ENVIRONMENT IS LOADED
    # ---------------------------------------------------------
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
