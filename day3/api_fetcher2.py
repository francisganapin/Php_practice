from flask import Flask,jsonify

app = Flask(__name__)


data_list = [
    {
        "id": 1,
        "name": "John Doe",
        "age": 28,
        "membershipType": "Premium",
        "joinDate": "2023-05-15",
        "activeStatus": True
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "age": 34,
        "membershipType": "Basic",
        "joinDate": "2022-09-10",
        "activeStatus": True
    },
    {
        "id": 3,
        "name": "Mike Johnson",
        "age": 40,
        "membershipType": "Standard",
        "joinDate": "2021-03-20",
        "activeStatus": True
    }
]


@app.route('/data/2')
def member_list():
    member_data = data_list
    return jsonify(member_data)


if __name__ == '__main__':
    app.run(debug=True)