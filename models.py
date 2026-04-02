from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)


def create_user(username, password):
    if User.query.filter_by(username=username).first():
        return False
    hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")
    user = User(username=username, password_hash=hashed_pw)
    db.session.add(user)
    db.session.commit()
    return True


def verify_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password_hash, password):
        return True
    return False
