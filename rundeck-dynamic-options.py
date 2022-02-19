#!/usr/bin/python
# supplied as-is, with no warranty or ownership implied.
# Jroberts (2022)

import csv,json,sys
from flask import Flask

basedir= sys.argv[1] 
portnumber= sys.argv[2] 
app = Flask(__name__)
@app.route("/options/<listname>")
def showlist(listname):
    try:
        with open(basedir+listname+".list", newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
            listToStr = ' '.join([str(elem) for elem in data])
            jsonString = json.dumps(listToStr)
            resp = app.make_response(listToStr)
            resp.headers['Content-Type'] = 'application/json'
            return (resp)
    except:
            return  "List " +listname + " threw an error. Is it there ? Is it formatted well?"
if __name__ == "__main__":
    app.run(debug=False,host='localhost', port=portnumber)
