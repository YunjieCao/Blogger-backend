from django.http import HttpResponse
import json
from BloggerModel.models import Users
from BloggerModel.models import UserInteractions
from blogger_backend.error_code import Error


def follow(request, follower_id, followee_id):
    """
    follower wants to follow followee
    :param request: request from frontend
    :param follower_id: user who click on follow button
    :param followee_id: user who are followed by this user action
    :return: None
    """
    rsp_status = 1
    errors = Error()

    try:
        new_interaction = UserInteractions(follower_id=follower_id, followee_id=followee_id)
        new_interaction.save()
    except Exception as e:
        rsp_status = 3

    ret = HttpResponse()
    ret['status'] = rsp_status
    ret['message'] = errors.get_message(rsp_status)
    ret['Access-Control-Allow-Origin'] = '*'

    return ret


def unfollow(request, follower_id, followee_id):
    """
    follower wants to unfollow followee
    :param request: request from frontend
    :param follower_id: user who clicks on unfollow button
    :param followee_id: user who are unfollowed by this user action
    :return: None
    """
    rsp_status = 1
    errors = Error()

    try:
        UserInteractions.objects.filter(follower_id=follower_id, followee_id=followee_id).delete()
    except Exception as e:
        rsp_status = 3

    ret = HttpResponse()
    ret['status'] = rsp_status
    ret['message'] = errors.get_message(rsp_status)
    ret['Access-Control-Allow-Origin'] = '*'
    return ret


def check_follow(request, follower_id, followee_id):
    """
    check whether follower is following followee
    :param request: request from frontend
    :param follower_id: follower id
    :param followee_id: followee id
    :return: boolean is_following
    """
    rsp_status = 1
    errors = Error()

    try:
        res = UserInteractions.objects.filter(follower_id=follower_id, followee_id=followee_id)
        if_following = (len(res) > 0)
        check_res = {'if_following': if_following}
        ret = HttpResponse(json.dumps(check_res))
    except Exception as e:
        rsp_status = 3
        ret = HttpResponse()
    ret['status'] = rsp_status
    ret['message'] = errors.get_message(rsp_status)
    ret['Access-Control-Allow-Origin'] = '*'
    return ret


def get_user_interaction(request, target_id):
    """
    get user interaction data of a user
    :param request: request from frontend
    :param target_id: target user id
    :return: how many people follow this user && how many people are followed by this user
    """
    rsp_status = 1
    errors = Error()

    try:
        follower = UserInteractions.objects.filter(followee=target_id).count()  # how many people follow target id
        followee = UserInteractions.objects.filter(follower=target_id).count()  # how many people target id follows
        ret_data = {'follower': follower, 'followee': followee}
        ret = HttpResponse(json.dumps(ret_data))
    except Exception as e:
        rsp_status = 3
        ret = HttpResponse()
    ret['status'] = rsp_status
    ret['message'] = errors.get_message(rsp_status)
    ret['Access-Control-Allow-Origin'] = '*'
    return ret
