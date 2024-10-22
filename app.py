from flask import Flask, render_template, request, session
from models import db, Book, User, UserType
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
        usertype = UserType.query.filter_by(name=request.form['userType']).first()
        hashed_password = generate_password_hash(request.form['password'])
        user = User(nickname=request.form['nickname'], name=request.form['name'], last_name=request.form['last_name'],
                    grade=request.form['grade'], password=hashed_password, usertype_id=usertype.id)
        db.session.add(user)
        db.session.commit()
        bookshelf = Book.query.all()
        return render_template('СтраницаФедиЛол.html', bookshelf=bookshelf, num=len(bookshelf))
    else:
        return "user already exists"


@app.route('/Kvass52', methods=['POST'])
def confirming2():
    user = User.query.filter_by(nickname=request.form['nickname']).first()
    if user is not None:
        hash = generate_password_hash(request.form['password'])
        if check_password_hash(user.password, request.form['password']):
            bookshelf = Book.query.all()
            return render_template('СтраницаФедиЛол.html', bookshelf=bookshelf, num=len(bookshelf))
        else:
            return 'Имя пользователя или пароль указаны неверно'
    else:
        return 'Имя пользователя или пароль указаны неверно'


if __name__ == '__main__':
    app.run()
