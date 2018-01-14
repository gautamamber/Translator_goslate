from flask import Flask, render_template, request
import goslate
app = Flask(__name__)
@app.route('/')
def home():
	return render_template('home.html')
@app.route('/trans' , methods = ['POST'])
def trans():
	lang = request.form['trans']
	ch = request.form['choose']
	gs = goslate.Goslate()
	ts = gs.translate(lang, ch)
	return render_template('new.html' , ts = ts)



	
if __name__ == '__main__':
	app.secret_key = 'secret123'
	app.run(debug = True)