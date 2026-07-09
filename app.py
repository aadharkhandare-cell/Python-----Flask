from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return "Wekcime to flask"

@app.route('/about')
def about():
    return render_template("About.html")

@app.route('/contact')
def contact():
    return render_template("Contact.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)