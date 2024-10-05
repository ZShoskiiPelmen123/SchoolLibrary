from flask import Flask
import sqlalchemy as db
from Models.User import User

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/books')
def books():  # put application's code here
    print(db)
    return 'books World!' #+ db.select(dual)


if __name__ == '__main__':
    app.run()
