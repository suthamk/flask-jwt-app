from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from models import bcrypt

app = Flask(__name__)

# Secret key (CHANGE THIS in production)
app.config["JWT_SECRET_KEY"] = "super-secret-key"

jwt = JWTManager(app)
bcrypt.init_app(app)

from routes.auth import auth_bp
app.register_blueprint(auth_bp, url_prefix="/auth")

@app.route("/")
def index():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)