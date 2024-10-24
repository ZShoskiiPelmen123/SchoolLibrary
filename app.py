from flask import Flask, render_template, request, session
from flask_login import LoginManager, UserMixin, login_required
from models import db, Book, User, UserType
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = datetime.timedelta(days=30)
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = ''
session['user'] = {'key': 'None'}


@app.route('/egg')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/', methods=['GET'])
def login():
    return render_template('Войти.html', session1=session)


@app.route('/registration')
def register():
    return render_template('Регистрация.html', session1=session)


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
        return render_template('СтраницаФедиЛол.html', session1=session)
    else:
        return "user already exists"


@app.route('/Kvass52', methods=['POST'])
# @login_required
def confirming2():
    user = User.query.filter_by(nickname=request.form['nickname']).first()
    if user is not None:
        hash = generate_password_hash(request.form['password'])
        if check_password_hash(user.password, request.form['password']):
            session['user'] = user.nickname
            bookshelf = Book.query.all()
            return render_template('СтраницаФедиЛол.html', session1=session, bookshelf=bookshelf, num=len(bookshelf))
        else:
            return 'Имя пользователя или пароль указаны неверно'
    else:
        return 'Имя пользователя или пароль указаны неверно'


@app.route('/session/')
def updating_session():
    res = str(session.items())
    return res


if __name__ == '__main__':
    app.run()
