"""
Complete the insert_data function to insert the data into MongoDB.
"""

import json

def insert_data(data, db):
    for i in data:
        db.arachnid.insert(i)
    


if __name__ == "__main__":
    
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.examples

    with open('./data/arachnid.json') as f:
        data = json.loads(f.read())
        insert_data(data, db)
        print db.arachnid.find_one()


