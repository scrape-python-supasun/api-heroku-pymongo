from flask_restful import Resource, Api, reqparse
from flask import Flask, jsonify, render_template, request
from flask_pymongo import PyMongo
import json

from bson.json_util import dumps


# วิธีรัน 
# 1.set FLASK_APP=addapihistoryday.py
# 2.flask run

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://heroku_x8cpgsr1:gpuotu8ahk87ti53c483o94et2@ds161183.mlab.com:61183/heroku_x8cpgsr1'
mongo = PyMongo(app)
api = Api(app)

# user = mongo.db.historyday.find_one_or_404({"historyData":HeaderDetail[element]})

parser = reqparse.RequestParser()
parser.add_argument('date', type=str)
# dictp = parser.parse_args()
def date(date):
    day = date[:2]
    month = date[2:]
    mouthList = {
      "01": "มกราคม",
      "02": "กุมภาพันธ์",
      "03": "มีนาคม",
      "04": "เมษายน",
      "05": "พฤษภาคม",
      "06": "มิถุนายน",
      "07": "กรกฎาคม",
      "08": "สิงหาคม",
      "09": "กันยายน",
      "10": "ตุลาคม",
      "11": "พฤศจิกายน",
      "12": "ธันวาคม"
    }
    dayList = {
        "01":"1",
        "02":"2",
        "03":"3",
        "04":"4",
        "05":"5",
        "06":"6",
        "07":"7",
        "08":"8",
        "09":"9",
        "10":"10",
        "11":"11",
        "12":"12",
        "13":"13",
        "14":"14",
        "15":"15",
        "16":"16",
        "17":"17",
        "18":"18",
        "19":"19",
        "10":"10",
        "11":"11",
        "12":"12",
        "13":"13",
        "14":"14",
        "15":"15",
        "16":"16",
        "17":"17",
        "18":"18",
        "19":"19",
        "20":"20",
        "21":"21",
        "22":"22",
        "23":"23",
        "24":"24",
        "25":"25",
        "26":"26",
        "27":"27",
        "28":"28",
        "29":"29",
        "30":"30",
        "31":"31",
    }
    if day in dayList and month in mouthList:
        return dayList[day] + ' ' + mouthList[month] + ' '



class calendarDay(Resource):
    def get(self):
        # calendar = date(date)
        args = parser.parse_args()
        calendar = args['date']
        # เอาค่ามาเก็บในcalendar
        # return "Input is {}".format(date(calendar))
        try:
            query = {"contentData": date(calendar)}
            projection = {'_id':False}
            historyData = mongo.db.historyday.find(query, projection)
            return jsonify(historyData[0])
        except:
            return 'Not found'


api.add_resource(calendarDay, '/calendar')

# api.add_resource('/')
# api.add_resource(heyyou, '/heyyou',endpoint='heyyou')



if __name__ == '__main__':
    app.run(debug=True)

# วิธีดู
# 
# http://127.0.0.1:5000/calendar?date=1208

# pip freeze > requirements.txt
