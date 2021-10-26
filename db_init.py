import redis
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from setup import CONNECT_STR

client = MongoClient(CONNECT_STR, serverSelectionTimeoutMS=5000)
try:
    print(client.server_info())
except Exception:
    print("Unable to connect to the server.")
assistant_db: Database = client.assistant_db
abonent_collection: Collection = assistant_db.abonent


db_redis = redis.Redis(
    host='localhost',
    port=6379,
    db=0
)
