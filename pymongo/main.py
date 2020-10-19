import pymongo
from pymongo import MongoClient
from datetime import datetime

client = MongoClient()
db = client.mongo_with_python
Users = db.users

# INSERT ONE USER AT A TIME IN MONGO DB

# user_1 = {"username": "akshitone",
#           "password": "akshitone",
#           "number": 87,
#           "hobbies": ["coding", "gaming", "music"]}
# user_id = Users.insert_one(user_1).inserted_id
# user_2 = {"username": "viral",
#           "password": "viral",
#           "number": 19,
#           "hobbies": ["coding", "gaming", "music"]}
# user_id = Users.insert_one(user_2).inserted_id


# INSERT MANY USER AT A TIME

# users = [{"username": "suru195", "password": "suru195"},
#          {"username": "ashu20", "password":  "ashu20"}]

# insert_multi_user = Users.insert_many(users)
# ids = insert_multi_user.inserted_ids

count_user = Users.count_documents(
    {"hobbies": ["coding", "gaming", "music"],
     "username": "akshitone"})

print(count_user)

current_time = datetime.now()

# user_2 = {"username": "viral",
#           "password": "viral",
#           "number": 19,
#           "date": current_time,
#           "hobbies": ["coding", "gaming", "music"]}
# Users.insert_one(user_2)

count_user_has_date = Users.count_documents({"date": {"$exists": True}})
# count_user_has_date = Users.count_documents({"username": {"$ne": "viral"}})
print(count_user_has_date)
