import pymongo
import os

conn_str = "mongodb://127.0.0.1:20170"

local_conn_str = os.environ.get('local-ttmik-db')
cloud_conn_str = os.environ.get('cloud-ttmik-db')
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)


# Cloud instance connection string

# mongodb+srv://root:toor@ttmikclone.s0e2a.mongodb.net/myFirstDatabase?retryWrites=true&w=majority