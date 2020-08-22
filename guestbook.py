from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql12360662:8IWChv1IeW@sql12.freemysqlhosting.net/sql12360662'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sign')
def sign():
    return render_template('sign.html')


@app.route('/<place>', methods=['GET', 'POST'])
def place(place):
    links = ['https://www.hotstar.com/', 'https://facebook.com/']
    return render_template('example.html', place=place, links=links)


@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    comment = request.form['comment']
    return render_template('index.html', name=name, comment=comment)


@app.route('/home')
def home():
    return render_template('example.html')


if __name__ == '__main__':
    app.run(debug=True)
