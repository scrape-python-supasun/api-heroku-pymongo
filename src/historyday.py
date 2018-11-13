# languague : beautihulsoup
import urllib
from bs4 import BeautifulSoup
import re
# languague : beautihulsoup

# languague : pymongo
import pymongo
from pymongo import MongoClient
uri = "mongodb://heroku_rq8d3bm0:2ebjovmic0jkd2bqhltgt802j@ds159263.mlab.com:59263/heroku_rq8d3bm0"
client = MongoClient(uri)
db = client["heroku_rq8d3bm0"]
collections = db['historyday']
# languague : pymongo
# languague : beautihulsoup
r = urllib.request.urlopen('http://www.tewfree.com/%E0%B8%A7%E0%B8%B1%E0%B8%99%E0%B8%AA%E0%B8%B3%E0%B8%84%E0%B8%B1%E0%B8%8D%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B9%84%E0%B8%97%E0%B8%A2/').read()
soup = BeautifulSoup(r ,'html.parser')
# 
# print(soup)

# a = soup.find_all("a", text="วันที")
# a = soup.find_all("a", attrs={"class": "sister"})
# header = soup.html.find_all("strong")
# content = soup.find_all("div", attrs={"class": "entry-content-inner medium-10 columns small-12 content-inner-between"})

# languague : beautihulsoup
# languague : python
def HeaderDayHistory():
    allDataHistoryDay = soup.find_all("p")
    AllListHeader = []
    # print(contentday)
    for element in allDataHistoryDay[4:82]:
        allDataText = element.text
        myListOneData = allDataText.split("–")
        AllHeaderData = myListOneData[1]
        AllListHeader.append(AllHeaderData)
    return AllListHeader
# HeaderDetail = HeaderDayHistory()
# print(HeaderDetail)

def contentDayHistory():
    allDataHistoryDay = soup.find_all("p")
    ListAllContentData = []
    for element in allDataHistoryDay[4:82]:
        allDataText = element.text
        myListOneData = allDataText.split("–")
        AllContentData = myListOneData[0]
        ListAllContentData.append(AllContentData)
    return ListAllContentData
# contentDetail = contentDayHistory()
# print(contentDetail)

def numberOfDetail():
    numberDataList = []
    for element in range(1,79):
        numberOneList = element
        numberDataList.append(numberOneList)
    return numberDataList
numberOfData = numberOfDetail()


def allDataHistoryDay():
    HeaderDetail = HeaderDayHistory()
    contentDetail = contentDayHistory()
    numberOfData = numberOfDetail()
    listDataAll = []
    for element in range(0,78):
        mydict = {"id":numberOfData[element],"historyData":HeaderDetail[element],"contentData":contentDetail[element]}
        listDataAll.append(mydict)
    return listDataAll

allDataDay = allDataHistoryDay()
print(allDataDay)
# languague : python
# languague : pymongo
# def databaseHistoryDay():
#     allDataDay = allDataHistoryDay()
#     result = collections.insert_many(allDataDay)
#     result.inserted_ids
#     return result
# databaseHistoryDay() // ลบคอมเม้นเอาไว้ต่อmlab heroku
# languague : pymongo




