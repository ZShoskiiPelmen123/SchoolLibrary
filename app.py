from flask import Flask
from flask import render_template
from models import Book
from models import db
from flask import request
from models import User
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/egg')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/')
def login():
    return render_template('Войти.html')


@app.route('/registration')
def register():
    return render_template('Регистрация.html')


@app.route('/Kvass1488', methods=['POST'])
def confirming1():
    if User.query.filter_by(nickname=request.form['nickname']).first() is None:
        print('user is not defined')
        hashed_password = generate_password_hash(request.form['password'])
        user = User(nickname=request.form['nickname'], name=request.form['name'], last_name=request.form['last_name'],
                    grade=request.form['grade'], password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return('СтраницаФедиЛол.html')
    else:
        print('user already exists')
        return "Пасхалко 1488"


@app.route('/Kvass52')
def confirming2():
    bookshelf = Book.query.all()
    return render_template('СтраницаФедиЛол.html', bookshelf=bookshelf, num=len(bookshelf))


if __name__ == '__main__':
    app.run()
