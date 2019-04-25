
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = '725547f0b73c8eeb32471a3cd8b10d92'



@app.route("/")
@app.route("/home")

def home():
    return render_template('home.html')


if __name__ == '__main__':
	app.run(debug=True)