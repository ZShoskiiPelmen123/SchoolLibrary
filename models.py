from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class UserType(db.Model):
    __tablename__ = 'user_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    usertype_id = db.Column(db.Integer, db.ForeignKey('user_type.id'))


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    info = db.Column(db.Text, nullable=False)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
