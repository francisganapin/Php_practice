from flask import Flask,render_template
import json
app = Flask(__name__)



with open('data/users.json','r') as file:
    data = json.load(file)



@app.route('/')
def index():
    data_id = []
    data_name = []
    data_age = []
    for i in data:
        data_id.append(i['id'])
        data_name.append(i['name'])
        data_age.append(i['age'])
    return f'{data_id},{data_name},{data_age}'

if __name__ == '__main__':
    app.run(debug=True)