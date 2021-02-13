import pymongo
from flask import jsonify

myclient = pymongo.MongoClient("mongodb+srv://ankush053:gPwP79NEJ57qD4Xn@cluster0.koh9g.mongodb.net")

mydb = myclient["my_database"]  

mycol = mydb["users"]

data = [
    {
    "name": "Aman",
    "LName": "singh"
    },
    {
    "name": "deepak",
    "LName": "yadu"
    }
]

# x = mycol.find_one()
# print(x)

for x in mycol.find():
    print(x)