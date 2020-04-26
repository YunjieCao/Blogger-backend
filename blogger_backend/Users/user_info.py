from django.http import HttpResponse
import pymysql
import json
from BloggerModel.models import Users


def get_profile(request, user_id):
    # get all attributes from database
    # user_info = Users.objects.filter(id=user_id).values()
    # get specific attributes from database
    user_info = Users.objects.filter(id=user_id).values('name', 'birthday', 'occupation', 'introduction') # list of objects
    user_info = user_info[0]
    user_info['birthday'] = json.dumps(user_info['birthday'], indent=4, sort_keys=True, default=str) # jsonify datatime

    ret = HttpResponse(json.dumps(user_info))
    ret['Access-Control-Allow-Origin'] = '*'
    # ret['Content-Type'] = 'text/html'

    return ret

