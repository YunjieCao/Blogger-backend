import time
from BloggerModel.models import News
from blogger_backend.Blogs import mongo
from bson.objectid import ObjectId
from blogger_backend.error_code import Error

def get_news(request, news_id):

    error = Error()
    rsp_status = 1
    if not news_id:
        error.send_response(9)

    # user_id = data["user_id"]
    # judge whehter user exist
    news = News.objects.get(id=news_id)
    if not news:
        return error.send_response(10)

    content_id = str(news.content)
    # check in mongodb
    mongodb = mongo.Mongo()
    content = mongodb.news_collection.articles.find_one({'_id': ObjectId(content_id)})
    print(content)
    if not content:
        # can also return error message
        rsp_status = 7
        content_str= "[ERR 404]  NOT FOUND"
    else:
        # rsp_status = 1
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
    other_attrs = dict()
    other_attrs["news"] = news_info
    return error.send_response(rsp_status, other_attrs)
