from flask import Flask, render_template, request
import model
model.start()
app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def get_predictions():
    if request.method == 'GET':
        return render_template("questionJson.html")
    query = request.form['query']
    return model.predict(query)


@app.route("/app", methods =['GET', 'POST'])
def frontend():
    if request.method == "GET":
        return render_template("question.html")
    if request.method == "POST":
        query = request.form['query']
        prediction =  model.predict(query)
        print(prediction['answers'])
        print(prediction['documents'])
        print(prediction['query'])
        return render_template("answer.html",answers = prediction['answers'], documents = prediction['documents'], query = prediction['query'])
    