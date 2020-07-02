#!python
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL, MySQLdb
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, SelectField, SubmitField, HiddenField
from passlib.hash import sha256_crypt
from functools import wraps
from flask_uploads import UploadSet, configure_uploads, IMAGES
import timeit
import datetime
from flask_mail import Mail, Message
import os
from wtforms.fields.html5 import EmailField

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['UPLOADED_PHOTOS_DEST'] = 'static/image/product'
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

# Config MySQL
mysql = MySQL()
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1288zpmqal'
app.config['MYSQL_DB'] = 'menshut'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Initialize the app for use with this MySQL class
mysql.init_app(app)


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, *kwargs)
        else:
            return redirect(url_for('login'))

    return wrap

def not_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return redirect(url_for('index'))
        else:
            return f(*args, *kwargs)

    return wrap

def is_admin_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'admin_logged_in' in session:
            return f(*args, *kwargs)
        else:
            return redirect(url_for('admin_login'))

    return wrap

def not_admin_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'admin_logged_in' in session:
            return redirect(url_for('admin'))
        else:
            return f(*args, *kwargs)

    return wrap

def wrappers(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)

    return wrapped

def content_based_filtering(product_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, pName, price, description, available, category, item, pCode, picture, date FROM products WHERE id=%s", (product_id,))  # getting id row
    data = cur.fetchone()  # get row info
    data_cat = data['category']  # get id category ex shirt
    print('Showing result for Product Id: ' + product_id)
    category_matched = cur.execute("SELECT * FROM products WHERE category=%s", (data_cat,))  # get all shirt category
    print('Total product matched: ' + str(category_matched))
    cat_product = cur.fetchall()  # get all row
    cur.execute("SELECT * FROM product_level WHERE product_id=%s", (product_id,))  # id level info
    id_level = cur.fetchone()
    recommend_id = []
    cate_level = ['v_shape', 'polo', 'clean_text', 'design', 'leather', 'color', 'formal', 'converse', 'loafer', 'hook',
                  'chain']
    for product_f in cat_product:
        cur.execute("SELECT * FROM product_level WHERE product_id=%s", (product_f['id'],))
        f_level = cur.fetchone()
        match_score = 0
        if f_level['product_id'] != int(product_id):
            for cat_level in cate_level:
                if f_level[cat_level] == id_level[cat_level]:
                    match_score += 1
            if match_score == 11:
                recommend_id.append(f_level['product_id'])
    print('Total recommendation found: ' + str(recommend_id))
    if recommend_id:
        cur = mysql.connection.cursor()
        placeholders = ','.join((str(n) for n in recommend_id))
        query = 'SELECT * FROM products WHERE id IN (%s)' % placeholders
        cur.execute(query)
        recommend_list = cur.fetchall()
        return recommend_list, recommend_id, category_matched, product_id
    else:
        return ''

@app.route('/')
def home():
    return render_template('home.html')


class LoginForm(Form):  # Create Login Form
    email = EmailField('', [validators.DataRequired(), validators.Email(), validators.length(min=4, max=25)],
                       render_kw={'placeholder': 'Email'})
    password = PasswordField('', [validators.length(min=3)],
                             render_kw={'placeholder': 'Password'})

# User Login
@app.route('/login', methods=['GET', 'POST'])
@not_logged_in
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        # GEt user form
        email = form.email.data
        # password_candidate = request.form['password']
        password_candidate = form.password.data

        # Create cursor
        cur = mysql.connection.cursor()

        # Get user by username
        result = cur.execute("SELECT * FROM users WHERE email=%s", [email])

        if result > 0:
            # Get stored value
            data = cur.fetchone()
            password = data['password']
            uid = data['id']
            name = data['username']

            # Compare password
            if sha256_crypt.verify(password_candidate, password):
                # passed
                session['logged_in'] = True
                session['uid'] = uid
                session['s_name'] = name
                x = '1'
                cur.execute("UPDATE users SET online=%s WHERE id=%s", (x, uid))

                return redirect(url_for('home'))

            else:
                flash('Incorrect password', 'danger')
                return render_template('login.html', form=form)

        else:
            flash('Username not found', 'danger')
            # Close connection
            cur.close()
            return render_template('login.html', form=form)
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    if 'uid' in session:
        # Create cursor
        cur = mysql.connection.cursor()
        uid = session['uid']
        x = '0'
        cur.execute("UPDATE users SET online=%s WHERE id=%s", (x, uid))
        session.clear()
        flash('You are logged out', 'success')
        return redirect(url_for('home'))
    return redirect(url_for('login'))

class RegisterForm(Form):
    username = StringField('', [validators.length(min=3, max=50)],
                       render_kw={'autofocus': True, 'placeholder': 'Full Name'})
    email = EmailField('', [validators.DataRequired(), validators.Email(), validators.length(min=4, max=25)],
                       render_kw={'placeholder': 'Email'})
    password = PasswordField('', [validators.length(min=3)],
                             render_kw={'placeholder': 'Password'})
    rmobile1 = StringField('', [validators.length(min=3, max=3)],
                       render_kw={'autofocus': True})
    rmobile2 = StringField('', [validators.length(min=3, max=4)],
                       render_kw={'autofocus': True})
    rmobile3 = StringField('', [validators.length(min=3, max=4)],
                       render_kw={'autofocus': True})


@app.route('/register', methods=['GET', 'POST'])
@not_logged_in
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(str(form.password.data))
        rmobile1 = form.rmobile1.data
        rmobile2 = form.rmobile2.data
        rmobile3 = form.rmobile3.data

        # Create Cursor
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(username, email, password, rmobile1, rmobile2, rmobile3) VALUES(%s, %s, %s, %s, %s, %s)",
                    (username, email, password, rmobile1, rmobile2, rmobile3,))
        cur.execute("INSERT INTO buy_product2(ofname, username, rmobile1, rmobile2, rmobile3) VALUES(%s, %s, %s, %s, %s)",
                    (username, username, rmobile1, rmobile2, rmobile3,))

        # Commit cursor
        mysql.connection.commit()

        # Close Connection
        cur.close()

        flash('You are now registered and can login', 'success')

        return redirect(url_for('home'))
    return render_template('register.html', form=form)

class HelpForm(Form):
    selec = StringField('', [validators.length(min=3, max=3)],render_kw={'autofocus': True})
    name = StringField('', [validators.length(min=3, max=10)],render_kw={'autofocus': True})
    phone = StringField('', [validators.length(min=3, max=3)],render_kw={'autofocus': True})
    email = StringField('', [validators.length(min=3, max=4)],render_kw={'autofocus': True})
    title = StringField('', [validators.length(min=3, max=4)],render_kw={'autofocus': True})
    contents = TextAreaField('', [validators.length(min=0, max=300)],render_kw={'autofocus': True})

@app.route('/help', methods=['GET','POST'])
def help():
    form = HelpForm(request.form)
    selec = form.selec.data
    name = form.name.data
    phone = form.phone.data
    email = form.email.data
    title = form.title.data
    contents = form.contents.data
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO help(selec,name,phone,email,title,contents) VALUES (%s,%s,%s,%s,%s,%s)', (selec,name,phone,email,title,contents,))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('home'))
    return render_template('help.html')

class DeleteForm(Form):
    delete = SubmitField('Delete')

@app.route('/carts', methods=["GET","POST"])
def carts():
    if 'uid' in session:
        form = DeleteForm(request.form)
        uid = session['uid']
        ofname = session['s_name']
        cur = mysql.connection.cursor()
        order_rows = cur.execute("SELECT * FROM orders WHERE uid=%s", (uid,))
        cur.execute('DROP TABLE IF EXISTS uorders')
        cur.execute('CREATE TABLE uorders SELECT uid,ofname,pid,quantity,dstatus,odate,ddate,pName,price,condi FROM orders WHERE uid=%s', (uid,))
        cur.execute('ALTER TABLE uorders ADD COLUMN id INT NOT NULL AUTO_INCREMENT PRIMARY KEY')
        cur.execute('SELECT * FROM uorders')
        result = cur.fetchall()
        cur.execute('SELECT id,pid,pName,price,quantity,uid,condi,(price*quantity) AS total_price FROM uorders')
        row = cur.fetchall()
        cur.execute('SELECT id,pid,pName,price,quantity,uid,condi,(price*quantity) AS total_price FROM uorders WHERE id=1')
        row1 = cur.fetchall()
        cur.execute('SELECT id,pid,pName,price,quantity,uid,condi,(price*quantity) AS total_price FROM uorders WHERE id=2')
        row2 = cur.fetchall()
        cur.execute('SELECT id,pid,pName,price,quantity,uid,condi,(price*quantity) AS total_price FROM uorders WHERE id=3')
        row3 = cur.fetchall()
        cur.execute('SELECT id,pid,pName,price,quantity,uid,condi,(price*quantity) AS total_price FROM uorders WHERE id=4')
        row4 = cur.fetchall()
        cur.execute('SELECT id,pid,pName,price,quantity,uid,condi,(price*quantity) AS total_price FROM uorders WHERE id=5')
        row5 = cur.fetchall()
        cur.execute('SELECT id,pid,pName,price,quantity,uid,condi,(price*quantity) AS total_price FROM uorders WHERE id=6')
        row6 = cur.fetchall()
        cur.execute('SELECT id,pid,pName,price,quantity,uid,condi,(price*quantity) AS total_price FROM uorders WHERE id=7')
        row7 = cur.fetchall()
        cur.execute('SELECT id,pid,pName,price,quantity,uid,condi,(price*quantity) AS total_price FROM uorders WHERE id=8')
        row8 = cur.fetchall()
        cur.execute('SELECT id,pid,pName,price,quantity,uid,condi,(price*quantity) AS total_price FROM uorders WHERE id=9')
        row9 = cur.fetchall()
        cur.execute('SELECT id,pid,pName,price,quantity,uid,condi,(price*quantity) AS total_price FROM uorders WHERE id=10')
        row10 = cur.fetchall()
        cur.execute('SELECT id,pid,pName,price,quantity,uid,condi,(price*quantity) AS total_price FROM uorders WHERE id=11')
        row11 = cur.fetchall()
        cur.close()
        if request.method == 'POST' and form.validate():
            num = request.form['num']
            delete = form.delete.data
            icebox = request.form['icebox']
            curs = mysql.connection.cursor()
            if num == '1':
                curs.execute('DELETE FROM uorders WHERE id=1')
            elif num == '2':
                curs.execute('DELETE FROM uorders WHERE id=2')
            elif num == '3':
                curs.execute('DELETE FROM uorders WHERE id=3')
            elif num == '4':
                curs.execute('DELETE FROM uorders WHERE id=4')
            elif num == '5':
                curs.execute('DELETE FROM uorders WHERE id=5')
            elif num == '6':
                curs.execute('DELETE FROM uorders WHERE id=6')
            elif num == '7':
                curs.execute('DELETE FROM uorders WHERE id=7')
            elif num == '8':
                curs.execute('DELETE FROM uorders WHERE id=8')
            elif num == '9':
                curs.execute('DELETE FROM uorders WHERE id=9')
            elif num == '10':
                curs.execute('DELETE FROM uorders WHERE id=10')
            elif num == '11':
                curs.execute('DELETE FROM uorders WHERE id=11')
            elif icebox == '1':
                curs.execute('INSERT INTO uorders (uid,ofname,pid,quantity,pName,price,condi) VALUES (%s,%s,%s,%s,%s,%s,%s)', (uid,ofname,16,1,'icebox',1500,'배송준비',))
            curs.execute('DELETE FROM orders WHERE uid=%s', (uid,))
            curs.execute('ALTER TABLE orders DROP COLUMN id')
            curs.execute('INSERT orders SELECT uid,ofname,pid,quantity,dstatus,odate,ddate,pName,price,condi FROM uorders')
            curs.execute('ALTER TABLE orders ADD COLUMN id INT NOT NULL AUTO_INCREMENT PRIMARY KEY')
            mysql.connection.commit()
            curs.close()
            return redirect(url_for('carts'))
        return render_template('carts.html', form=form, result=result, order_rows=order_rows, row1=row1,row2=row2,row3=row3,row4=row4,row5=row5,row6=row6,row7=row7,row8=row8,row9=row9,row10=row10,row11=row11)
    elif 'ofname' in session:
        form = DeleteForm(request.form)
        ofname = session['ofname']
        cur = mysql.connection.cursor()
        order_rows = cur.execute("SELECT * FROM orders WHERE ofname=%s", (ofname,))
        cur.execute('DROP TABLE IF EXISTS uorders')
        cur.execute('CREATE TABLE uorders SELECT uid,ofname,pid,quantity,dstatus,odate,ddate,pName,price,condi FROM orders WHERE ofname=%s', (ofname,))
        cur.execute('ALTER TABLE uorders ADD COLUMN id INT NOT NULL AUTO_INCREMENT PRIMARY KEY')
        cur.execute('SELECT * FROM uorders')
        result = cur.fetchall()
        cur.execute('SELECT id,pid,pName,price,quantity,uid,ofname,condi,(price*quantity) AS total_price FROM uorders')
        row = cur.fetchall()
        cur.execute('SELECT id,pid,pName,price,quantity,uid,ofname,condi,(price*quantity) AS total_price FROM uorders WHERE id=1')
        row1 = cur.fetchall()
        cur.execute('SELECT id,pid,pName,price,quantity,uid,ofname,condi,(price*quantity) AS total_price FROM uorders WHERE id=2')
        row2 = cur.fetchall()
        cur.execute('SELECT id,pid,pName,price,quantity,uid,ofname,condi,(price*quantity) AS total_price FROM uorders WHERE id=3')
        row3 = cur.fetchall()
        cur.execute('SELECT id,pid,pName,price,quantity,uid,ofname,condi,(price*quantity) AS total_price FROM uorders WHERE id=4')
        row4 = cur.fetchall()
        cur.execute('SELECT id,pid,pName,price,quantity,uid,ofname,condi,(price*quantity) AS total_price FROM uorders WHERE id=5')
        row5 = cur.fetchall()
        cur.execute('SELECT id,pid,pName,price,quantity,uid,ofname,condi,(price*quantity) AS total_price FROM uorders WHERE id=6')
        row6 = cur.fetchall()
        cur.execute('SELECT id,pid,pName,price,quantity,uid,ofname,condi,(price*quantity) AS total_price FROM uorders WHERE id=7')
        row7 = cur.fetchall()
        cur.execute('SELECT id,pid,pName,price,quantity,uid,ofname,condi,(price*quantity) AS total_price FROM uorders WHERE id=8')
        row8 = cur.fetchall()
        cur.execute('SELECT id,pid,pName,price,quantity,uid,ofname,condi,(price*quantity) AS total_price FROM uorders WHERE id=9')
        row9 = cur.fetchall()
        cur.execute('SELECT id,pid,pName,price,quantity,uid,ofname,condi,(price*quantity) AS total_price FROM uorders WHERE id=10')
        row10 = cur.fetchall()
        cur.execute('SELECT id,pid,pName,price,quantity,uid,ofname,condi,(price*quantity) AS total_price FROM uorders WHERE id=11')
        row11 = cur.fetchall()
        cur.close()
        if request.method == 'POST' and form.validate():
            num = request.form['num']
            delete = form.delete.data
            icebox = request.form['icebox']
            curs = mysql.connection.cursor()
            if num == '1':
                curs.execute('DELETE FROM uorders WHERE id=1')
            elif num == '2':
                curs.execute('DELETE FROM uorders WHERE id=2')
            elif num == '3':
                curs.execute('DELETE FROM uorders WHERE id=3')
            elif num == '4':
                curs.execute('DELETE FROM uorders WHERE id=4')
            elif num == '5':
                curs.execute('DELETE FROM uorders WHERE id=5')
            elif num == '6':
                curs.execute('DELETE FROM uorders WHERE id=6')
            elif num == '7':
                curs.execute('DELETE FROM uorders WHERE id=7')
            elif num == '8':
                curs.execute('DELETE FROM uorders WHERE id=8')
            elif num == '9':
                curs.execute('DELETE FROM uorders WHERE id=9')
            elif num == '10':
                curs.execute('DELETE FROM uorders WHERE id=10')
            elif num == '11':
                curs.execute('DELETE FROM uorders WHERE id=11')
            elif icebox == '1':
                curs.execute('INSERT INTO uorders (ofname,pid,quantity,pName,price,condi) VALUES (%s,%s,%s,%s,%s,%s)', (ofname,16,1,'icebox',1500,'배송준비',))
            curs.execute('DELETE FROM orders WHERE ofname=%s', (ofname,))
            curs.execute('ALTER TABLE orders DROP COLUMN id')
            curs.execute('INSERT orders SELECT uid,ofname,pid,quantity,dstatus,odate,ddate,pName,price,condi FROM uorders')
            curs.execute('ALTER TABLE orders ADD COLUMN id INT NOT NULL AUTO_INCREMENT PRIMARY KEY')
            mysql.connection.commit()
            curs.close()
            return redirect(url_for('carts'))
        return render_template('carts.html', form=form, result=result, order_rows=order_rows, row1=row1,row2=row2,row3=row3,row4=row4,row5=row5,row6=row6,row7=row7,row8=row8,row9=row9,row10=row10,row11=row11)
    else:
        return render_template('carts.html')

class BuyForm(Form):
    username = StringField('', [validators.length(min=3, max=10)],
                       render_kw={'autofocus': True})
    rmobile1 = StringField('', [validators.length(min=3, max=3)],render_kw={'autofocus': True})
    rmobile2 = StringField('', [validators.length(min=3, max=4)],render_kw={'autofocus': True})
    rmobile3 = StringField('', [validators.length(min=3, max=4)],render_kw={'autofocus': True})
    addnum = StringField('', [validators.length(min=4, max=6)],render_kw={'autofocus': True})
    oplace = StringField('', [validators.length(min=4, max=20)],render_kw={'autofocus': True})
    oplacee = StringField('', [validators.length(min=4, max=50)],render_kw={'autofocus': True})
    oplaced = StringField('', [validators.length(min=4, max=50)],render_kw={'autofocus': True})
    memo = TextAreaField('', [validators.length(min=0, max=100)],render_kw={'autofocus': True})

@app.route('/buy_product', methods=["GET","POST"])
def buy_product():
    form = BuyForm(request.form)
    if 'uid' in session:
        username = form.username.data
        rmobile1 = form.rmobile1.data
        rmobile2 = form.rmobile2.data
        rmobile3 = form.rmobile3.data
        addnum = form.addnum.data
        oplace = form.oplace.data
        oplacee = form.oplacee.data
        oplaced = form.oplaced.data
        memo = form.memo.data
        uid = session['uid']
        cur = mysql.connection.cursor()
        cur.execute('SELECT id,pid,pName,price,quantity,uid,(price*quantity) AS total_price FROM uorders WHERE uid=%s', (uid,))
        product = cur.fetchall()
        cur.execute('SELECT SUM(price*quantity) AS total_price FROM uorders WHERE uid=%s', (uid,))
        total = cur.fetchall()
        cur.close()
        curs = mysql.connection.cursor()
        curs.execute('SELECT * FROM users WHERE id=%s', (uid,))
        recipient = curs.fetchall()
        curs.close()
        if request.method == 'POST' and form.validate():
            curso = mysql.connection.cursor()
            curso.execute('ALTER TABLE uorders DROP id')
            curso.execute('ALTER TABLE buy_product1 DROP id')
            curso.execute('INSERT buy_product1 SELECT uid,ofname,pid,quantity,dstatus,odate,ddate,pName,price,condi,(price*quantity) AS total_price FROM uorders')
            curso.execute('ALTER TABLE buy_product1 ADD COLUMN id INT NOT NULL AUTO_INCREMENT PRIMARY KEY')
            curso.execute('UPDATE users SET uid=%s,rmobile1=%s,rmobile2=%s,rmobile3=%s,addnum=%s,oplace=%s, oplacee=%s, oplaced=%s, memo=%s WHERE id=%s', (uid,rmobile1,rmobile2,rmobile3,addnum,oplace,oplacee,oplaced,memo,uid,))
            curso.execute('UPDATE buy_product2 SET uid=%s,rmobile1=%s,rmobile2=%s,rmobile3=%s,addnum=%s,oplace=%s, oplacee=%s, oplaced=%s, memo=%s WHERE uid=%s', (uid,rmobile1,rmobile2,rmobile3,addnum,oplace,oplacee,oplaced,memo,uid,))
            curso.execute('CREATE OR REPLACE VIEW all_orders AS SELECT id,ofname,username,pid,quantity,dstatus,odate,ddate,pName,price,total_price,condi,rmobile1,rmobile2,rmobile3,addnum,oplace,oplacee,oplaced,memo FROM buy_product1 INNER JOIN buy_product2 USING (ofname)')
            curso.execute('DELETE FROM orders WHERE uid=%s', (uid,))
            curso.execute('DELETE FROM uorders WHERE uid=%s', (uid,))
            mysql.connection.commit()
            curso.close()
            return redirect(url_for('mypage'))
        return render_template('buy_product.html', form=form, product=product, recipient=recipient, total=total)
    else:
        if 'ofname' in session:
            username = form.username.data
            rmobile1 = form.rmobile1.data
            rmobile2 = form.rmobile2.data
            rmobile3 = form.rmobile3.data
            addnum = form.addnum.data
            oplace = form.oplace.data
            oplacee = form.oplacee.data
            oplaced = form.oplaced.data
            memo = form.memo.data
            ofname = session['ofname']
            cur = mysql.connection.cursor()
            cur.execute('SELECT id,pid,pName,price,quantity,ofname,condi,(price*quantity) AS total_price FROM uorders WHERE ofname=%s', (ofname,))
            product = cur.fetchall()
            cur.execute('SELECT SUM(price*quantity) AS total_price FROM uorders WHERE ofname=%s', (ofname,))
            total = cur.fetchall()
            cur.close()
            if request.method == 'POST':
                curso = mysql.connection.cursor()
                curso.execute('ALTER TABLE uorders DROP id')
                curso.execute('ALTER TABLE buy_product1 DROP id')
                curso.execute('INSERT buy_product1 SELECT uid,ofname,pid,quantity,dstatus,odate,ddate,pName,price,condi,(price*quantity) AS total_price FROM uorders')
                curso.execute('ALTER TABLE buy_product1 ADD COLUMN id INT NOT NULL AUTO_INCREMENT PRIMARY KEY')
                curso.execute('INSERT INTO buy_product2 (ofname,username,rmobile1,rmobile2,rmobile3,addnum,oplace,oplacee,oplaced,memo) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (ofname,ofname,rmobile1,rmobile2,rmobile3,addnum,oplace,oplacee,oplaced,memo,))
                curso.execute('DELETE FROM buy_product2 WHERE ofname=%s', (ofname,))
                curso.execute('INSERT INTO buy_product2 (ofname,username,rmobile1,rmobile2,rmobile3,addnum,oplace,oplacee,oplaced,memo) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (ofname,ofname,rmobile1,rmobile2,rmobile3,addnum,oplace,oplacee,oplaced,memo,))
                curso.execute('CREATE OR REPLACE VIEW all_orders AS SELECT id,ofname,username,pid,quantity,dstatus,odate,ddate,pName,price,total_price,condi,rmobile1,rmobile2,rmobile3,addnum,oplace,oplacee,oplaced,memo FROM buy_product1 INNER JOIN buy_product2 USING (ofname)')
                curso.execute('DELETE FROM orders WHERE ofname=%s', (ofname,))
                curso.execute('DELETE FROM uorders WHERE ofname=%s', (ofname,))
                mysql.connection.commit()
                curso.close()
                return redirect(url_for('mypage'))
            return render_template('buy_product.html', form=form, product=product, total=total)
        return render_template('buy_product.html')

class MessageForm(Form):  # Create Message Form
    body = StringField('', [validators.length(min=1)], render_kw={'autofocus': True})

@app.route('/chatting/<string:id>', methods=['GET', 'POST'])
def chatting(id):
    if 'uid' in session:
        form = MessageForm(request.form)
        # Create cursor
        cur = mysql.connection.cursor()

        # lid name
        get_result = cur.execute("SELECT * FROM users WHERE id=%s", [id])
        l_data = cur.fetchone()
        if get_result > 0:
            session['name'] = l_data['name']
            uid = session['uid']
            session['lid'] = id

            if request.method == 'POST' and form.validate():
                txt_body = form.body.data
                # Create cursor
                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO messages(body, msg_by, msg_to) VALUES(%s, %s, %s)",
                            (txt_body, id, uid))
                # Commit cursor
                mysql.connection.commit()

            # Get users
            cur.execute("SELECT * FROM users")
            users = cur.fetchall()

            # Close Connection
            cur.close()
            return render_template('chat_room.html', users=users, form=form)
        else:
            flash('No permission!', 'danger')
            return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

@app.route('/chats', methods=['GET', 'POST'])
def chats():
    if 'lid' in session:
        id = session['lid']
        uid = session['uid']
        # Create cursor
        cur = mysql.connection.cursor()
        # Get message
        cur.execute("SELECT * FROM messages WHERE (msg_by=%s AND msg_to=%s) OR (msg_by=%s AND msg_to=%s) "
                    "ORDER BY id ASC", (id, uid, uid, id))
        chats = cur.fetchall()
        # Close Connection
        cur.close()
        return render_template('chats.html', chats=chats, )
    return redirect(url_for('login'))

class OrderForm(Form):  # Create Order Form
    quantity = StringField('', [validators.length(min=1), validators.DataRequired()],
                       render_kw={'autofocus': True, 'placeholder': '수량'})
    price = HiddenField('', [validators.length(min=0), validators.DataRequired()])
    pName = HiddenField('', [validators.length(min=0), validators.DataRequired()])

@app.route('/a1', methods=['GET', 'POST'])
def a1():
    form = OrderForm(request.form)
    # Create cursor
    cur = mysql.connection.cursor()
    # Get message
    values = 'a1'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY id ASC", (values,))
    products = cur.fetchall()
    # Close Connection
    cur.close()
    if request.method == 'POST' and form.validate():
        quantity = form.quantity.data
        price = form.price.data
        pName = form.pName.data
        pid = request.args['order']
        now = datetime.datetime.now()
        week = datetime.timedelta(days=7)
        delivery_date = now + week
        now_time = delivery_date.strftime("%y-%m-%d %H:%M:%S")
        # Create Cursor
        curs = mysql.connection.cursor()
        if 'uid' in session:
            uid = session['uid']
            ofname = session['s_name']
            curs.execute("INSERT INTO orders(uid, ofname, pid, quantity, ddate, price, pName) VALUES(%s, %s, %s, %s, %s, %s, %s)", (uid, ofname, pid, quantity, now_time, price, pName,))
        else:
            ofname = request.form['ofname']
            curs.execute("INSERT INTO orders(pid, ofname, quantity, ddate, price, pName) VALUES(%s, %s, %s, %s, %s, %s)", (pid, ofname, quantity, now_time, price, pName,))
            session['ofname'] = ofname
        # Commit cursor
        mysql.connection.commit()

        # Close Connection
        cur.close()

        flash('Order successful', 'success')
        return render_template('a1.html', a1=products, form=form)
    if 'view' in request.args:
        product_id = request.args['view']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
        product = curso.fetchall()
        x = content_based_filtering(product_id)
        wrappered = wrappers(content_based_filtering, product_id)
        execution_time = timeit.timeit(wrappered, number=0)
        # print('Execution time: ' + str(execution_time) + ' usec')
        if 'uid' in session:
            uid = session['uid']
            # Create cursor
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM product_view WHERE user_id=%s AND product_id=%s", (uid, product_id))
            result = cur.fetchall()
            if result:
                now = datetime.datetime.now()
                now_time = now.strftime("%y-%m-%d %H:%M:%S")
                cur.execute("UPDATE product_view SET date=%s WHERE user_id=%s AND product_id=%s",
                            (now_time, uid, product_id))
            else:
                cur.execute("INSERT INTO product_view(user_id, product_id) VALUES(%s, %s)", (uid, product_id))
                mysql.connection.commit()
        return render_template('view_product_a1.html', x=x, a1=product, form=form)
    elif 'order' in request.args:
        product_id = request.args['order']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
        product = curso.fetchall()
        x = content_based_filtering(product_id)
        return render_template('order_product_a1.html', x=x, a1=product, form=form)
    return render_template('a1.html', a1=products, form=form)

@app.route('/a2', methods=['GET', 'POST'])
def a2():
    form = OrderForm(request.form)
    # Create cursor
    cur = mysql.connection.cursor()
    # Get message
    values = 'a2'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY id ASC", (values,))
    products = cur.fetchall()
    # Close Connection
    cur.close()
    if request.method == 'POST' and form.validate():
        quantity = form.quantity.data
        price = form.price.data
        pName = form.pName.data
        pid = request.args['order']
        now = datetime.datetime.now()
        week = datetime.timedelta(days=7)
        delivery_date = now + week
        now_time = delivery_date.strftime("%y-%m-%d %H:%M:%S")
        # Create Cursor
        curs = mysql.connection.cursor()
        if 'uid' in session:
            uid = session['uid']
            ofname = session['s_name']
            curs.execute("INSERT INTO orders(uid, ofname, pid, quantity, ddate, price, pName) VALUES(%s, %s, %s, %s, %s, %s, %s)", (uid, ofname, pid, quantity, now_time, price, pName,))
        else:
            ofname = request.form['ofname']
            curs.execute("INSERT INTO orders(pid, ofname, quantity, ddate, price, pName) VALUES(%s, %s, %s, %s, %s, %s)", (pid, ofname, quantity, now_time, price, pName,))
            session['ofname'] = ofname
        # Commit cursor
        mysql.connection.commit()

        # Close Connection
        cur.close()

        flash('Order successful', 'success')
        return render_template('a2.html', a2=products, form=form)
    if 'view' in request.args:
        product_id = request.args['view']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
        product = curso.fetchall()
        x = content_based_filtering(product_id)
        wrappered = wrappers(content_based_filtering, product_id)
        execution_time = timeit.timeit(wrappered, number=0)
        # print('Execution time: ' + str(execution_time) + ' usec')
        if 'uid' in session:
            uid = session['uid']
            # Create cursor
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM product_view WHERE user_id=%s AND product_id=%s", (uid, product_id))
            result = cur.fetchall()
            if result:
                now = datetime.datetime.now()
                now_time = now.strftime("%y-%m-%d %H:%M:%S")
                cur.execute("UPDATE product_view SET date=%s WHERE user_id=%s AND product_id=%s",
                            (now_time, uid, product_id))
            else:
                cur.execute("INSERT INTO product_view(user_id, product_id) VALUES(%s, %s)", (uid, product_id))
                mysql.connection.commit()
        return render_template('view_product_a2.html', x=x, a2=product, form=form)
    elif 'order' in request.args:
        product_id = request.args['order']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
        product = curso.fetchall()
        x = content_based_filtering(product_id)
        return render_template('order_product_a2.html', x=x, a2=product, form=form)
    return render_template('a2.html', a2=products, form=form)

@app.route('/a3', methods=['GET', 'POST'])
def a3():
    form = OrderForm(request.form)
    # Create cursor
    cur = mysql.connection.cursor()
    # Get message
    values = 'a3'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY id ASC", (values,))
    products = cur.fetchall()
    # Close Connection
    cur.close()
    if request.method == 'POST' and form.validate():
        quantity = form.quantity.data
        price = form.price.data
        pName = form.pName.data
        pid = request.args['order']
        now = datetime.datetime.now()
        week = datetime.timedelta(days=7)
        delivery_date = now + week
        now_time = delivery_date.strftime("%y-%m-%d %H:%M:%S")
        # Create Cursor
        curs = mysql.connection.cursor()
        if 'uid' in session:
            uid = session['uid']
            ofname = session['s_name']
            curs.execute("INSERT INTO orders(uid, ofname, pid, quantity, ddate, price, pName) VALUES(%s, %s, %s, %s, %s, %s, %s)", (uid, ofname, pid, quantity, now_time, price, pName,))
        else:
            ofname = request.form['ofname']
            curs.execute("INSERT INTO orders(pid, ofname, quantity, ddate, price, pName) VALUES(%s, %s, %s, %s, %s, %s)", (pid, ofname, quantity, now_time, price, pName,))
            session['ofname'] = ofname
        # Commit cursor
        mysql.connection.commit()

        # Close Connection
        cur.close()

        flash('Order successful', 'success')
        return render_template('a3.html', a3=products, form=form)
    if 'view' in request.args:
        product_id = request.args['view']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
        product = curso.fetchall()
        x = content_based_filtering(product_id)
        wrappered = wrappers(content_based_filtering, product_id)
        execution_time = timeit.timeit(wrappered, number=0)
        # print('Execution time: ' + str(execution_time) + ' usec')
        if 'uid' in session:
            uid = session['uid']
            # Create cursor
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM product_view WHERE user_id=%s AND product_id=%s", (uid, product_id))
            result = cur.fetchall()
            if result:
                now = datetime.datetime.now()
                now_time = now.strftime("%y-%m-%d %H:%M:%S")
                cur.execute("UPDATE product_view SET date=%s WHERE user_id=%s AND product_id=%s",
                            (now_time, uid, product_id))
            else:
                cur.execute("INSERT INTO product_view(user_id, product_id) VALUES(%s, %s)", (uid, product_id))
                mysql.connection.commit()
        return render_template('view_product_a3.html', x=x, a3=product, form=form)
    elif 'order' in request.args:
        product_id = request.args['order']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
        product = curso.fetchall()
        x = content_based_filtering(product_id)
        return render_template('order_product_a3.html', x=x, a3=product, form=form)
    return render_template('a3.html', a3=products, form=form)

@app.route('/a4', methods=['GET', 'POST'])
def a4():
    form = OrderForm(request.form)
    # Create cursor
    cur = mysql.connection.cursor()
    # Get message
    values = 'a4'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY id ASC", (values,))
    products = cur.fetchall()
    # Close Connection
    cur.close()
    if request.method == 'POST' and form.validate():
        quantity = form.quantity.data
        price = form.price.data
        pName = form.pName.data
        pid = request.args['order']
        now = datetime.datetime.now()
        week = datetime.timedelta(days=7)
        delivery_date = now + week
        now_time = delivery_date.strftime("%y-%m-%d %H:%M:%S")
        # Create Cursor
        curs = mysql.connection.cursor()
        if 'uid' in session:
            uid = session['uid']
            ofname = session['s_name']
            curs.execute("INSERT INTO orders(uid, ofname, pid, quantity, ddate, price, pName) VALUES(%s, %s, %s, %s, %s, %s, %s)", (uid, ofname, pid, quantity, now_time, price, pName,))
        else:
            ofname = request.form['ofname']
            curs.execute("INSERT INTO orders(pid, ofname, quantity, ddate, price, pName) VALUES(%s, %s, %s, %s, %s, %s)", (pid, ofname, quantity, now_time, price, pName,))
            session['ofname'] = ofname
        # Commit cursor
        mysql.connection.commit()

        # Close Connection
        cur.close()

        flash('Order successful', 'success')
        return render_template('a4.html', a4=products, form=form)
    if 'view' in request.args:
        product_id = request.args['view']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
        product = curso.fetchall()
        x = content_based_filtering(product_id)
        wrappered = wrappers(content_based_filtering, product_id)
        execution_time = timeit.timeit(wrappered, number=0)
        # print('Execution time: ' + str(execution_time) + ' usec')
        if 'uid' in session:
            uid = session['uid']
            # Create cursor
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM product_view WHERE user_id=%s AND product_id=%s", (uid, product_id))
            result = cur.fetchall()
            if result:
                now = datetime.datetime.now()
                now_time = now.strftime("%y-%m-%d %H:%M:%S")
                cur.execute("UPDATE product_view SET date=%s WHERE user_id=%s AND product_id=%s",
                            (now_time, uid, product_id))
            else:
                cur.execute("INSERT INTO product_view(user_id, product_id) VALUES(%s, %s)", (uid, product_id))
                mysql.connection.commit()
        return render_template('view_product_a3.html', x=x, a4=product, form=form)
    elif 'order' in request.args:
        product_id = request.args['order']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
        product = curso.fetchall()
        x = content_based_filtering(product_id)
        return render_template('order_product_a3.html', x=x, a4=product, form=form)
    return render_template('a4.html', a4=products, form=form)

@app.route('/a5', methods=['GET', 'POST'])
def a5():
    form = OrderForm(request.form)
    # Create cursor
    cur = mysql.connection.cursor()
    # Get message
    values = 'a5'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY id ASC", (values,))
    products = cur.fetchall()
    # Close Connection
    cur.close()
    if request.method == 'POST' and form.validate():
        quantity = form.quantity.data
        price = form.price.data
        pName = form.pName.data
        pid = request.args['order']
        now = datetime.datetime.now()
        week = datetime.timedelta(days=7)
        delivery_date = now + week
        now_time = delivery_date.strftime("%y-%m-%d %H:%M:%S")
        # Create Cursor
        curs = mysql.connection.cursor()
        if 'uid' in session:
            uid = session['uid']
            ofname = session['s_name']
            curs.execute("INSERT INTO orders(uid, ofname, pid, quantity, ddate, price, pName) VALUES(%s, %s, %s, %s, %s, %s, %s)", (uid, ofname, pid, quantity, now_time, price, pName,))
        else:
            ofname = request.form['ofname']
            curs.execute("INSERT INTO orders(pid, ofname, quantity, ddate, price, pName) VALUES(%s, %s, %s, %s, %s, %s)", (pid, ofname, quantity, now_time, price, pName,))
            session['ofname'] = ofname
        # Commit cursor
        mysql.connection.commit()

        # Close Connection
        cur.close()

        flash('Order successful', 'success')
        return render_template('a5.html', a5=products, form=form)
    if 'view' in request.args:
        product_id = request.args['view']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
        product = curso.fetchall()
        x = content_based_filtering(product_id)
        wrappered = wrappers(content_based_filtering, product_id)
        execution_time = timeit.timeit(wrappered, number=0)
        # print('Execution time: ' + str(execution_time) + ' usec')
        if 'uid' in session:
            uid = session['uid']
            # Create cursor
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM product_view WHERE user_id=%s AND product_id=%s", (uid, product_id))
            result = cur.fetchall()
            if result:
                now = datetime.datetime.now()
                now_time = now.strftime("%y-%m-%d %H:%M:%S")
                cur.execute("UPDATE product_view SET date=%s WHERE user_id=%s AND product_id=%s",
                            (now_time, uid, product_id))
            else:
                cur.execute("INSERT INTO product_view(user_id, product_id) VALUES(%s, %s)", (uid, product_id))
                mysql.connection.commit()
        return render_template('view_product_a5.html', x=x, a5=product, form=form)
    elif 'order' in request.args:
        product_id = request.args['order']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
        product = curso.fetchall()
        x = content_based_filtering(product_id)
        return render_template('order_product_a5.html', x=x, a5=product, form=form)
    return render_template('a5.html', a5=products, form=form)

@app.route('/a6', methods=['GET', 'POST'])
def a6():
    form = OrderForm(request.form)
    # Create cursor
    cur = mysql.connection.cursor()
    # Get message
    values = 'a6'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY id ASC", (values,))
    products = cur.fetchall()
    # Close Connection
    cur.close()
    if request.method == 'POST' and form.validate():
        quantity = form.quantity.data
        price = form.price.data
        pName = form.pName.data
        pid = request.args['order']
        now = datetime.datetime.now()
        week = datetime.timedelta(days=7)
        delivery_date = now + week
        now_time = delivery_date.strftime("%y-%m-%d %H:%M:%S")
        # Create Cursor
        curs = mysql.connection.cursor()
        if 'uid' in session:
            uid = session['uid']
            ofname = session['s_name']
            curs.execute("INSERT INTO orders(uid, ofname, pid, quantity, ddate, price, pName) VALUES(%s, %s, %s, %s, %s, %s, %s)", (uid, ofname, pid, quantity, now_time, price, pName,))
        else:
            ofname = request.form['ofname']
            curs.execute("INSERT INTO orders(pid, ofname, quantity, ddate, price, pName) VALUES(%s, %s, %s, %s, %s, %s)", (pid, ofname, quantity, now_time, price, pName,))
            session['ofname'] = ofname
        # Commit cursor
        mysql.connection.commit()

        # Close Connection
        cur.close()

        flash('Order successful', 'success')
        return render_template('a6.html', a6=products, form=form)
    if 'view' in request.args:
        product_id = request.args['view']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
        product = curso.fetchall()
        x = content_based_filtering(product_id)
        wrappered = wrappers(content_based_filtering, product_id)
        execution_time = timeit.timeit(wrappered, number=0)
        # print('Execution time: ' + str(execution_time) + ' usec')
        if 'uid' in session:
            uid = session['uid']
            # Create cursor
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM product_view WHERE user_id=%s AND product_id=%s", (uid, product_id))
            result = cur.fetchall()
            if result:
                now = datetime.datetime.now()
                now_time = now.strftime("%y-%m-%d %H:%M:%S")
                cur.execute("UPDATE product_view SET date=%s WHERE user_id=%s AND product_id=%s",
                            (now_time, uid, product_id))
            else:
                cur.execute("INSERT INTO product_view(user_id, product_id) VALUES(%s, %s)", (uid, product_id))
                mysql.connection.commit()
        return render_template('view_product_a6.html', x=x, a6=product, form=form)
    elif 'order' in request.args:
        product_id = request.args['order']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
        product = curso.fetchall()
        x = content_based_filtering(product_id)
        return render_template('order_product_a6.html', x=x, a6=product, form=form)
    return render_template('a6.html', a6=products, form=form)

@app.route('/b1', methods=['GET', 'POST'])
def b1():
    form = OrderForm(request.form)
    # Create cursor
    cur = mysql.connection.cursor()
    # Get message
    values = 'b1'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY id ASC", (values,))
    products = cur.fetchall()
    # Close Connection
    cur.close()
    if request.method == 'POST' and form.validate():
        quantity = form.quantity.data
        price = form.price.data
        pName = form.pName.data
        pid = request.args['order']
        now = datetime.datetime.now()
        week = datetime.timedelta(days=7)
        delivery_date = now + week
        now_time = delivery_date.strftime("%y-%m-%d %H:%M:%S")
        # Create Cursor
        curs = mysql.connection.cursor()
        if 'uid' in session:
            uid = session['uid']
            ofname = session['s_name']
            curs.execute("INSERT INTO orders(uid, ofname, pid, quantity, ddate, price, pName) VALUES(%s, %s, %s, %s, %s, %s, %s)", (uid, ofname, pid, quantity, now_time, price, pName,))
        else:
            ofname = request.form['ofname']
            curs.execute("INSERT INTO orders(pid, ofname, quantity, ddate, price, pName) VALUES(%s, %s, %s, %s, %s, %s)", (pid, ofname, quantity, now_time, price, pName,))
            session['ofname'] = ofname
        # Commit cursor
        mysql.connection.commit()

        # Close Connection
        cur.close()

        flash('Order successful', 'success')
        return render_template('b1.html', b1=products, form=form)
    if 'view' in request.args:
        product_id = request.args['view']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
        product = curso.fetchall()
        x = content_based_filtering(product_id)
        wrappered = wrappers(content_based_filtering, product_id)
        execution_time = timeit.timeit(wrappered, number=0)
        # print('Execution time: ' + str(execution_time) + ' usec')
        if 'uid' in session:
            uid = session['uid']
            # Create cursor
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM product_view WHERE user_id=%s AND product_id=%s", (uid, product_id))
            result = cur.fetchall()
            if result:
                now = datetime.datetime.now()
                now_time = now.strftime("%y-%m-%d %H:%M:%S")
                cur.execute("UPDATE product_view SET date=%s WHERE user_id=%s AND product_id=%s",
                            (now_time, uid, product_id))
            else:
                cur.execute("INSERT INTO product_view(user_id, product_id) VALUES(%s, %s)", (uid, product_id))
                mysql.connection.commit()
        return render_template('view_product_b1.html', x=x, b1=product, form=form)
    elif 'order' in request.args:
        product_id = request.args['order']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
        product = curso.fetchall()
        x = content_based_filtering(product_id)
        return render_template('order_product_b1.html', x=x, b1=product, form=form)
    return render_template('b1.html', b1=products, form=form)

@app.route('/b2', methods=['GET', 'POST'])
def b2():
    form = OrderForm(request.form)
    # Create cursor
    cur = mysql.connection.cursor()
    # Get message
    values = 'b2'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY id ASC", (values,))
    products = cur.fetchall()
    # Close Connection
    cur.close()
    if request.method == 'POST' and form.validate():
        quantity = form.quantity.data
        price = form.price.data
        pName = form.pName.data
        pid = request.args['order']
        now = datetime.datetime.now()
        week = datetime.timedelta(days=7)
        delivery_date = now + week
        now_time = delivery_date.strftime("%y-%m-%d %H:%M:%S")
        # Create Cursor
        curs = mysql.connection.cursor()
        if 'uid' in session:
            uid = session['uid']
            ofname = session['s_name']
            curs.execute("INSERT INTO orders(uid, ofname, pid, quantity, ddate, price, pName) VALUES(%s, %s, %s, %s, %s, %s, %s)", (uid, ofname, pid, quantity, now_time, price, pName,))
        else:
            ofname = request.form['ofname']
            curs.execute("INSERT INTO orders(pid, ofname, quantity, ddate, price, pName) VALUES(%s, %s, %s, %s, %s, %s)", (pid, ofname, quantity, now_time, price, pName,))
            session['ofname'] = ofname
        # Commit cursor
        mysql.connection.commit()

        # Close Connection
        cur.close()

        flash('Order successful', 'success')
        return render_template('b2.html', b2=products, form=form)
    if 'view' in request.args:
        product_id = request.args['view']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
        product = curso.fetchall()
        x = content_based_filtering(product_id)
        wrappered = wrappers(content_based_filtering, product_id)
        execution_time = timeit.timeit(wrappered, number=0)
        # print('Execution time: ' + str(execution_time) + ' usec')
        if 'uid' in session:
            uid = session['uid']
            # Create cursor
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM product_view WHERE user_id=%s AND product_id=%s", (uid, product_id))
            result = cur.fetchall()
            if result:
                now = datetime.datetime.now()
                now_time = now.strftime("%y-%m-%d %H:%M:%S")
                cur.execute("UPDATE product_view SET date=%s WHERE user_id=%s AND product_id=%s",
                            (now_time, uid, product_id))
            else:
                cur.execute("INSERT INTO product_view(user_id, product_id) VALUES(%s, %s)", (uid, product_id))
                mysql.connection.commit()
        return render_template('view_product_b2.html', x=x, b2=product, form=form)
    elif 'order' in request.args:
        product_id = request.args['order']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
        product = curso.fetchall()
        x = content_based_filtering(product_id)
        return render_template('order_product_b2.html', x=x, b2=product, form=form)
    return render_template('b2.html', b2=products, form=form)

@app.route('/c1', methods=['GET', 'POST'])
def c1():
    form = OrderForm(request.form)
    # Create cursor
    cur = mysql.connection.cursor()
    # Get message
    values = 'c1'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY id ASC", (values,))
    products = cur.fetchall()
    # Close Connection
    cur.close()
    if request.method == 'POST' and form.validate():
        quantity = form.quantity.data
        price = form.price.data
        pName = form.pName.data
        pid = request.args['order']
        now = datetime.datetime.now()
        week = datetime.timedelta(days=7)
        delivery_date = now + week
        now_time = delivery_date.strftime("%y-%m-%d %H:%M:%S")
        # Create Cursor
        curs = mysql.connection.cursor()
        if 'uid' in session:
            uid = session['uid']
            ofname = session['s_name']
            curs.execute("INSERT INTO orders(uid, ofname, pid, quantity, ddate, price, pName) VALUES(%s, %s, %s, %s, %s, %s, %s)", (uid, ofname, pid, quantity, now_time, price, pName,))
        else:
            ofname = request.form['ofname']
            curs.execute("INSERT INTO orders(pid, ofname, quantity, ddate, price, pName) VALUES(%s, %s, %s, %s, %s, %s)", (pid, ofname, quantity, now_time, price, pName,))
            session['ofname'] = ofname
        # Commit cursor
        mysql.connection.commit()

        # Close Connection
        cur.close()

        flash('Order successful', 'success')
        return render_template('c1.html', c1=products, form=form)
    if 'view' in request.args:
        product_id = request.args['view']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
        product = curso.fetchall()
        x = content_based_filtering(product_id)
        wrappered = wrappers(content_based_filtering, product_id)
        execution_time = timeit.timeit(wrappered, number=0)
        # print('Execution time: ' + str(execution_time) + ' usec')
        if 'uid' in session:
            uid = session['uid']
            # Create cursor
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM product_view WHERE user_id=%s AND product_id=%s", (uid, product_id))
            result = cur.fetchall()
            if result:
                now = datetime.datetime.now()
                now_time = now.strftime("%y-%m-%d %H:%M:%S")
                cur.execute("UPDATE product_view SET date=%s WHERE user_id=%s AND product_id=%s",
                            (now_time, uid, product_id))
            else:
                cur.execute("INSERT INTO product_view(user_id, product_id) VALUES(%s, %s)", (uid, product_id))
                mysql.connection.commit()
        return render_template('view_product_c1.html', x=x, c1=product, form=form)
    elif 'order' in request.args:
        product_id = request.args['order']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
        product = curso.fetchall()
        x = content_based_filtering(product_id)
        return render_template('order_product_c1.html', x=x, c1=product, form=form)
    return render_template('c1.html', c1=products, form=form)

@app.route('/c2', methods=['GET', 'POST'])
def c2():
    form = OrderForm(request.form)
    # Create cursor
    cur = mysql.connection.cursor()
    # Get message
    values = 'c2'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY id ASC", (values,))
    products = cur.fetchall()
    # Close Connection
    cur.close()
    if request.method == 'POST' and form.validate():
        quantity = form.quantity.data
        price = form.price.data
        pName = form.pName.data
        pid = request.args['order']
        now = datetime.datetime.now()
        week = datetime.timedelta(days=7)
        delivery_date = now + week
        now_time = delivery_date.strftime("%y-%m-%d %H:%M:%S")
        # Create Cursor
        curs = mysql.connection.cursor()
        if 'uid' in session:
            uid = session['uid']
            ofname = session['s_name']
            curs.execute("INSERT INTO orders(uid, ofname, pid, quantity, ddate, price, pName) VALUES(%s, %s, %s, %s, %s, %s, %s)", (uid, ofname, pid, quantity, now_time, price, pName,))
        else:
            ofname = request.form['ofname']
            curs.execute("INSERT INTO orders(pid, ofname, quantity, ddate, price, pName) VALUES(%s, %s, %s, %s, %s, %s)", (pid, ofname, quantity, now_time, price, pName,))
            session['ofname'] = ofname
        # Commit cursor
        mysql.connection.commit()

        # Close Connection
        cur.close()

        flash('Order successful', 'success')
        return render_template('c2.html', c2=products, form=form)
    if 'view' in request.args:
        product_id = request.args['view']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
        product = curso.fetchall()
        x = content_based_filtering(product_id)
        wrappered = wrappers(content_based_filtering, product_id)
        execution_time = timeit.timeit(wrappered, number=0)
        # print('Execution time: ' + str(execution_time) + ' usec')
        if 'uid' in session:
            uid = session['uid']
            # Create cursor
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM product_view WHERE user_id=%s AND product_id=%s", (uid, product_id))
            result = cur.fetchall()
            if result:
                now = datetime.datetime.now()
                now_time = now.strftime("%y-%m-%d %H:%M:%S")
                cur.execute("UPDATE product_view SET date=%s WHERE user_id=%s AND product_id=%s",
                            (now_time, uid, product_id))
            else:
                cur.execute("INSERT INTO product_view(user_id, product_id) VALUES(%s, %s)", (uid, product_id))
                mysql.connection.commit()
        return render_template('view_product_c2.html', x=x, c2=product, form=form)
    elif 'order' in request.args:
        product_id = request.args['order']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
        product = curso.fetchall()
        x = content_based_filtering(product_id)
        return render_template('order_product_c2.html', x=x, c2=product, form=form)
    return render_template('c2.html', c2=products, form=form)

@app.route('/c3', methods=['GET', 'POST'])
def c3():
    form = OrderForm(request.form)
    # Create cursor
    cur = mysql.connection.cursor()
    # Get message
    values = 'c3'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY id ASC", (values,))
    products = cur.fetchall()
    # Close Connection
    cur.close()
    if request.method == 'POST' and form.validate():
        quantity = form.quantity.data
        price = form.price.data
        pName = form.pName.data
        pid = request.args['order']
        now = datetime.datetime.now()
        week = datetime.timedelta(days=7)
        delivery_date = now + week
        now_time = delivery_date.strftime("%y-%m-%d %H:%M:%S")
        # Create Cursor
        curs = mysql.connection.cursor()
        if 'uid' in session:
            uid = session['uid']
            ofname = session['s_name']
            curs.execute("INSERT INTO orders(uid, ofname, pid, quantity, ddate, price, pName) VALUES(%s, %s, %s, %s, %s, %s, %s)", (uid, ofname, pid, quantity, now_time, price, pName,))
        else:
            ofname = request.form['ofname']
            curs.execute("INSERT INTO orders(pid, ofname, quantity, ddate, price, pName) VALUES(%s, %s, %s, %s, %s, %s)", (pid, ofname, quantity, now_time, price, pName,))
            session['ofname'] = ofname
        # Commit cursor
        mysql.connection.commit()

        # Close Connection
        cur.close()

        flash('Order successful', 'success')
        return render_template('c3.html', c3=products, form=form)
    if 'view' in request.args:
        product_id = request.args['view']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
        product = curso.fetchall()
        x = content_based_filtering(product_id)
        wrappered = wrappers(content_based_filtering, product_id)
        execution_time = timeit.timeit(wrappered, number=0)
        # print('Execution time: ' + str(execution_time) + ' usec')
        if 'uid' in session:
            uid = session['uid']
            # Create cursor
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM product_view WHERE user_id=%s AND product_id=%s", (uid, product_id))
            result = cur.fetchall()
            if result:
                now = datetime.datetime.now()
                now_time = now.strftime("%y-%m-%d %H:%M:%S")
                cur.execute("UPDATE product_view SET date=%s WHERE user_id=%s AND product_id=%s",
                            (now_time, uid, product_id))
            else:
                cur.execute("INSERT INTO product_view(user_id, product_id) VALUES(%s, %s)", (uid, product_id))
                mysql.connection.commit()
        return render_template('view_product_c3.html', x=x, c3=product, form=form)
    elif 'order' in request.args:
        product_id = request.args['order']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
        product = curso.fetchall()
        x = content_based_filtering(product_id)
        return render_template('order_product_c3.html', x=x, c3=product, form=form)
    return render_template('c3.html', c3=products, form=form)

@app.route('/d1', methods=['GET', 'POST'])
def d1():
    form = OrderForm(request.form)
    # Create cursor
    cur = mysql.connection.cursor()
    # Get message
    values = 'd1'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY id ASC", (values,))
    products = cur.fetchall()
    # Close Connection
    cur.close()
    if request.method == 'POST' and form.validate():
        quantity = form.quantity.data
        price = form.price.data
        pName = form.pName.data
        pid = request.args['order']
        now = datetime.datetime.now()
        week = datetime.timedelta(days=7)
        delivery_date = now + week
        now_time = delivery_date.strftime("%y-%m-%d %H:%M:%S")
        # Create Cursor
        curs = mysql.connection.cursor()
        if 'uid' in session:
            uid = session['uid']
            ofname = session['s_name']
            curs.execute("INSERT INTO orders(uid, ofname, pid, quantity, ddate, price, pName) VALUES(%s, %s, %s, %s, %s, %s, %s)", (uid, ofname, pid, quantity, now_time, price, pName,))
        else:
            ofname = request.form['ofname']
            curs.execute("INSERT INTO orders(pid, ofname, quantity, ddate, price, pName) VALUES(%s, %s, %s, %s, %s, %s)", (pid, ofname, quantity, now_time, price, pName,))
            session['ofname'] = ofname
        # Commit cursor
        mysql.connection.commit()

        # Close Connection
        cur.close()

        flash('Order successful', 'success')
        return render_template('d1.html', d1=products, form=form)
    if 'view' in request.args:
        product_id = request.args['view']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
        product = curso.fetchall()
        x = content_based_filtering(product_id)
        wrappered = wrappers(content_based_filtering, product_id)
        execution_time = timeit.timeit(wrappered, number=0)
        # print('Execution time: ' + str(execution_time) + ' usec')
        if 'uid' in session:
            uid = session['uid']
            # Create cursor
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM product_view WHERE user_id=%s AND product_id=%s", (uid, product_id))
            result = cur.fetchall()
            if result:
                now = datetime.datetime.now()
                now_time = now.strftime("%y-%m-%d %H:%M:%S")
                cur.execute("UPDATE product_view SET date=%s WHERE user_id=%s AND product_id=%s",
                            (now_time, uid, product_id))
            else:
                cur.execute("INSERT INTO product_view(user_id, product_id) VALUES(%s, %s)", (uid, product_id))
                mysql.connection.commit()
        return render_template('view_product_d1.html', x=x, d1=product, form=form)
    elif 'order' in request.args:
        product_id = request.args['order']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
        product = curso.fetchall()
        x = content_based_filtering(product_id)
        return render_template('order_product_d1.html', x=x, d1=product, form=form)
    return render_template('d1.html', d1=products, form=form)

@app.route('/e1', methods=['GET', 'POST'])
def e1():
    form = OrderForm(request.form)
    # Create cursor
    cur = mysql.connection.cursor()
    # Get message
    values = 'e1'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY id ASC", (values,))
    products = cur.fetchall()
    # Close Connection
    cur.close()
    if request.method == 'POST' and form.validate():
        quantity = form.quantity.data
        price = form.price.data
        pName = form.pName.data
        pid = request.args['order']
        now = datetime.datetime.now()
        week = datetime.timedelta(days=7)
        delivery_date = now + week
        now_time = delivery_date.strftime("%y-%m-%d %H:%M:%S")
        # Create Cursor
        curs = mysql.connection.cursor()
        if 'uid' in session:
            uid = session['uid']
            ofname = session['s_name']
            curs.execute("INSERT INTO orders(uid, ofname, pid, quantity, ddate, price, pName) VALUES(%s, %s, %s, %s, %s, %s, %s)", (uid, ofname, pid, quantity, now_time, price, pName,))
        else:
            ofname = request.form['ofname']
            curs.execute("INSERT INTO orders(pid, ofname, quantity, ddate, price, pName) VALUES(%s, %s, %s, %s, %s, %s)", (pid, ofname, quantity, now_time, price, pName,))
            session['ofname'] = ofname
        # Commit cursor
        mysql.connection.commit()

        # Close Connection
        cur.close()

        flash('Order successful', 'success')
        return render_template('e1.html', e1=products, form=form)
    if 'view' in request.args:
        product_id = request.args['view']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
        product = curso.fetchall()
        x = content_based_filtering(product_id)
        wrappered = wrappers(content_based_filtering, product_id)
        execution_time = timeit.timeit(wrappered, number=0)
        # print('Execution time: ' + str(execution_time) + ' usec')
        if 'uid' in session:
            uid = session['uid']
            # Create cursor
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM product_view WHERE user_id=%s AND product_id=%s", (uid, product_id))
            result = cur.fetchall()
            if result:
                now = datetime.datetime.now()
                now_time = now.strftime("%y-%m-%d %H:%M:%S")
                cur.execute("UPDATE product_view SET date=%s WHERE user_id=%s AND product_id=%s",
                            (now_time, uid, product_id))
            else:
                cur.execute("INSERT INTO product_view(user_id, product_id) VALUES(%s, %s)", (uid, product_id))
                mysql.connection.commit()
        return render_template('view_product_e1.html', x=x, e1=product, form=form)
    elif 'order' in request.args:
        product_id = request.args['order']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
        product = curso.fetchall()
        x = content_based_filtering(product_id)
        return render_template('order_product_e1.html', x=x, e1=product, form=form)
    return render_template('e1.html', e1=products, form=form)

@app.route('/f1', methods=['GET', 'POST'])
def f1():
    form = OrderForm(request.form)
    # Create cursor
    cur = mysql.connection.cursor()
    # Get message
    values = 'f1'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY id ASC", (values,))
    products = cur.fetchall()
    # Close Connection
    cur.close()
    if request.method == 'POST' and form.validate():
        quantity = form.quantity.data
        price = form.price.data
        pName = form.pName.data
        pid = request.args['order']
        now = datetime.datetime.now()
        week = datetime.timedelta(days=7)
        delivery_date = now + week
        now_time = delivery_date.strftime("%y-%m-%d %H:%M:%S")
        # Create Cursor
        curs = mysql.connection.cursor()
        if 'uid' in session:
            uid = session['uid']
            ofname = session['s_name']
            curs.execute("INSERT INTO orders(uid, ofname, pid, quantity, ddate, price, pName) VALUES(%s, %s, %s, %s, %s, %s, %s)", (uid, ofname, pid, quantity, now_time, price, pName,))
        else:
            ofname = request.form['ofname']
            curs.execute("INSERT INTO orders(pid, ofname, quantity, ddate, price, pName) VALUES(%s, %s, %s, %s, %s, %s)", (pid, ofname, quantity, now_time, price, pName,))
            session['ofname'] = ofname
        # Commit cursor
        mysql.connection.commit()

        # Close Connection
        cur.close()

        flash('Order successful', 'success')
        return render_template('f1.html', f1=products, form=form)
    if 'view' in request.args:
        product_id = request.args['view']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
        product = curso.fetchall()
        x = content_based_filtering(product_id)
        wrappered = wrappers(content_based_filtering, product_id)
        execution_time = timeit.timeit(wrappered, number=0)
        # print('Execution time: ' + str(execution_time) + ' usec')
        if 'uid' in session:
            uid = session['uid']
            # Create cursor
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM product_view WHERE user_id=%s AND product_id=%s", (uid, product_id))
            result = cur.fetchall()
            if result:
                now = datetime.datetime.now()
                now_time = now.strftime("%y-%m-%d %H:%M:%S")
                cur.execute("UPDATE product_view SET date=%s WHERE user_id=%s AND product_id=%s",
                            (now_time, uid, product_id))
            else:
                cur.execute("INSERT INTO product_view(user_id, product_id) VALUES(%s, %s)", (uid, product_id))
                mysql.connection.commit()
        return render_template('view_product_f1.html', x=x, f1=product, form=form)
    elif 'order' in request.args:
        product_id = request.args['order']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
        product = curso.fetchall()
        x = content_based_filtering(product_id)
        return render_template('order_product_f1.html', x=x, f1=product, form=form)
    return render_template('f1.html', f1=products, form=form)

@app.route('/admin_login', methods=['GET', 'POST'])
@not_admin_logged_in
def admin_login():
    if request.method == 'POST':
        # GEt user form
        username = request.form['email']
        password_candidate = request.form['password']

        # Create cursor
        cur = mysql.connection.cursor()

        # Get user by username
        result = cur.execute("SELECT * FROM admin WHERE email=%s", [username])

        if result > 0:
            # Get stored value
            data = cur.fetchone()
            password = data['password']
            uid = data['id']
            name = data['firstName']

            session['admin_logged_in'] = True
            session['admin_uid'] = uid
            session['admin_name'] = name

            return redirect(url_for('admin'))

        else:
            flash('Username not found', 'danger')
            # Close connection
            cur.close()
            return render_template('pages/login.html')
    return render_template('pages/login.html')

@app.route('/admin_out')
def admin_logout():
    if 'admin_logged_in' in session:
        session.clear()
        return redirect(url_for('admin_login'))
    return redirect(url_for('admin'))

@app.route('/FAQ1')
def FAQ1():
    return render_template('FAQ1.html')
@app.route('/FAQ2')
def FAQ2():
    return render_template('FAQ2.html')
@app.route('/FAQ3')
def FAQ3():
    return render_template('FAQ3.html')
@app.route('/FAQ4')
def FAQ4():
    return render_template('FAQ4.html')
@app.route('/FAQ5')
def FAQ5():
    return render_template('FAQ5.html')

@app.route('/admin')
@is_admin_logged_in
def admin():
    curso = mysql.connection.cursor()
    num_rows = curso.execute("SELECT * FROM products")
    result = curso.fetchall()
    order_rows = curso.execute("SELECT * FROM orders")
    users_rows = curso.execute("SELECT * FROM users")
    return render_template('pages/index.html', result=result, row=num_rows, order_rows=order_rows,
                           users_rows=users_rows)

class DeleForm(Form):
    id = StringField('', [validators.length(min=0), validators.DataRequired()])
    condi = StringField('', [validators.length(min=0), validators.DataRequired()])

@app.route('/orders', methods=["GET","POST"])
@is_admin_logged_in
def orders():
    form = DeleForm(request.form)
    id = form.id.data
    condi = form.condi.data
    curso = mysql.connection.cursor()
    num_rows = curso.execute("SELECT * FROM products")
    order_rows = curso.execute("SELECT * FROM all_orders ORDER BY id DESC")
    result = curso.fetchall()
    users_rows = curso.execute("SELECT * FROM users")
    if request.method == 'POST' and form.validate():
        if condi == '배송중':
            cur = mysql.connection.cursor()
            cur.execute('UPDATE buy_product1 SET condi=%s WHERE id=%s', (condi,id,))
            cur.execute('CREATE OR REPLACE VIEW all_orders AS SELECT id,ofname,username,pid,quantity,dstatus,odate,ddate,pName,price,total_price,condi,rmobile1,rmobile2,rmobile3,addnum,oplace,oplacee,oplaced,memo FROM buy_product1 INNER JOIN buy_product2 USING (ofname)')
            mysql.connection.commit()
            cur.close()
        return redirect(url_for('orders'))
    return render_template('pages/all_orders.html', result=result, row=num_rows, order_rows=order_rows,
                           users_rows=users_rows)

@app.route('/users')
@is_admin_logged_in
def users():
    curso = mysql.connection.cursor()
    num_rows = curso.execute("SELECT * FROM products")
    order_rows = curso.execute("SELECT * FROM orders")
    users_rows = curso.execute("SELECT * FROM users")
    result = curso.fetchall()
    return render_template('pages/all_users.html', result=result, row=num_rows, order_rows=order_rows,
                           users_rows=users_rows)

@app.route('/helped')
@is_admin_logged_in
def helped():
    curso = mysql.connection.cursor()
    num_rows = curso.execute("SELECT * FROM products")
    order_rows = curso.execute("SELECT * FROM orders")
    users_rows = curso.execute("SELECT * FROM users")
    help_rows = curso.execute('SELECT * FROM help')
    result = curso.fetchall()
    return render_template('pages/all_helps.html', result=result, row=num_rows, order_rows=order_rows,
                           users_rows=users_rows,help_rows=help_rows)

@app.route('/mypage')
def mypage():
    if 'uid' in session:
        uid = session['uid']
        ofname = session['s_name']
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM all_orders WHERE ofname=%s ORDER BY id DESC', (ofname,))
        result = cur.fetchall()
        cur.execute('SELECT * FROM help WHERE name=%s ORDER BY id DESC', (ofname,))
        help = cur.fetchall()
        cur.close()
        return render_template('mypage.html', result=result, help=help)
    elif 'ofname' in session:
        ofname = session['ofname']
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM all_orders WHERE ofname=%s ORDER BY id DESC', (ofname,))
        result = cur.fetchall()
        cur.execute('SELECT * FROM help WHERE name=%s ORDER BY id DESC', (ofname,))
        help = cur.fetchall()
        cur.close()
        return render_template('mypage.html', result=result, help=help)
    return render_template('mypage.html')

@app.route('/admin_add_product', methods=['POST', 'GET'])
@is_admin_logged_in
def admin_add_product():
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form['price']
        description = request.form['description']
        available = request.form['available']
        category = request.form['category']
        item = request.form['item']
        code = request.form['code']
        file = request.files['picture']
        if name and price and description and available and category and item and code and file:
            pic = file.filename
            photo = pic.replace("'", "")
            picture = photo.replace(" ", "_")
            if picture.lower().endswith(('.png', '.jpg', '.jpeg')):
                save_photo = photos.save(file, folder=category)
                if save_photo:
                    # Create Cursor
                    curs = mysql.connection.cursor()
                    curs.execute("INSERT INTO products(pName,price,description,available,category,item,pCode,picture)"
                                 "VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",
                                 (name, price, description, available, category, item, code, picture))
                    mysql.connection.commit()
                    product_id = curs.lastrowid
                    curs.execute("INSERT INTO product_level(product_id)" "VALUES(%s)", [product_id])
                    if category == 'tshirt':
                        level = request.form.getlist('tshirt')
                        for lev in level:
                            yes = 'yes'
                            query = 'UPDATE product_level SET {field}=%s WHERE product_id=%s'.format(field=lev)
                            curs.execute(query, (yes, product_id))
                            # Commit cursor
                            mysql.connection.commit()
                    elif category == 'wallet':
                        level = request.form.getlist('wallet')
                        for lev in level:
                            yes = 'yes'
                            query = 'UPDATE product_level SET {field}=%s WHERE product_id=%s'.format(field=lev)
                            curs.execute(query, (yes, product_id))
                            # Commit cursor
                            mysql.connection.commit()
                    elif category == 'belt':
                        level = request.form.getlist('belt')
                        for lev in level:
                            yes = 'yes'
                            query = 'UPDATE product_level SET {field}=%s WHERE product_id=%s'.format(field=lev)
                            curs.execute(query, (yes, product_id))
                            # Commit cursor
                            mysql.connection.commit()
                    elif category == 'shoes':
                        level = request.form.getlist('shoes')
                        for lev in level:
                            yes = 'yes'
                            query = 'UPDATE product_level SET {field}=%s WHERE product_id=%s'.format(field=lev)
                            curs.execute(query, (yes, product_id))
                            # Commit cursor
                            mysql.connection.commit()
                    else:
                        flash('Product level not fund', 'danger')
                        return redirect(url_for('admin_add_product'))
                    # Close Connection
                    curs.close()

                    flash('Product added successful', 'success')
                    return redirect(url_for('admin_add_product'))
                else:
                    flash('Picture not save', 'danger')
                    return redirect(url_for('admin_add_product'))
            else:
                flash('File not supported', 'danger')
                return redirect(url_for('admin_add_product'))
        else:
            flash('Please fill up all form', 'danger')
            return redirect(url_for('admin_add_product'))
    else:
        return render_template('pages/add_product.html')


@app.route('/edit_product', methods=['POST', 'GET'])
@is_admin_logged_in
def edit_product():
    if 'id' in request.args:
        product_id = request.args['id']
        curso = mysql.connection.cursor()
        res = curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
        product = curso.fetchall()
        curso.execute("SELECT * FROM product_level WHERE product_id=%s", (product_id,))
        product_level = curso.fetchall()
        if res:
            if request.method == 'POST':
                name = request.form.get('name')
                price = request.form['price']
                description = request.form['description']
                available = request.form['available']
                category = request.form['category']
                item = request.form['item']
                code = request.form['code']
                file = request.files['picture']
                # Create Cursor
                if name and price and description and available and category and item and code and file:
                    pic = file.filename
                    photo = pic.replace("'", "")
                    picture = photo.replace(" ", "")
                    if picture.lower().endswith(('.png', '.jpg', '.jpeg')):
                        file.filename = picture
                        save_photo = photos.save(file, folder=category)
                        if save_photo:
                            # Create Cursor
                            cur = mysql.connection.cursor()
                            exe = curso.execute(
                                "UPDATE products SET pName=%s, price=%s, description=%s, available=%s, category=%s, item=%s, pCode=%s, picture=%s WHERE id=%s",
                                (name, price, description, available, category, item, code, picture, product_id))
                            if exe:
                                if category == 'tshirt':
                                    level = request.form.getlist('tshirt')
                                    for lev in level:
                                        yes = 'yes'
                                        query = 'UPDATE product_level SET {field}=%s WHERE product_id=%s'.format(
                                            field=lev)
                                        cur.execute(query, (yes, product_id))
                                        # Commit cursor
                                        mysql.connection.commit()
                                elif category == 'wallet':
                                    level = request.form.getlist('wallet')
                                    for lev in level:
                                        yes = 'yes'
                                        query = 'UPDATE product_level SET {field}=%s WHERE product_id=%s'.format(
                                            field=lev)
                                        cur.execute(query, (yes, product_id))
                                        # Commit cursor
                                        mysql.connection.commit()
                                elif category == 'belt':
                                    level = request.form.getlist('belt')
                                    for lev in level:
                                        yes = 'yes'
                                        query = 'UPDATE product_level SET {field}=%s WHERE product_id=%s'.format(
                                            field=lev)
                                        cur.execute(query, (yes, product_id))
                                        # Commit cursor
                                        mysql.connection.commit()
                                elif category == 'shoes':
                                    level = request.form.getlist('shoes')
                                    for lev in level:
                                        yes = 'yes'
                                        query = 'UPDATE product_level SET {field}=%s WHERE product_id=%s'.format(
                                            field=lev)
                                        cur.execute(query, (yes, product_id))
                                        # Commit cursor
                                        mysql.connection.commit()
                                else:
                                    flash('Product level not fund', 'danger')
                                    return redirect(url_for('admin_add_product'))
                                flash('Product updated', 'success')
                                return redirect(url_for('edit_product'))
                            else:
                                flash('Data updated', 'success')
                                return redirect(url_for('edit_product'))
                        else:
                            flash('Pic not upload', 'danger')
                            return render_template('pages/edit_product.html', product=product,
                                                   product_level=product_level)
                    else:
                        flash('File not support', 'danger')
                        return render_template('pages/edit_product.html', product=product,
                                               product_level=product_level)
                else:
                    flash('Fill all field', 'danger')
                    return render_template('pages/edit_product.html', product=product,
                                           product_level=product_level)
            else:
                return render_template('pages/edit_product.html', product=product, product_level=product_level)
        else:
            return redirect(url_for('admin_login'))
    else:
        return redirect(url_for('admin_login'))


@app.route('/search', methods=['POST', 'GET'])
def search():
    form = OrderForm(request.form)
    if 'q' in request.args:
        q = request.args['q']
        # Create cursor
        cur = mysql.connection.cursor()
        # Get message
        query_string = "SELECT * FROM products WHERE pName LIKE %s ORDER BY id ASC"
        cur.execute(query_string, ('%' + q + '%',))
        products = cur.fetchall()
        # Close Connection
        cur.close()
        flash('Showing result for: ' + q, 'success')
        return render_template('search.html', products=products, form=form)
    else:
        flash('Search again', 'danger')
        return render_template('search.html')


@app.route('/profile')
@is_logged_in
def profile():
    if 'user' in request.args:
        q = request.args['user']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM users WHERE id=%s", (q,))
        result = curso.fetchone()
        if result:
            if result['id'] == session['uid']:
                curso.execute("SELECT * FROM orders WHERE uid=%s ORDER BY id ASC", (session['uid'],))
                res = curso.fetchall()
                return render_template('profile.html', result=res)
            else:
                flash('Unauthorised', 'danger')
                return redirect(url_for('login'))
        else:
            flash('Unauthorised! Please login', 'danger')
            return redirect(url_for('login'))
    else:
        flash('Unauthorised', 'danger')
        return redirect(url_for('login'))


class UpdateRegisterForm(Form):
    name = StringField('Full Name', [validators.length(min=3, max=50)],
                       render_kw={'autofocus': True, 'placeholder': 'Full Name'})
    email = EmailField('Email', [validators.DataRequired(), validators.Email(), validators.length(min=4, max=25)],
                       render_kw={'placeholder': 'Email'})
    password = PasswordField('Password', [validators.length(min=3)],
                             render_kw={'placeholder': 'Password'})
    mobile = StringField('Mobile', [validators.length(min=11, max=15)], render_kw={'placeholder': 'Mobile'})


@app.route('/settings', methods=['POST', 'GET'])
@is_logged_in
def settings():
    form = UpdateRegisterForm(request.form)
    if 'user' in request.args:
        q = request.args['user']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM users WHERE id=%s", (q,))
        result = curso.fetchone()
        if result:
            if result['id'] == session['uid']:
                if request.method == 'POST' and form.validate():
                    name = form.name.data
                    email = form.email.data
                    password = sha256_crypt.encrypt(str(form.password.data))
                    mobile = form.mobile.data

                    # Create Cursor
                    cur = mysql.connection.cursor()
                    exe = cur.execute("UPDATE users SET name=%s, email=%s, password=%s, mobile=%s WHERE id=%s",
                                      (name, email, password, mobile, q))
                    if exe:
                        flash('Profile updated', 'success')
                        return render_template('user_settings.html', result=result, form=form)
                    else:
                        flash('Profile not updated', 'danger')
                return render_template('user_settings.html', result=result, form=form)
            else:
                flash('Unauthorised', 'danger')
                return redirect(url_for('login'))
        else:
            flash('Unauthorised! Please login', 'danger')
            return redirect(url_for('login'))
    else:
        flash('Unauthorised', 'danger')
        return redirect(url_for('login'))


class DeveloperForm(Form):  #
    id = StringField('', [validators.length(min=1)],
                     render_kw={'placeholder': 'Input a product id...'})


@app.route('/developer', methods=['POST', 'GET'])
def developer():
    form = DeveloperForm(request.form)
    if request.method == 'POST' and form.validate():
        q = form.id.data
        curso = mysql.connection.cursor()
        result = curso.execute("SELECT * FROM products WHERE id=%s", (q,))
        if result > 0:
            x = content_based_filtering(q)
            wrappered = wrappers(content_based_filtering, q)
            execution_time = timeit.timeit(wrappered, number=0)
            seconds = ((execution_time / 1000) % 60)
            return render_template('developer.html', form=form, x=x, execution_time=seconds)
        else:
            nothing = 'Nothing found'
            return render_template('developer.html', form=form, nothing=nothing)
    else:
        return render_template('developer.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
