#setup
from flask import Flask, request, render_template
import generate

app = Flask(__name__)

#homepage
@app.route('/')
def home():
	#just render the page
	return render_template('index.html')

@app.route('/speech/')
def speech():
	#set text to variable
	text = request.args.get("text")
	#run the function from generate.py file
	outfile = generate.trump(text)
	outfile = outfile.replace('\n', '<br>')
	#return the same file, only with text inside
	return render_template('index.html', outfile = outfile)


if __name__ == '__main__':
	app.run(debug=True)