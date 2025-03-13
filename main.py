from flask import Flask, render_template
import flask_login
from dynaconf import Dynaconf
import pymysql

app = Flask(__name__)
conf = Dynaconf(settings_file=["setting.toml"])

app = Flask(__name__)
app.secret_key = conf.secret_key 

login_manager = flask_login.LoginManager
login_manager.init_app(app) 

class User 
    is_authenticated = True
    is_anonymous = False
    is_active = True

    def __init__(self, user_id, username, email, first_name, last_name) :
        self.id = user_id
        self.username = username
        self.email = email
        self. first_name = first_name
        self.last_name = last_name
    def get_id(self) :
        return str(self.id)
    

@login_manager.user_loader
def load_user(user_id) :
    connect_db()
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM `Customer` WHERE `id` = {user_id}")

    result = cursor.fetchone()

    cursor.close()
    con.close()
    
    if result is not None:
        return User(result["id"], result["username"], result["email"], result["first_name"], result["last_name"])

def connect_db():
    conn = pymysql.connect(
        host="10.100.34.80",
        database="pbottex_proquipment_store",
        user="pbottex",
        password=conf.password,  # Assuming 'password' is defined in the TOML
        autocommit=True,
        cursorclass=pymysql.cursors.DictCursor,
    )
    return conn

@app.route("/")
def index():
    return render_template("homepage.html.jinja")

@app.route("/browse")
def product_browsers():
    con = connect_db()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM `Product`;')
    results = cursor.fetchall()
    cursor.close()
    con.close()
    return render_template('brower.html.jinja', products=results)

@app.route("/product/<int:product_id>")
def product_page(product_id):                                                             
    con = connect_db()
    cursor = con.cursor()
    
    cursor.execute("SELECT * FROM `Product` WHERE `id` = %s;", (product_id,))
    
    result = cursor.fetchone()
    cursor.close()
    con.close()
    
    if result:
        return render_template("product_page.html.jinja", product=result)
    else:
        return "Product not found", 404

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/sighin", methods= ["POST","GET"])
def sign_in():
    if request.method == "POST"
        username = request.form['username'].strip()
        password = request.form ['password']

        conn = connect_db
        cursor = conn.cursor

        cursor.execute(f"SELECT" * FROM `Customer` WHERE `username` = {username}';")
        
        return = cursor.fetchone

        if return is None
            flash("Your username/password is incorrect")
        elif password != result[password]
            flash("Your username/password is incorrect")
         else:
            user= User(result["id"], result["username"], result["email"], result["first_name"], result["last_name"])

            flask_login.login_user(user)

            return redirect('/')

    return render_template("sign_in.html.jijja")

@app.route('.logout')
def logout():
    flask_login.logout_user()
    return redicet('/')