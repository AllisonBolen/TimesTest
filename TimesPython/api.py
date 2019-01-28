# Write a function for each RESTful operation for a resource named “document.”
# Make sure each CRUD operation are represented by a single function.
# The hostname can be arbitrary.
from flask import Flask
from flask import request
import json

'''
GET
POST
PUT
PATCH
DELETE
'''

app = Flask(__name__)

@app.route("/document", methods=['GET'])
def get():
    '''ex req:
        curl -X GET http://127.0.0.1:5000/document
    '''
    loadJson()
    yeet = printData()
    return "Document Contents:" + yeet

@app.route("/document", methods=['POST'])
def post():
    '''ex req:
        curl -i -H "Content-Type: application/json" -X POST -d '{"A":"YES", "Q":"This is super cool, right?"}' http://localhost:5000/document
    '''
    req = request.get_json()
    if("Q" in req and "A" in req):
        Q = req.get('Q', '')
        A = req.get('A', '')
        info = loadJson()

        string = '{'+'\"A\":\"'+A+'\",\"Q\":\"'+Q+'\"}'
        test = json.loads(string)

        info["Questions"][len(info['Questions'])+1]=test
        saveJson(info)
        return "You added the answer: "+ A + " to question " + Q +"."
    return "Didnt create a new question answer pair."

@app.route("/document", methods=["PATCH"])
def patch():
    '''
    ex req:
        curl -i -H "Content-Type: application/json" -X PATCH -d '{"A":"SURE", "num":"2"}' http://localhost:5000/document

    '''
    req = request.get_json()

    if("Q" in req and "num" in req):
        num = req.get('num', '')
        Q = req.get('Q', '')
        info = loadJson()

        info["Questions"][num]['Q']=Q
        saveJson(info)
        return "You edited question "+num+" to: "+ Q

    if "A" in req and "num" in req:
        num = req.get('num', '')
        info = loadJson()
        A = req.get('A', '')

        info["Questions"][num]["A"] = A

        saveJson(info)
        return "You edited the answer: "+ A + " to question " + num +"."
    return "Nothing Changed"

@app.route("/document", methods=["PUT"])
def putEdit():
    '''
    ex req:
        curl -i -H "Content-Type: application/json" -X PUT -d '{"A":"YES", "num":"2"}' http://localhost:5000/document
    '''
    req = request.get_json()

    if("Q" in req and "A" in req and "num" in req):
        num = req.get('num', '')
        Q = req.get('Q', '')
        A = req.get('A', '')
        info = loadJson()

        string = '{'+'\"A\":\"'+A+'\",\"Q\":\"'+Q+'\"}'
        test = json.loads(string)

        info["Questions"][num] = test
        saveJson(info)
        return "You edited the answer and question for section : " + num + "."
    return "You didn't edit a question & answer pair."

@app.route("/document", methods=["DELETE"])
def deleteEdit():
    '''
    ex req:
        curl -i -H "Content-Type: application/json" -X DELETE -d '{"A":"NO", "num":"2"}' http://localhost:5000/document
    '''
    req = request.get_json()

    if("Q" in req and "A" in req and "num" in req):
        num = req.get('num', '')
        Q = req.get('Q', '')
        A = req.get('A', '')
        info = loadJson()
        info["Questions"][num] = ""
        saveJson(info)
        return "You deleted Question Answer pair: " + num

    elif "A" in req and "num" in req:
        num = req.get('num', '')
        info = loadJson()
        A = req.get('A', '')
        info["Questions"][num]['A']=""
        saveJson(info)
        return "You deleted Answer: " + num

    elif("Q" in req and "num" in req):
        num = req.get('num', '')
        Q = req.get('Q', '')
        info = loadJson()

        info["Questions"][num]['Q']=""
        saveJson(info)
        return "You deleted Question: " + num

    return "Nothing deleted"
    saveJson(info)


def saveJson(info):
    with open('data.json', 'w') as outfile:
        json.dump(info, outfile)

def loadJson():
    data = ""
    with open('data.json') as f:
        data = json.load(f)
    return data

def printData():
    info = loadJson()

    formated = "\nQuestions: "
    for item in info['Questions']:
        formated += "\n\t"+info['Questions'][item]['Q']
        if info['Questions'][item]['A'] is not None:
            formated += "\n\tAnswer: "+info["Questions"][item]["A"]
    return formated
