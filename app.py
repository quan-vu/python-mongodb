# Quick start with MongoDb in Python
# For simple task with script without web framework

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["mytest"]

def add_customer():
    # The collection: customers will be auto create if not exist
    db.customers.insert({"name" : "Quan Vu"})
    
def get_customers():
    return db.customers.find_one()

if __name__ == "__main__":
    add_customer()
    results = get_customers()
    print(results)