from blogger_backend.Blogs import mongo
from django.http import HttpResponse
import json
import pymongo
from bson.objectid import ObjectId
from BloggerModel.models import Comments


def add_comment(request, blog_id, user_id):
    """
    store comment to db
    :param request: request from frontend
    :param blog_id: blog id
    :param user_id: user leaving this comment
    :return: Status
    """
    rsp_status = 200
    rsp_msg = 'successfully add a comment to this blog'

    try:
        data = str(request.body, encoding='utf-8')   # {"comment": "do you like it?"}
        data = json.loads(data)
        assert data.has_key('comment')
    except Exception as e:
        rsp_status = 400
        rsp_msg = 'Bad request format'
        ret = HttpResponse(status=rsp_status, reason=rsp_msg)
        ret['Access-Control-Allow-Origin'] = '*'
        return ret

    try:
        mongodb = mongo.Mongo()
        result = mongodb.comment_collection.insert_one(data)
        comment_id = result.inserted_id
        comment_id = str(comment_id)

    except Exception as e:
        rsp_status = 500
        rsp_msg = 'MongoDB failed'
        ret = HttpResponse(status=rsp_status, reason=rsp_msg)
        ret['Access-Control-Allow-Origin'] = '*'
        return ret

    try:
        comment = Comments(blog_id_id=blog_id, user_id_id=user_id, content=comment_id)
        comment.save()
    except Exception as e:
        rsp_status = 400
        rsp_msg = 'Something wrong with blog or user info'
    ret = HttpResponse(status=rsp_status, reason=rsp_msg)
    ret['Access-Control-Allow-Origin'] = '*'

    return ret


def retrieve_comment(request, blog_id):
    """
    retrieve comments for a specific blog
    :param request: from frontend
    :param blog_id: blog id
    :return: a list of comments at most 10
    """
    rsp_status = 200
    rsp_msg = 'successfully retrieve comments for this blog'

    try:
        data = Comments.objects.filter(blog_id_id=blog_id).select_related('user_id').values('blog_id', 'user_id', 'content', 'user_id__name')  # list of objects
    except Exception as e:
        rsp_status = 400
        rsp_msg = 'Something wrong with blog info'
        ret = HttpResponse(status=rsp_status, reason=rsp_msg)
        ret['Access-Control-Allow-Origin'] = '*'
        return ret

    try:
        mongodb = mongo.Mongo()
    except Exception as e:
        rsp_status = 500
        rsp_msg = 'Failed to connect to MongoDB'
        ret = HttpResponse(status=rsp_status, reason=rsp_msg)
        ret['Access-Control-Allow-Origin'] = '*'
        return ret

    try:
        ret_data = []
        for d in data:
            mongo_id = d['content']
            obj = ObjectId(mongo_id)
            res = mongodb.comment_collection.find({"_id": obj})
            comment_body = ''
            for r in res:
                comment_body += r['comment']
            d['content'] = comment_body
            ret_data.append(d)
            if len(ret_data) > 10:
                break
    except Exception as e:
        rsp_status = 500
        rsp_msg = 'Something wrong when retrieve from MongoDB'
        ret = HttpResponse(status=rsp_status, reason=rsp_msg)
        ret['Access-Control-Allow-Origin'] = '*'
        return ret

    ret = dict()
    ret['data'] = ret_data

    ret = HttpResponse(json.dumps(ret), status=rsp_status, reason=rsp_msg)
    ret['Access-Control-Allow-Origin'] = '*'
    return ret
