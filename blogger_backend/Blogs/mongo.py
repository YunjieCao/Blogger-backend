import pymongo

"""
This file creates the connection with MondoDB in singleton pattern. 
"""


class Singleton(object):
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]


@Singleton
class Mongo(object):
    def __init__(self):
        self.client = pymongo.MongoClient(
                "mongodb+srv://documents:cloudcomputing@cluster0-byuor.mongodb.net/test?retryWrites=true&w=majority")
        self.database = self.client.dev

        # collection for blogs
        self.blog_collection = self.database.blogs

        # collection for comments
        self.comment_collection = self.database.comments