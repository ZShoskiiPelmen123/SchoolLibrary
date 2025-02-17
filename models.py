from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class UserType(db.Model):
    __tablename__ = 'user_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    BookAmount = db.Column(db.Integer, nullable=False, default=0)
    usertype_id = db.Column(db.Integer, db.ForeignKey('user_type.id'))
    usergrade_id = db.Column(db.Integer, db.ForeignKey('user_grade.id'))


class UserGrade(db.Model):
    __tablename__ = 'user_grade'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)


class BookStatus(db.Model):
    __tablename__ = 'book_status'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    info = db.Column(db.Text, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
    bookstatusid = db.Column(db.Integer, db.ForeignKey('book_status.id'), default=1)


class News(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(80), nullable=False)
    text = db.Column(db.String(80), nullable=False)
    https = db.Column(db.String(80), nullable=False)
