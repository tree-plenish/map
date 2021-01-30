import flask
from flask import Flask, render_template, request, jsonify
import json
app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/school')
def school():
    schoolName = request.args["school"]
    return render_template("school.html", name=schoolName)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
