from flask import Flask,render_template_string

app = Flask(__name__)

@app.route('/')
def index():

    data =[
    {'name':"francis","age":30},
    {'name':"trisha","age":24},
    {'name':"fire","age":31}
    ]


    table_template = '''
            <table>
            <thead>
                <tr>
                <td>Name</td>
                <td>Age</td>
                </tr>
                </thead>
                <tbody>
                {%for item in data %}
                <tr>
             
                <td>{{item.name}}</td> 
                <td>{{item.age}}</td>
            
                </tr>
                {%endfor%}
                </tbody>
            </table>
'''
    return render_template_string(table_template,data=data)


if __name__ == '__main__':
    app.run(debug=True)