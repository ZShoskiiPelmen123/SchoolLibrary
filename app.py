from flask import Flask, render_template, request, jsonify, redirect
from models import db, Book, User, UserType, UserGrade
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

theme = 'white'
authType = {'userType': 0, 'userId': 0}





def check_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if authType['userType'] == 0:
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


@app.route('/egg')
def hello_world():  # put application's code here
    bookList = getBooksByStudent(getStudentsByTeacher('uuuuuuu')[0].nickname)
    print(*[a.title for a in bookList])
    return 'Hello World!'


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
    studList = getStudentsByTeacher('dinosaur_hunter')  # FIXME: заменить на динамичное получение ID учителя
    result = []
    for i in studList:
        temp = getBooksByStudent(i.nickname)
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


@app.route('/Kvass1488', methods=['GET', 'POST'])
def confirming1():
    global authType
    if request.method == 'POST':
        if User.query.filter_by(nickname=request.form['nickname']).first() is None:
            usertype = UserType.query.filter_by(name=request.form['userType']).first()
            usergrade = UserGrade.query.filter_by(name=request.form['userGrade']).first()
            hashed_password = generate_password_hash(request.form['password'])
            user = User(nickname=request.form['nickname'], name=request.form['name'],
                        last_name=request.form['last_name'], password=hashed_password, usertype_id=usertype.id,
                        usergrade_id=usergrade.id)
            db.session.add(user)
            db.session.commit()
            bookshelf = Book.query.all()
            authType['userType'] = user.usertype_id
            authType['userId'] = user.id
            return render_template('СтраницаФедиЛол.html', bookshelf=bookshelf, num=len(bookshelf))
        else:
            return "user already exists"
    if request.method == 'GET':
        return "кто ты?"


def getStudentsByTeacher(teacher):
    teacher = User.query.filter_by(nickname=teacher, usertype_id=2).first()
    if teacher is None:
        return {}
    else:
        return User.query.filter_by(usergrade_id=teacher.usergrade_id, usertype_id=1)


def getBooksByStudent(stud_nickname):
    stud_nickname = User.query.filter_by(nickname=stud_nickname, usertype_id=1).first()
    if stud_nickname is None:
        return {}
    else:
        return Book.query.filter_by(userid=stud_nickname.id).all()


def get_userinfo():
    user = User.query.filter_by(id=authType['userId'], usertype_id=authType['userType']).first()
    print(user)
    if user is not None:
        authType['first_name'] = user.name
        authType['last_name'] = user.last_name
        authType['grade'] = "test"


@app.route('/Kvass52', methods=['POST'])
def confirming2():
    if request.method == "POST":
        global authType
        user = User.query.filter_by(nickname=request.form['nickname']).first()
        if user is not None:
            hash = generate_password_hash(request.form['password'])
            if check_password_hash(user.password, request.form['password']):
                bookshelf = Book.query.all()
                authType['userType'] = user.usertype_id
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
        return render_template('СтраницаФедиЛол.html')


@app.route('/Kvass53', methods=['GET'])
def logout():
    print(authType)
    if request.method == "GET":
        authType['userType'] = 0
        authType['userId'] = 0
        return render_template('Войти.html')


if __name__ == '__main__':
    app.run()
