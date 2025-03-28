from flask import Flask,request,jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/test_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100),nullable=False,unique=True)

def create_tables():
    db.create_all()


@app.route('/save', methods=['POST'])
def save_data():
    data = request.json
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({'error':'Missing value name or email'}),400
    
    try:
        new_user = User(name=name,email=email)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'Message':'Data saved succesffuly'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error':str(e)}),500
    
if __name__ == '__main__':
    app.run(debug=True)