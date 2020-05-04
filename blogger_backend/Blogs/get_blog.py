from django.http import HttpResponse
import json
from BloggerModel.models import Blogs
from blogger_backend.Blogs import mongo
from BloggerModel.models import Users
from django.db import IntegrityError
from bson.objectid import ObjectId

def get_blog(request, blog_id):
    msg = {
        "message": ""
    }
    status_code = 201
    # print(request)
    # print(request.body)
    if not blog_id:
        msg["message"] = "Need blog id to retrive the infomation"
        ret = HttpResponse(status=status_code, content=json.dumps(msg), content_type="application/json")
        ret['Access-Control-Allow-Origin'] = '*'
        return ret

    # user_id = data["user_id"]
    # judge whehter user exist
    blog = Blogs.objects.get(id=blog_id)
    if not blog:
        msg["message"] = "Required blog does not exist"
        ret = HttpResponse(status=status_code, content=json.dumps(msg), content_type="application/json")
        ret['Access-Control-Allow-Origin'] = '*'
        return ret

    content_id = str(blog.content)
    # check in mongodb
    mongodb = mongo.Mongo()
    content = mongodb.blog_collection.contents.find_one({'_id': ObjectId(content_id)})
    print(content)
    if not content:
        # can also return error message
        content_str= "[ERR 404]  NOT FOUND"
    else:
        content_str = content["content"]

    # print(blog.timestamp)
    # print(type(blog.timestamp))
    create_time = blog.timestamp.strftime("%Y-%m-%d %H:%M")
    print(create_time)
    blog_info = {
        "id": blog.id,
        "title": blog.title,
        "date": create_time,
        "author": blog.author.name, # get the name of the author
        "content": content_str,
        "description": blog.description
    }
    # successfully log the data
    status_code = 200
    msg["message"] = "Successfully retrieved the blog."
    msg["blog"] = blog_info
    ret = HttpResponse(status=status_code, content=json.dumps(msg), content_type="application/json")
    ret['Access-Control-Allow-Origin'] = '*'
    return ret
