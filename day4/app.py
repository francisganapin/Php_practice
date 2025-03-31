from flask import Flask,request,redirect,url_for,session

app = Flask(__name__)
app.secret_key = 'sadxzeq2321@asd'

users = {
    'admin':'password'
}

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as{session['username']} <br><a href="/logout">Logout</a>'
    return 'Your are logged in. <br><a href="/login">Login here </a>'


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return 'Invalid credentials. Please try again.'
    return '''
        <form method='post'>
            <label>Username: <input type='text' name='username'></label><br>
            <label>Password: <input type='password' name='password'></label><br>
            <button type='submit'>Login</button>
        </form>
            '''

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)