from pymongo import MongoClient
x=MongoClient()
name=input("Enter Name")
age=int(input("Enter Age"))
db=x.sham
table=db.student
roll=0
for x in table.find():
    roll=roll+1
data={"_id":(roll+1),"name":name,"age":age}
table.insert_one(data)
print("Data saved")
