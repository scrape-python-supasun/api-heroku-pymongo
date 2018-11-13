"# api-heroku-pymongo" 
สิ่งที่รู้เท่าที่จำได้
1.เครื่อมือที่ใช้มี virtualenv โดยใช้Scripts\activateตลอดเวลา เเล้วใช้pip freezeเพื่อดูว่าเรามีอะไรบ้างอย่างในที่นี้ต้องโหลด
pip install flask_restful, pip install flask, pip install flask_pymongo, pip install gunicorn โดยทั้ง4เอามาจากfromของไฟล์addapihistoryday.pyต้องทำหลังคำสั่งScripts\activate
จากนั้นใช้คำสั้ง pip freeze ว่ามี4อันที่เราต้องการไหม จากนั้นใช้คำสั่ง pip freeze > requirements.txt
https://medium.com/@nonthakon/virtualenv-%E0%B9%83%E0%B8%99-python-3-windows-10d3dd89a0a7
2.gunicorn คือไฟล์ที่เอาไฟล์เราเชื่อมต่อapi เช่นในไฟล์gunicornเรา คำสั่งweb: gunicorn addapihistoryday:app ให้เปลี่ยนเเค่ addapihistorydayตามซื่อไฟล์ที่เราจะเชื่อมกับapi
3.ไฟล์นี้ถ้าลงapiในherokuจะได้https://historyday.herokuapp.com/calendar?date=1208 เเต่ถ้าใช้คำสั่งpython ตามด้วยซื่อไฟล์apiของเรา.pyก็จะได้127.0.0.1/calendar?date=1208 โดยเปนการให้ข้อมูลเกี่ยวกับวันสำคัญ2ตัวเเรกคือวัน2ตัวหลังคือเดือนถ้าไม่เจอวันนั้นคือไม่มีวันสำคัญ
4.ใช้ heroku logs --tailในการรัน heroku api
5.ถ้าจะรัน flask จะต้องใช้set FLASK_APP=hello.py โดยhello.pyคือซื่อไฟล์ของเราจากนั้นพิมคำสั่งflask run
6.beautiful soup # a = soup.find_all("a", attrs={"class": "sister"}) คือ <a class"sister"></a>
โดยต้องimport
import urllib
from bs4 import BeautifulSoup
import re
เเละใช้คำสั่ง
r = urllib.request.urlopen('http://www.tewfree.com/%E0%B8%A7%E0%B8%B1%E0%B8%99%E0%B8%AA%E0%B8%B3%E0%B8%84%E0%B8%B1%E0%B8%8D%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B9%84%E0%B8%97%E0%B8%A2/').read() <===คือเว็บที่เราจะดึงข้อมูล
soup = BeautifulSoup(r ,'html.parser')
print(soup)เพื่อที่จะดูข้อมูลในเว็บ
7.เราจะใช้pymongoเราต้องเข้าไปที่resourcesของmlabจากนั้น add mlabเเล้วกดไปที่setting กดที่reveal config vars จากนั้นก็อปไปไฟล์ที่เราจะเชื่อมกับpymongoก็คือhistoryday.pyโดยพิมคำสั่งเข้าไปเช่น
import pymongo
from pymongo import MongoClient
uri = "mongodb://heroku_x8cpgsr1:gpuotu8ahk87ti53c483o94et2@ds161183.mlab.com:61183/heroku_x8cpgsr1" <==ดูจากsetting กดที่reveal config vars
client = MongoClient(uri)
db = client["heroku_x8cpgsr1"]
collections = db['historyday'] <==ถานข้อมูลซื่อ
เเล้วใช้function คือ databaseHistoryDay() ในไฟล์history.day
8.โดยฟังชั่นHeaderDayHistory()คือหัวข้อ, contentDayHistory()คือเนื้อหา, numberOfDetail()ลำดับid,allDataHistoryDay() คือรวมทั้ง3ฟังชั่น ,ฟั่งชั้นdatabaseHistoryDay()คือดึงเข้าpymongoโดยสามารถดูได้ทางmlab
=======================================================
ไฟล์addapihistoryday
1.app.config['MONGO_URI'] = 'mongodb://heroku_x8cpgsr1:gpuotu8ahk87ti53c483o94et2@ds161183.mlab.com:61183/heroku_x8cpgsr1'<==ดูจากsetting กดที่reveal config 
2.ฟังชั่นdateเเปลงurlเปน4ตัวเช่นhttps://historyday.herokuapp.com/calendar?date=1208 1208คือตัวที่เราจะเเสดง
โดยมีฟังชั้น
parser = reqparse.RequestParser()
parser.add_argument('date', type=str)<===คือuriเว็บตัวdate==
3.ในฟังชั่น calendarDay คือเชื่อมapi heroku
โดยใช้
args = parser.parse_args()
calendar = args['date'] # เอาค่าฟังชั่นเก็บในcalendar
4.
try:
    query = {"contentData": date(calendar)} <==เอาฟังชั่นมาใช้
    projection = {'_id':False}<==ไม่เอา_idเพราะไม่จำเป็น
    historyData = mongo.db.historyday.find(query, projection)รวมทั้งสอง
    return jsonify(historyData[0])<==ต้องทำให้มันออกมาจากlist
except:
    return 'Not found'<==หาไม่เจอurlให้ปริ้นอันนี้
 
5.api.add_resource(calendarDay, '/calendar')<==คือตัวcalendar https://historyday.herokuapp.com/calendar?date=1208
6.พิม
if __name__ == '__main__':
    app.run(debug=True)
    
****อย่าลืม กด deployในherokuเเล้วpushเหมือนgithub


