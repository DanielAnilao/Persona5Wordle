from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo

from flask import Flask
from flask import abort

from bson import json_util
import json
import bson
from bson.json_util import dumps

#connections
uri = "mongodb+srv://danielanilao848:HOnXsksC9m55A0H1@persodle.ai11e.mongodb.net/?retryWrites=true&w=majority&appName=Persodle"
app = Flask(__name__)

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
database = client["Compendium"]
collection = database["Personas"]

random_document = (collection.aggregate([{"$sample":{"size":1}}]).next())

json_data = dumps(random_document)
data = json.loads(json_data)


name = data["Name"]
arcana = data["Arcana"]
inherit = (data["Inherit"])
physical = (data["Physical"])
gun = data["Gun"]
fire = data["Fire"]
ice = data["Ice"]
wind = data["Wind"]
elec = data["Electric"]
psycho = data["Psychic"]
nuc = data["Nuclear"]
bless = data["Bless"] 
curse = data["Curse"]

print(json_data)
print(name)
print(arcana)
print(inherit)
print(physical)
print(gun)
print(fire)
print(ice)
print(wind)
print(elec)
print(nuc)
print(psycho)
print(bless)
print(curse)
