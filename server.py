from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/ninja')
def ninjas():
    return render_template('ninja.html')

@app.route('/ninja/<color>', methods = ['GET'])
def ninja_color(color):
	if color == 'red':
		return render_template("red.html")
	elif color == 'blue':
		return render_template("blue.html")
	elif color == 'purple':
		return render_template("purple.html")
	elif color == 'orange':
		return render_template("orange.html")
	else:
            return render_template("april.html")

app.run(debug=True)