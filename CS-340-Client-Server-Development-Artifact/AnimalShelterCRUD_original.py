from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32103
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# This Create method implements the C in CRUD.
    def create(self, data):
        if data is not None:
            dataCheck = self.database.animals.insert_one(data)  # data should be dictionary
            # check dataCheck for success & return result
            if dataCheck == 0:
                return False
            else:
                return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# This Read method implements the R in CRUD.
    def read(self, data):
        if data is not None:
            dataCheck = self.database.animals.find(data, {"_id": False}) # data should be dictionary
        else:
            dataCheck = self.database.animals.find({}, {"_id": False})
        # return result
        return dataCheck
    
# This Update method implements the U in CRUD.
    def update(self, data, updateData):
        if data is not None:
            dataCheck = self.database.animals.update_many(data, {"$set": updateData}) # data should be dictionary
        else:
            return "{}"
        # return result
        return dataCheck.raw_result
    
# This Delete method implements the D in CRUD.
    def delete(self, data):
        if data is not None:
            dataCheck = self.database.animals.delete_many(data)
        else:
            return "{}"
        # return result
        return dataCheck.raw_result
