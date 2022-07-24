import pymongo


client = pymongo.MongoClient("mongodb+srv://krishna:pass3210@cluster0.zhkcb.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name" : "nikhil",
    "email" : "krishnnikhil@gmail.com",
    "surname" : "krishn"
}
db = client['mongotest']
coll = db['test']
coll.insert_one(d )