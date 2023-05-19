from flask import Flask,jsonify, render_template, request
import json


app = Flask(__name__)
jData = json.loads(open('./marvel.json').read())
data=jData["MarvelMovies"]

@app.route('/')
def marvel_main():
    return render_template("index.html")

@app.route('/getmovies/')
def marvel_all():
    myList=[]
    for element in data:
        myList.append(element)
    result = jsonify(myList)
    return render_template("index.html",items=myList)

@app.route('/getmovies/<string:Year>/')
def marvel(Year=''):
    myList=[]
    for element in data:
        if element["Year"] == Year:
            myList.append(element)
    result = jsonify(myList)
    return render_template("index.html",items=myList)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
