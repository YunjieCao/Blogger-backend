from blogger_backend.Blogs import mongo
from django.http import HttpResponse
import json
import pymongo
from BloggerModel.models import Comments


def add_comment(request, blog_id, user_id):
    # TODO： add try exception when insert to mongodb or mysql
    """
    store comment to db
    :param request: request from frontend
    :param blog_id: blog id
    :param user_id: user leaving this comment
    :return: Status
    """
    # print(request.body)
    data = str(request.body, encoding='utf-8')
    data = json.loads(data)
    # print(data)

    mongodb = mongo.Mongo()
    result = mongodb.comment_collection.reviews.insert_one(data)
    # print(result.inserted_id)
    comment_id = result.inserted_id
    comment_id = str(comment_id)
    # print(comment_id)
    comment = Comments(blog_id_id=blog_id, uesr_id_id=user_id, content=comment_id)
    comment.save()
    ret = HttpResponse(status=200, reason="Successfully add a comment")
    ret['Access-Control-Allow-Origin'] = '*'
    return ret


def retrieve_comment(request):
    # TODO: retrieve comment of a blog
    pass