from autos import process_file


def insert_autos(infile, db):
    autos = process_file(infile)
    for a in autos:
        db.autos.insert(a)


if __name__ == "__main__":

    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.examples

    insert_autos('./data/autos.csv', db)

    print db.autos.find_one()
    print db.autos.count()

