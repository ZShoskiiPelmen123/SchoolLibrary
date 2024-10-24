from flask import Flask
from models import db, UserGrade, UserType, Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()

        usertype1 = UserType(name="Ученик")
        usertype2 = UserType(name="Классный руководитель")
        usertype3 = UserType(name="Библиотекарь")
        db.session.add_all([usertype1, usertype2, usertype3])

        usergrade1 = UserGrade(name="1А")
        usergrade1488 = UserGrade(name="10Т")

        db.session.add_all([usergrade1, usergrade1488])

        book1 = Book(title="Я чувствую", author="Тимечко Глеб", info="Ох, как же он чувствует, год издания: В твоих "
                                                                     "мечтах")
        book2 = Book(title="История этого проекта", author="Тимечко Глеб", info="Это история про Глеба, который "
                                                                                "хорошо писал проект, и про Федю "
                                                                                "который всё это время страдал фигнёй.")
        book3 = Book(title="Преступление и наказание", author="Фёдор Достоевский", info="Хз чё там, пока не читал, "
                                                                                        "зато вам интересно будет")
        db.session.add_all([book1, book2, book3])
        db.session.commit()
