from flask import Flask, render_template

app = Flask(__name__)


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


@app.route('/home')
def home():
    return render_template('example.html')


if __name__ == '__main__':
    app.run(debug=True)
