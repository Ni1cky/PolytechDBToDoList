from flask import Flask
from flask_migrate import Migrate

from routers import *
from store.config import PostgresConfig
from store.postgres import sa

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = PostgresConfig.db_url
app.config["SECRET_KEY"] = "popajopa"

sa.init_app(app)
migrate = Migrate(app, sa)

app.register_blueprint(login_blueprint)
app.register_blueprint(views_blueprint)


@app.teardown_appcontext
def commit_session(exception=None):
    sa.session.commit()


if __name__ == "__main__":
    app.run(debug=True)
