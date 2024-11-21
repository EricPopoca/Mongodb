
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://Popoca:palito13@cluster0.daz2x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    mydb = client["APIS"]
    mycol = mydb["alumnos"]

    x = mycol.insert_one({
        'nombre':'Eric',
        'Edad':20
    })
    #print the result:
    print(x)
except Exception as e:
    print(e)