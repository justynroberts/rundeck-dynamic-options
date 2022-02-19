from flask import Flask
import csv

import json

basedir ="/Users/jroberts/work/code/rundeck-dynamic-options/options/"

app = Flask(__name__)
@app.route("/options/<listname>")
def showlist(listname):
    try:
        with open(basedir+listname+".list", newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
            listToStr = ' '.join([str(elem) for elem in data])
            jsonString = json.dumps(listToStr)
            #resp = app.make_response( "{ ""name"": ""name"",""name2"": ""name2"" }")
            resp = app.make_response(listToStr)
            resp.headers['Content-Type'] = 'application/json'
            return (resp)

    except:
            return  listname + " was not found"


 
if __name__ == "__main__":
    app.run(debug=False,host='localhost', port=3000)