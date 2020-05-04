import time
from django.http import HttpResponse
import json
from BloggerModel.models import News
from blogger_backend.Blogs import mongo
from BloggerModel.models import Users
from django.db import IntegrityError
from bson.objectid import ObjectId

def get_news(request, news_id):
    msg = {
        "message": ""
    }
    status_code = 404
    # print(request)
    # print(request.body)
    if not news_id:
        status_code = 400
        msg["message"] = "Need news id to retrieve the infomation."
        ret = HttpResponse(status=status_code, content=json.dumps(msg), content_type="application/json")
        ret['Access-Control-Allow-Origin'] = '*'
        return ret

    # user_id = data["user_id"]
    # judge whehter user exist
    news = News.objects.get(id=news_id)
    if not news:
        status_code = 403
        msg["message"] = "Required news does not exist"
        ret = HttpResponse(status=status_code, content=json.dumps(msg), content_type="application/json")
        ret['Access-Control-Allow-Origin'] = '*'
        return ret

    content_id = str(news.content)
    # check in mongodb
    mongodb = mongo.Mongo()
    content = mongodb.news_collection.articles.find_one({'_id': ObjectId(content_id)})
    print(content)
    if not content:
        # can also return error message
        status_code = 404
        msg["message"] = "Content of the targeted news can not be retrieved."
        content_str= "[ERR 404]  NOT FOUND"
    else:
        content_str = content["content"]

    # print(blog.timestamp)
    create_time = time.strftime("%Y-%m-%d %H:%M")
    news_info = {
        "id": news.id,
        "title": news.title,
        "date": create_time,
        "content": content_str,
        "url": news.url
    }
    # successfully log the data
    status_code = 200
    msg["message"] = "Successfully retrieved the news."
    msg["news"] = news_info
    ret = HttpResponse(status=status_code, content=json.dumps(msg), content_type="application/json")
    ret['Access-Control-Allow-Origin'] = '*'
    return ret
