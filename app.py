from flask import Flask
from flask_smorest import Api
from db import db
from routes import blp


def create_app():
    app = Flask(__name__, static_folder="static", template_folder="static/templates")

    app.config["API_TITLE"] = "Employee CRUD Example"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/docs"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5430/ss_web_course"

    app.register_error_handler(404, lambda error: ('bad request!', 404))

    db.init_app(app)

    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(blp)

    return app
