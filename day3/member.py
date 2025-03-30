from flask import Flask,request,jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os



app = Flask(__name__)
CORS(app)

if not os.path.exists('instance'):
    os.makedirs('instance')


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data2.db'
app.config['SQLALCHEMY_TRACK_MONDIFICATIONS'] = False

db = SQLAlchemy(app)

class Member(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    card_id = db.Column(db.String(20),nullable=False)
    first_name = db.Column(db.String(20),nullable=False)
    last_name = db.Column(db.String(20),nullable=False)
    expiry = db.Column(db.String(255),nullable=False)

with app.app_context():
    db.create_all()


@app.route('/member/register',methods=['POST'])
def register_member():
    data = request.json
    
    try:
        
        context = Member(
               card_id = data.get('card_id'),
               first_name = data.get('first_name'),
               last_name = data.get('last_name'),
               expiry = data.get('expiry')
        )


        db.session.add(context)
        db.session.commit()
        return jsonify({'message':f'Data saved sucessfully {context}'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error':str(e)}),

if __name__ == '__main__':
    app.run(debug=True)