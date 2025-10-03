import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev')
	app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///db.sqlite3')
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', app.config['SECRET_KEY'])

	db.init_app(app)
	jwt.init_app(app)

	# register blueprints
	from .routes.auth import auth_bp
	from .routes.products import products_bp
	from .routes.admin import admin_bp
	from .routes.orders import orders_bp

	app.register_blueprint(auth_bp, url_prefix='/auth')
	app.register_blueprint(products_bp, url_prefix='/products')
	app.register_blueprint(admin_bp, url_prefix='/admin')
	app.register_blueprint(orders_bp, url_prefix='/orders')

	return app