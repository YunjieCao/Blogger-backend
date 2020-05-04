from django.http import HttpResponse
import json
from BloggerModel.models import LikeBlogs
from BloggerModel.models import DislikeBlogs


def process_like_dislike(request, blog_id, user_id, action_type):
    """

    :param request: like/ dislike blog request from users
    :param blog_id: blog id
    :param user_id: user if
    :param action_type: 0: dislike 1: like
    :return: action result
    """
    rsp_status = 200
    rsp_msg = 'successfully executed'
    if action_type == 0: # dislike
        try:
            dislike = DislikeBlogs(blogid_id=blog_id, userid_id=user_id)
            dislike.save()
        except Exception as e:
            rsp_status = 400
            rsp_msg = 'Something wrong with blog or user info'
    elif action_type == 1: # like
        try:
            like = LikeBlogs(blogid_id=blog_id, userid_id=user_id)
            like.save()
        except Exception as e:
            rsp_status = 400
            rsp_msg = 'Something wrong with blog or user info'
    else:
        rsp_status = 400
        rsp_msg = 'wrong action type'

    ret = HttpResponse(status=rsp_status, reason=rsp_msg)
    return ret


