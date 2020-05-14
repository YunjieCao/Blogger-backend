from blogger_backend.Blogs import mongo
from django.http import HttpResponse
import json
import pymongo
from bson.objectid import ObjectId
from BloggerModel.models import Comments
from blogger_backend.error_code import Error


def add_comment(request):
    """
    store comment to db
    :param request: request from frontend
    :param blog_id: blog id
    :param user_id: user leaving this comment
    :return: Status
    """
    rsp_status = 1

    try:
        data = str(request.body, encoding='utf-8')   # {"comment": "do you like it?"}

        data = json.loads(data)

        required_fields = ['comment', 'blog_id', 'user_id']
        for field in required_fields:
            assert field in data
        blog_id = data['blog_id']
        user_id = data['user_id']
        del data['blog_id']
        del data['user_id']

    except Exception as e:
        rsp_status = 6
        ret = HttpResponse()
        errors = Error()
        ret['status'] = rsp_status
        ret['message'] = errors.get_message(rsp_status)
        ret['Access-Control-Allow-Origin'] = '*'
        return ret

    try:
        mongodb = mongo.Mongo()
        result = mongodb.comment_collection.insert_one(data)
        comment_id = result.inserted_id
        comment_id = str(comment_id)

    except Exception as e:
        rsp_status = 7
        ret = HttpResponse()
        errors = Error()
        ret['status'] = rsp_status
        ret['message'] = errors.get_message(rsp_status)
        ret['Access-Control-Allow-Origin'] = '*'
        return ret

    try:
        comment = Comments(blog_id_id=blog_id, user_id_id=user_id, content=comment_id)
        comment.save()
    except Exception as e:
        rsp_status = 4

    ret = HttpResponse()
    errors = Error()
    ret['status'] = rsp_status
    ret['message'] = errors.get_message(rsp_status)
    ret['Access-Control-Allow-Origin'] = '*'

    return ret


def retrieve_comment(request, blog_id):
    """
    retrieve comments for a specific blog
    :param request: from frontend
    :param blog_id: blog id
    :return: a list of comments at most 10
    """
    rsp_status = 1

    try:
        data = Comments.objects.filter(blog_id_id=blog_id).select_related('user_id').order_by('-timestamp').values('comment_id', 'blog_id', 'user_id', 'content', 'timestamp', 'user_id__name')  # list of objects
    except Exception as e:
        rsp_status = 8
        ret = HttpResponse()
        errors = Error()
        ret['status'] = rsp_status
        ret['message'] = errors.get_message(rsp_status)
        ret['Access-Control-Allow-Origin'] = '*'
        return ret

    try:
        mongodb = mongo.Mongo()
    except Exception as e:
        rsp_status = 7
        ret = HttpResponse()
        errors = Error()
        ret['status'] = rsp_status
        ret['message'] = errors.get_message(rsp_status)
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
            d['timestamp'] = json.dumps(d['timestamp'], indent=4, sort_keys=True, default=str)
            ret_data.append(d)
            if len(ret_data) > 10:
                break
    except Exception as e:
        rsp_status = 7
        ret = HttpResponse()
        errors = Error()
        ret['status'] = rsp_status
        ret['message'] = errors.get_message(rsp_status)
        ret['Access-Control-Allow-Origin'] = '*'
        return ret

    ret = dict()
    ret['data'] = ret_data
    print(ret_data)
    ret = HttpResponse(json.dumps(ret))
    errors = Error()
    ret['status'] = rsp_status
    ret['message'] = errors.get_message(rsp_status)
    ret['Access-Control-Allow-Origin'] = '*'
    return ret
