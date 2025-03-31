from flask import Flask,render_template

app = Flask(__name__)


@app.route('/users')
def users():
    user_data = [
        {'name':'alice','age':30,'email':'alice30@gmail.com'},
        {'name':'bob','age':21,'email':'bob21@gmail.com'},
        {'name':'Charlie','age':35,'email':'charlie@gmail.com'}
    ]

    return render_template('users.html',data=user_data)

if __name__ =='__main__':
    app.run(debug=True)


    