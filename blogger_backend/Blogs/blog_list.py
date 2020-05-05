from django.http import HttpResponse
import json
from BloggerModel.models import Blogs
from BloggerModel.models import Users


def get_user_blog_list(request, user_id):
    """
    get blogs of a user
    :param request: request from frontend
    :param user_id: the quried user id
    :return: a list of blogs belonging to this user
    """
    rsp_status = 200
    rsp_msg = 'successfully get blogs for this user'
    try:
        blog_list = Blogs.objects.filter(author_id=user_id).values('title', 'id', 'timestamp', 'description').order_by('-timestamp')[:10]
        user_info = Users.objects.filter(id=user_id).values('name', 'avatar')  # list of objects
        user_info = user_info[0]
        author = user_info['name']
        avatar = user_info['avatar']

        ret_data = {}
        ret_list = []
        for i in range(len(blog_list)):
            blog_list[i]['timestamp'] = json.dumps(blog_list[i]['timestamp'], indent=4, sort_keys=True, default=str)
            blog_list[i]['author'] = author
            blog_list[i]['avatar'] = avatar
            ret_list.append(blog_list[i])
        ret_data['blogs'] = ret_list

        ret = HttpResponse(json.dumps(ret_data), status=rsp_status, reason=rsp_msg)
    except Exception as e:
        rsp_status = 400
        rsp_msg = 'something wrong with user info'
        ret = HttpResponse(status=rsp_status, reason=rsp_msg)

    ret['Access-Control-Allow-Origin'] = '*'

    return ret
