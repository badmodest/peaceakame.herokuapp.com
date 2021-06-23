from flask import Flask, render_template, url_for, flash, redirect
from flask import request
app = Flask(__name__, template_folder='/')

@app.route('/')
def home():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)