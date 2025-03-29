from flask import Flask,request,jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
CORS(app)

if not os.path.exists('instance'):
    os.makedirs('instance')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Booking(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

with app.app_context():
    db.create_all()


@app.route('/save/database/3',methods=['POST'])
def save_data():
    data = request.json
    username = data.get('username')
    email = data.get('email')

    if not username or not email:
        return jsonify({'error':'Missing value: name or email'}),400

    try:
        new_user = Booking(username=username,email=email)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message':'Data saved successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error':str(e)}),500
    
if __name__ == '__main__':
    app.run(debug=True)