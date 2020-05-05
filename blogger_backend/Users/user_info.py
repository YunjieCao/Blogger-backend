from django.http import HttpResponse
import json
from BloggerModel.models import Users


def get_profile(request, user_id):
    """
    get user profile according to user id
    :param request: request from frontend
    :param user_id: user_id
    :return: basic information of this user
    """
    # get all attributes from database
    # user_info = Users.objects.filter(id=user_id).values()
    # get specific attributes from database
    rsp_status = 200
    rsp_msg = 'successfully get user profile'
    try:
        user_info = Users.objects.filter(id=user_id).values('name', 'birthday', 'occupation', 'introduction', 'timestamp', 'avatar') # list of objects
        user_info = user_info[0]
        user_info['birthday'] = json.dumps(user_info['birthday'], indent=4, sort_keys=True, default=str) # jsonify datatime
        user_info['timestamp'] = json.dumps(user_info['timestamp'], indent=4, sort_keys=True, default=str)
        ret = HttpResponse(json.dumps(user_info), status=rsp_status, reason=rsp_msg)
    except Exception as e:
        rsp_status = 400
        rsp_msg = 'Something wrong with user info'
        ret = HttpResponse(status=rsp_status, reason=rsp_msg)
    ret['Access-Control-Allow-Origin'] = '*'

    return ret



