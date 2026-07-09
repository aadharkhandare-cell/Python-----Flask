from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def marks():
	return render_template("index.html",marks=65)
	
if __name__=='_main__':
	app.run(debug=True,port=5000)
	
	