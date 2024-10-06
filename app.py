from flask import Flask
from flask import render_template
import sqlalchemy as db
# from Models.Book import Book
# from Models.User import User
from Models.Test import Test

app = Flask(__name__)


@app.route('/egg')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/books')
def books():  # put application's code here
    print(Test)
    return 'books World!' #+ db.select(dual)


@app.route('/')
def login():
    return render_template('Войти.html')


@app.route('/registration')
def register():
    return render_template('Регистрация.html')


@app.route('/Kvass1488')
def confirming1():
    return render_template('СтраницаФедиЛол.html')


@app.route('/Kvass52')
def confirming2():
    return render_template('СтраницаФедиЛол.html')


if __name__ == '__main__':
    app.run()
