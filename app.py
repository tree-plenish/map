import flask
from flask import Flask, render_template, request, jsonify
import json
app = Flask(__name__)

#home page
@app.route('/index')
@app.route('/')
def index():
    return render_template("index.html")

#school-specific pages
@app.route('/school')
def school():
    schoolName = request.args["school"].strip()
    try:
        with open('./static/schoolData.json', 'r') as f:
            data = json.load(f)
            treeReqs = data[schoolName]['Tree Requests']
            treeGoal = data[schoolName]['Tree Goal']
            prog = data[schoolName]['Tree Progress']
        return render_template("school.html", name=schoolName, treeRequests = treeReqs, treeGoal =  treeGoal, progress=prog)
    except:
        return render_template("school_not_found.html")

# version 2
# @app.route('/school')
# def school():
#     schoolName = request.args["school"].strip()
#     filePath = "../static/allSchoolData.json"
#     try:
#         with open(filePath, 'r') as f:
#             data = json.load(f)[schoolName]
#             #get data and give it to the template in the form of a dictionary
#             schoolData = {}
#             #blah blah code blah blah
#             render_template("school.html", schoolData)
#     except:
#         return render_template("school_not_found.html")

#full analytics page
@app.route('/analytics')
def analytics():
    return render_template("analytics.html") 

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
