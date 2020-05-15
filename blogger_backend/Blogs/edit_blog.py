from BloggerModel.models import Blogs
from blogger_backend.Blogs import mongo
from bson.objectid import ObjectId
from blogger_backend.error_code import Error
import json
# data request: blog_id, title, content
# post method
def edit_blog(request):
    error = Error()
    # print(request)
    if not request.body:
        return error.send_response(6)

    # print(request.body)
    data_str = str(request.body, encoding='utf-8')
    data = json.loads(data_str)

    required_attrs = {"blog_id", "title", "content"}
    for attr in required_attrs:
        if attr not in data or not data[attr]:
            # status_code = 400
            # msg["message"] = "Format error or lack key infomation."
            return error.send_response(6)


    blog = Blogs.objects.get(id=data["blog_id"])
    if not blog:
        # can not retrieve blog info
        return error.send_response(10)
    blog.title = data["title"]
    mongodb = mongo.Mongo()
    query = {'_id': ObjectId(blog.content)}
    new_contents = {"$set": {"content": data["content"]}}
    try:
        mongodb.blog_collection.contents.update_one(query, new_contents)
    except:
        error.send_response(7)
    try:
        blog.save()
    except:
        error.send_response(12)
    other_attrs = dict()
    other_attrs['content_id'] = blog.content
    other_attrs['blog_id'] = blog.id
    return error.send_response(1, other_attrs)


