from flask import Flask, render_template, request, jsonify, redirect
from models import db, Book, User, UserType, UserGrade
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from sqlalchemy import and_, or_

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

theme = 'white'
authType = {'userTypeId': 0, 'userId': 0}

def check_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if authType['userTypeId'] == 0:
            return redirect('/')
        return f(*args, **kwargs)
    return decorated_function


@app.route('/getTheme', methods=['GET'])
def get_theme():
    return {'newTheme': theme}


@app.route('/setTheme', methods=['POST'])
def set_theme():
    global theme
    theme = request.json['newTheme']
    return jsonify(success=True)


@app.route('/')
def login():
    return render_template('Войти.html')


@app.route('/profile')
@check_auth
def profile():
    global authType
    get_userinfo()
    return render_template('index.html', authType=authType)


@app.route('/getKlass', methods=['GET'])
@check_auth
def getKlass():
    studList = getStudentsByTeacher()
    print(*studList)
    result = []
    for i in studList:
        temp = getBooksByStudent(i.id)
        books = []
        for j in temp:
            books.append({"author": j.author, "title": j.title})
        # books["books_count"] = str(len(temp))
        result.append({'name': i.name, 'last_name': i.last_name, 'books': books, "books_count": len(temp)})
    return result


@app.route('/registration')
def register():
    KvassInfinity = UserGrade.query.all()
    KvassMnogo = UserType.query.all()
    return render_template('Регистрация.html', KvassMnogo=KvassMnogo, KvassInfinity=KvassInfinity)


# регистрация
@app.route('/Kvass1488', methods=['GET', 'POST'])
def confirming1():
    global authType
    if request.method == 'POST':
        if User.query.filter_by(nickname=request.form['nickname']).first() is None:
            usertype = UserType.query.filter_by(name=request.form['userTypeId']).first()
            usergrade = UserGrade.query.filter_by(name=request.form['userGrade']).first()
            hashed_password = generate_password_hash(request.form['password'])
            user = User(nickname=request.form['nickname'], name=request.form['name'],
                        last_name=request.form['last_name'], password=hashed_password, usertype_id=usertype.id,
                        usergrade_id=usergrade.id)
            db.session.add(user)
            db.session.commit()
            bookshelf = Book.query.all()
            authType['userTypeId'] = user.usertype_id
            authType['userId'] = user.id
            return render_template('СтраницаФедиЛол.html', bookshelf=bookshelf, num=len(bookshelf))
        else:
            return "user already exists"
    if request.method == 'GET':
        return "кто ты?"


@app.route('/getMyBooks')
@check_auth
def getMyBooks():
    return getBooksByStudent(authType['userId'])


def getStudentsByTeacher():
    teacher = User.query.filter_by(id=authType['userId'], usertype_id=authType['userTypeId']).first()
    if teacher is None:
        return {}
    else:
        return User.query.filter_by(usergrade_id=teacher.usergrade_id, usertype_id=1)


def getBooksByStudent(stud_id):
    books = Book.query.filter_by(userid=stud_id).all()
    if books is None:
        return {}
    return books


def get_userinfo():
    user = User.query.filter_by(id=authType['userId'], usertype_id=authType['userTypeId']).first()
    if user is not None:
        authType['first_name'] = user.name
        authType['last_name'] = user.last_name
        authType['grade'] = UserGrade.query.filter_by(id=user.usergrade_id).first().name


@app.route('/bb', methods=['POST'])
def bb():
    book_id = request.json['book_id']
    print(book_id)
    if request.method == "POST":
        book = Book.query.filter_by(id=book_id).first()
        if book is None:
            return jsonify(error='Книга не найдена'), 400
        elif book.userid is not None:
            return jsonify(error='Книга уже взята'), 400
        book.userid = authType['userId']
        db.session.commit()
    return jsonify(success=True)


@app.route('/Kvass52', methods=['POST'])
def confirming2():
    if request.method == "POST":
        global authType
        user = User.query.filter_by(nickname=request.form['nickname']).first()
        if user is not None:
            hash = generate_password_hash(request.form['password'])
            if check_password_hash(user.password, request.form['password']):
                bookshelf = Book.query.all()
                authType['userTypeId'] = user.usertype_id
                authType['userId'] = user.id
                return render_template('СтраницаФедиЛол.html', bookshelf=bookshelf, num=len(bookshelf))
            else:
                return 'Имя пользователя или пароль указаны неверно'
        else:
            return 'Имя пользователя или пароль указаны неверно'


@app.route('/Kvass52', methods=['GET'])
@check_auth
def confirming2get():
    if request.method == "GET":
        bookshelf = Book.query.all()
        return render_template('СтраницаФедиЛол.html', bookshelf=bookshelf, num=len(bookshelf))


@app.route('/Kvass53', methods=['GET'])
def logout():
    print(authType)
    if request.method == "GET":
        authType['userTypeId'] = 0
        authType['userId'] = 0
        return render_template('Войти.html')


@app.route('/searchBook', methods=['GET'])
@check_auth
def search_book():
    st = request.args.get('searchText')
    st = '%{}%'.format(st)
    books = []
    if request.method == 'GET':
        books = Book.query.filter(or_(Book.title.like(st), Book.author.like(st), Book.info.like(st))).all()
        return render_template('СтраницаФедиЛол.html', bookshelf=books, num=len(books))


if __name__ == '__main__':
    app.run()
