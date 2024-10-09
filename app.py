from flask import Flask
from flask import render_template
# from Models.User import User
from models import Book

app = Flask(__name__)


@app.route('/egg')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/books')
def books():  # put application's code here
    return 'books World!' #+ db.select(dual)


@app.route('/')
def login():
    return render_template('Войти.html')


@app.route('/registration')
def register():
    return render_template('Регистрация.html')


@app.route('/Kvass1488')
def confirming1():
    print('asdsadad')
    bookshelf = Book.query.all()
    return render_template('СтраницаФедиЛол.html', bookshelf=bookshelf)


@app.route('/Kvass52')
def confirming2():
    bookshelf = Book.query.all()
    return render_template('СтраницаФедиЛол.html', bookshelf=bookshelf)


if __name__ == '__main__':
    app.run()
