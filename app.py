from flask import Flask
from flask_jwt_extended import JWTManager

app = Flask(__name__)

# Secret key (CHANGE THIS in production)
app.config["JWT_SECRET_KEY"] = "super-secret-key"

jwt = JWTManager(app)

from routes.auth import auth_bp
app.register_blueprint(auth_bp, url_prefix="/auth")

if __name__ == "__main__":
    app.run(debug=True)