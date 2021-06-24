from flask import Flask, render_template, url_for, flash, redirect
from flask import request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
    	SMS = request.form['SMS']
    	data = [SMS]
    	vectorized = cv.transform(data).toarray()
    	my_prediction = classifier.predict(vectorized)
    	return render_template('result.html', prediction = my_prediction)

if __name__ == '__main__':
    app.run(debug=False)