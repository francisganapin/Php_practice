from flask import Flask,jsonify

app = Flask(__name__)




@app.route('/data/')
def user_list():
    user =  {'first_name':'ganapin','last_name':'francis'}
    return jsonify(user)
    

if __name__ == '__main__':
    app.run(debug=True)