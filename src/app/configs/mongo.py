from pymongo import MongoClient
from mongoengine import connect
import app.configs.variables as var

MONGO_HOST = var.get('MONGO_HOST')
MONGO_PORT = int(var.get('MONGO_PORT'))
MONGO_BASE = var.get('MONGO_BASE')
MONGO_USER = var.get('MONGO_USER')
MONGO_PASS = var.get('MONGO_PASS')

# pymongo
coneccion_str = f'mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_BASE}?authSource=admin'
cliente = MongoClient(coneccion_str).get_database(name=MONGO_BASE)

# mongoengine
connect(MONGO_BASE,
        username=MONGO_USER,
        password=MONGO_PASS,
        authentication_source='admin')
