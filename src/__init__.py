from flask import Flask
from flask import request


def register_blueprint(app: Flask):
    from .web import web
    from .router import router as _router
    app.register_blueprint(web)
    app.register_blueprint(_router.get_blueprint())


def register_middleware(app: Flask):
    @app.before_request
    def before_request():
        print(request.method, request.endpoint)

    from .middlewares.args import args
    app.after_request(args)


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('src.secure')
    app.config.from_object('src.setting')
    register_blueprint(app)
    register_middleware(app)
    return app
