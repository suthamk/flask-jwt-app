import os

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_jwt_extended import JWTManager

load_dotenv()

from models import bcrypt, db

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "super-secret-key")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://root:@127.0.0.1:3306/flask_jwt_app?charset=utf8mb4",
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
jwt = JWTManager(app)
bcrypt.init_app(app)

with app.app_context():
    db.create_all()

from routes.auth import auth_bp

app.register_blueprint(auth_bp, url_prefix="/auth")


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
