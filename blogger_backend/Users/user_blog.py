from django.http import HttpResponse
import json
from BloggerModel.models import LikeBlogs
from BloggerModel.models import DislikeBlogs
from blogger_backend.error_code import Error


def process_like_dislike(request, blog_id, user_id, action_type):
    """

    :param request: like/ dislike blog request from users
    :param blog_id: blog id
    :param user_id: user if
    :param action_type: 0: dislike 1: like
    :return: action result
    """
    rsp_status = 1

    if action_type == 0: # dislike
        try:
            dislike = DislikeBlogs(blogid_id=blog_id, userid_id=user_id)
            dislike.save()
        except Exception as e:
            rsp_status = 4
    elif action_type == 1: # like
        try:
            like = LikeBlogs(blogid_id=blog_id, userid_id=user_id)
            like.save()
        except Exception as e:
            rsp_status = 4
    else:
        rsp_status = 5

    ret = HttpResponse()
    errors = Error()
    ret['status'] = rsp_status
    ret['message'] = errors.get_message(rsp_status)
    ret['Access-Control-Allow-Origin'] = '*'
    return ret


