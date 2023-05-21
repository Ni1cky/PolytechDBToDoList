from flask import Flask, render_template, session, redirect
from flask_migrate import Migrate

from routers import login_blueprint
from store.config import PostgresConfig
from store.postgres import sa

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = PostgresConfig.db_url
app.config["SECRET_KEY"] = "popajopa"

sa.init_app(app)
migrate = Migrate(app, sa)

app.register_blueprint(login_blueprint)


@app.teardown_appcontext
def commit_session(exception=None):
    sa.session.commit()


@app.route("/")
def hello():
    if session["user"]:
        return redirect("/home")
    return render_template("login.html")


@app.route("/home")
def home():
    return render_template("home.html", user_id=session["user"])


if __name__ == "__main__":
    app.run(debug=True)
