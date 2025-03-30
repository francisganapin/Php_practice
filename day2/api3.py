from flask import Flask,request,jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
import rsa

publicKey,privateKey = rsa.newkeys(255)

app = Flask(__name__)
CORS(app)

if not os.path.exists('instance'):
    os.makedirs('instance')


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data2.db'
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),nullable=False)
    first_name = db.Column(db.String(20),nullable=False)
    last_name = db.Column(db.String(20),nullable=False)
    password = db.Column(db.String(255),nullable=False)
    email = db.Column(db.String(100),nullable=False)

with app.app_context():
    db.create_all()

@app.route('/save/database',methods=['POST'])
def save_data():
    data = request.json
    username = data.get('username')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    password = data.get('password')
    email = data.get('email')

    # encrypte the password
    encrpyt_password = rsa.encrypt(password.encode(),publicKey)

    context =[data,username,first_name,last_name,password,email]

    for item in  context:
        if item is None:
            return jsonify({'error': f'missing value at {context.index(item)}'}),400
    try:
        new_user = User(username=username,first_name=first_name,last_name=last_name,
                        password=encrpyt_password,email=email    
                        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message':'Data saved sucessfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error':str(e)}),

if __name__ == '__main__':
    app.run(debug=True)