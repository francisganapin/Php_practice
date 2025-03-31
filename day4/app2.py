from flask import Flask,request,redirect,url_for,render_template_string
from flask_login import LoginManager,UserMixin,login_user,login_user,logout_user,login_required,current_user


app = Flask(__name__)
app.secret_key = 'YSADZXC@!@DASVVVVASEe5123'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


users = {
    'admin':{'password':'password'}
}

class User(UserMixin):
    def __init__(self,username):
        self.id = username

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id)
    return None

@app.route('/')
def index():
    if current_user.is_authenticated:
        return render_template_string('''
        <h1>Hello,{{current_user.id}}!</h1>
        <p><a href="{{url_for('logout')}}">Logout</a><p>
''')
    return render_template_string('''
            <h1>You are not Logged in.</h1>
            <p><a href="{{url_for('login')}}">Login Here </a><p>
''')


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('index'))
        else:
            return render_template_string('''
            <h1>Invalid credentials. Please try again.</h1>
            <a href="{{url_for('login')}}">Back To Login </a>
        ''')
    
    return render_template_string('''
        <form method="post">
            <div>
                <label>Username:<input type='text' name='username'></label>
            </div>
            <div>
                <label>Password:<input type="password" name="password"></label>
            </div>
            <div>
                    <input type="submit" value="Login">
            </div>
        </form>
''')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)