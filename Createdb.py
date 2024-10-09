from flask import Flask
from models import db, User, UserType, Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()

        usertype1 = UserType(name="Классный руководитель")
        usertype2 = UserType(name="Ученик")
        usertype3 = UserType(name="Библиотекарь")
        db.session.add_all([usertype1, usertype2, usertype3])

        book1 = Book(title="title", author="author", info="info")
        book2 = Book(title="another title", author="another author", info="another info")
        book3 = Book(title="third title", author="third author", info="third info")
        db.session.add_all([book1, book2, book3])
        db.session.commit()
