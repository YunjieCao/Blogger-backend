from django.http import HttpResponse
import json
from BloggerModel.models import Blogs

def get_user_blog_list(request, user_id):
    blog_list = Blogs.objects.filter(author_id=user_id).values('title', 'id', 'timestamp', 'description').order_by('-timestamp')[:10]
    ret_data = {}
    ret_list = []
    for i in range(len(blog_list)):
        blog_list[i]['timestamp'] = json.dumps(blog_list[i]['timestamp'], indent=4, sort_keys=True, default=str)
        ret_list.append(blog_list[i])
    ret_data['blogs'] = ret_list

    ret = HttpResponse(json.dumps(ret_data))
    ret['Access-Control-Allow-Origin'] = '*'
    # ret['Content-Type'] = 'text/html'

    return ret
