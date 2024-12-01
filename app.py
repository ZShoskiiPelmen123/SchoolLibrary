from flask import Flask, render_template, request, jsonify, redirect
from models import db, Book, User, UserType, UserGrade, BookStatus
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
    print("studList", studList)
    result = []
    for i in studList:
        temp = getBooksByStudent(i.id)
        books = []
        for j in temp:
            books.append({"author": j['author'], "title": j['title']})
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
            usertype = UserType.query.filter_by(id=request.form['userTypeId']).first()
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
            return render_template('СтраницаФедиЛол.html', bookshelf=bookshelf, num=len(bookshelf), authType=authType)
        else:
            return "user already exists"
    if request.method == 'GET':
        return "кто ты?"


@app.route('/getMyBooks')
@check_auth
def getMyBooks():
    response = jsonify()
    response.status_code = 200
    return getBooksByStudent(authType['userId'])


def getStudentsByTeacher():
    teacher = User.query.filter_by(id=authType['userId'], usertype_id=authType['userTypeId']).first()
    if teacher is None:
        return {}
    else:
        return User.query.filter_by(usergrade_id=teacher.usergrade_id, usertype_id=1).all()


def getBooksByStudent(stud_id):
    result = []
    books = Book.query.filter_by(userid=stud_id, bookstatusid=3).all()
    for i in books:
        result.append({'title': i.title, 'author': i.author, 'info': i.info})
    return result


def get_userinfo():
    user = User.query.filter_by(id=authType['userId'], usertype_id=authType['userTypeId']).first()
    if user is not None:
        authType['first_name'] = user.name
        authType['last_name'] = user.last_name
        authType['grade'] = UserGrade.query.filter_by(id=user.usergrade_id).first().name


# бронирование книги
@app.route('/bb', methods=['POST'])
@check_auth
def bb():
    book_id = request.json['book_id']
    if request.method == "POST":
        book = Book.query.filter_by(id=book_id).first()
        if book is None:
            return jsonify(error='Книга не найдена'), 400
        elif book.userid is not None:
            return jsonify(error='Книга уже взята'), 400
        book.userid = authType['userId']
        book.bookstatusid = 2
        db.session.commit()
    return jsonify(success=True)


# отмена бронирования книги
@app.route('/cb', methods=['POST'])
@check_auth
def cb():
    book_id = request.json['book_id']
    if request.method == "POST":
        book = Book.query.filter_by(id=book_id, userid=authType['userId']).first()
        if book is None:
            return jsonify(error='Книга не найдена'), 400
        book.userid = None
        book.bookstatusid = 1
        db.session.commit()
    return jsonify(success=True)


# выдать книгу (только для библиотекаря)
@app.route('/gb', methods=['POST'])
@check_auth
def gb():
    if authType['userTypeId'] == 3:
        book_id = request.json['book_id']
        if request.method == "POST":
            book = Book.query.filter_by(id=book_id).first()
            if book is None:
                return jsonify(error='Книга не найдена'), 400
            book.bookstatusid = 3
            db.session.commit()
        return jsonify(success=True)
    else:
        return None


# взять книгу, то есть сдать книгу, то есть принять книгу (только для библиотекаря)
@app.route('/tb', methods=['POST'])
@check_auth
def tb():
    if authType['userTypeId'] == 3:
        book_id = request.json['book_id']
        if request.method == "POST":
            book = Book.query.filter_by(id=book_id).first()
            if book is None:
                return jsonify(error='Книга не найдена'), 400
            book.userid = None
            book.bookstatusid = 1
            db.session.commit()
        return jsonify(success=True)
    else:
        return None


@app.route('/getCurrentUserId', methods=['GET'])
@check_auth
def get_current_user_id():
    return authType, 200


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
                return render_template('СтраницаФедиЛол.html', bookshelf=bookshelf, num=len(bookshelf), authType=authType)
            else:
                return 'Имя пользователя или пароль указаны неверно'
        else:
            return 'Имя пользователя или пароль указаны неверно'


@app.route('/Kvass52', methods=['GET'])
@check_auth
def confirming2get():
    if request.method == "GET":
        bookshelf = Book.query.all()
        return render_template('СтраницаФедиЛол.html', bookshelf=bookshelf, num=len(bookshelf), authType=authType)


@app.route('/Kvass53', methods=['GET'])
def logout():
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
        return render_template('СтраницаФедиЛол.html', bookshelf=books, num=len(books), authType=authType)


if __name__ == '__main__':
    app.run()
