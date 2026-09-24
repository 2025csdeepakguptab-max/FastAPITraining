# This creates a singlee shared connection to MongoDB using pymongo

from pymongo import MongoClient
from pymongo.database import Database
from app.config import settings
# MongoClient manages a poo. of connections to the MongoDB server.
client: MongoClient = MongoClient(settings.MONGO_URI)
database: Database = client[settings.MONGO_DB_NAME]

#sends a ping command to MongoDB to confirm the connection is live
def ping_database() -> bool:
    try:
        client.admin.command("ping")
        return True
    except Exception as e:
        print(f"Error pinging MongoDB: {e}")
        return False