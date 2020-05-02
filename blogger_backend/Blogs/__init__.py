import pymongo

client = pymongo.MongoClient(
        "mongodb+srv://documents:cloudcomputing@cluster0-byuor.mongodb.net/test?retryWrites=true&w=majority")
database = client.dev

# collection for blogs
blog_collection = database.blogs

# collection for comments
comment_collection = database.comments