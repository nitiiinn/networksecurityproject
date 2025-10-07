from pymongo.mongo_client import MongoClient
import certifi

# Connection URI
uri = "mongodb+srv://nitin77kothiyal_db_user:admin123456@cluster0.ndfyvrs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client with TLS certificate
client = MongoClient(uri, tlsCAFile=certifi.where())

# Test connection
try:
    client.admin.command('ping')
    print("✅ Pinged your MongoDB deployment successfully!")
except Exception as e:
    print("❌ Connection failed:", e)
