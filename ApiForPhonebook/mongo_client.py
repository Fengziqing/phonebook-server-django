# myapp/mongo_client.py
from pymongo import MongoClient

# 替换为你的MongoDB URI
MONGODB_URI = "mongodb+srv://haru:123@haruko.ynhjzzr.mongodb.net/PhoneBook?retryWrites=true&w=majority"
client = MongoClient(MONGODB_URI)
db = client['Haruko']  # 替换为你的数据库名称