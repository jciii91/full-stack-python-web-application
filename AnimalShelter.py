from pymongo import MongoClient


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # Connection Variables
        #
        host = 'nv-desktop-services.apporto.com'
        options = '?directConnection=true&appName=mongosh+1.8.0'
        port = 32364
        db = 'AAC'
        col = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d/%s/' % (username, password, host, port, options))
        self.database = self.client['%s' % (db)]
        self.collection = self.database['%s' % (col)]

    # Insert document into collection
    def create(self, data):
        if data is not None:
            self.collection.insert_one(data)  # data should be dictionary
            return True
        else:
            return False

    # Read document from collection
    # The key should be a valid key present in the collection documents
    def read(self, data):
        if data is not None:
            cursor = self.collection.find(data)
            return list(cursor)
        else:
            return []
    
    # Find ojects that meet the find_criteria and update them with new data
    # Return the numer of objects updated
    def update(self, find_criteria, new_data):
        if find_criteria and new_data is not None:
            return(self.collection.update_many(find_criteria, new_data).modified_count)
    
    # Find ojects that meet the find_criteria and delete them
    # Return the number of objects deleted
    def delete(self, find_criteria):
        if find_criteria is not None:
            return(self.collection.delete_many(find_criteria).deleted_count)
