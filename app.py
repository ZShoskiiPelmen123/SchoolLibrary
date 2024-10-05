from flask import Flask
import sqlalchemy as db
# from Models.Book import Book
# from Models.User import User
from Models.Test import Test

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/books')
def books():  # put application's code here
    print(Test)
    return 'books World!' #+ db.select(dual)


if __name__ == '__main__':
    app.run()
