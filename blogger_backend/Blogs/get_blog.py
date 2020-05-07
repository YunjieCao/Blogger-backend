from BloggerModel.models import Blogs
from blogger_backend.Blogs import mongo
from bson.objectid import ObjectId
from blogger_backend.error_code import Error

def get_blog(request, blog_id):
    error = Error()
    rsp_status = 1
    if not blog_id:
        return error.send_response(9)

    blog = Blogs.objects.get(id=blog_id)
    if not blog:
        # can not retrieve blog info
        return error.send_response(10)

    content_id = str(blog.content)
    # check in mongodb
    mongodb = mongo.Mongo()
    content = mongodb.blog_collection.contents.find_one({'_id': ObjectId(content_id)})
    print(content)
    if not content:
        # can also return error message
        rsp_status = 7
        content_str= "[ERR 404]  NOT FOUND"
    else:
        # rsp_status = 1
        content_str = content["content"]

    # print(blog.timestamp)
    create_time = blog.timestamp.strftime("%Y-%m-%d %H:%M")
    blog_info = {
        "id": blog.id,
        "title": blog.title,
        "date": create_time,
        "author": blog.author.name, # get the name of the author
        "content": content_str,
        "description": blog.description
    }
    # successfully log the data
    other_attrs = dict()
    other_attrs["blog"] = blog_info
    return error.send_response(rsp_status, other_attrs)