from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():

    product = [
        {'name':'laptop','price':1200,'stock':8},
        {'name':'Smartphone','price':800,'stock':12},
        {'name':'Tablet','price':500,'stock':8}
    ]

    return render_template('index2.html',products=product)


if __name__ == '__main__':
    app.run(debug=True)