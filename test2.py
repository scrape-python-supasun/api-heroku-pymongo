from flask_restful import Resource, Api, reqparse
from flask import Flask, jsonify, render_template, request
from flask_pymongo import PyMongo
import json

from bson.json_util import dumps

app = Flask(__name__)

api = Api(app)

parser = reqparse.RequestParser()
# parser.add_argument('param1', type=str)
# parser.add_argument('param2', type=str)
# parser.add_argument('param3', type=str)

# parser.add_argument('x', type=str)
# parser.add_argument('y', type=str)


parser.add_argument('num', type=str)


class testfun(Resource):
    def get(self):
        # เก็บparameter
        path = parser.parse_args()
        # x = int(path["x"])
        # y = int(path["y"])
        

        number = path["num"]
        listThree = number.split(",")

        dict = {
            "param1": listThree[0],
            "param2": listThree[1],
            "param3": listThree[2]
        }
        sum = 0
        for element in listThree:
            sum += int(element)
        
        try:
            return sum
            # return path["param1"] + path["param2"] + path["param3"]
            # http://127.0.0.1:5000/test?param1=param1&param2=param2&param3=param3
            # return 2 ** (x+y)
            #http://127.0.0.1:5000/test?x=3&y=2
        except:
            return 'Not found'


api.add_resource(testfun, '/test')

if __name__ == '__main__':
    app.run(debug=True)
