def get_quotes():
    results = collection.find()
    return results


if __name__ == "__main__":
    from pymongo import MongoClient

    # Connecting to the database
    mongoURI = ""
    with open("connectionString.txt", "r") as file:
        mongoURI = file.readline()
    client = MongoClient(mongoURI)
    # The ronSwansonQuotes database is created if it doesn't exist
    db = client.ronSwansonQuotes

    get_quotes()
