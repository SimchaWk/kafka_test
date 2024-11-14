from flask import Flask

from app.psql_db.connection import create_tables_if_not_exist
from app.routes.queries_route import queries_bp
from app.routes.receive_data_route import receive_data_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(receive_data_bp, url_prefix='/api')
    app.register_blueprint(queries_bp, url_prefix='/api')
    return app


if __name__ == '__main__':
    create_tables_if_not_exist()
    app = create_app()
    app.run()
