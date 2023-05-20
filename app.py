from flask import Flask
from flask_migrate import Migrate

from store.config import PostgresConfig
from store.postgres import sa

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = PostgresConfig.db_url

sa.init_app(app)
migrate = Migrate(app, sa)


@app.teardown_appcontext
def commit_session(exception=None):
    sa.session.commit()


@app.route("/")
def hello_world():
    return f'''
    Hello world!
    '''


if __name__ == "__main__":
    app.run(debug=True)
