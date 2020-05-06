import time
from django.http import HttpResponse
import json
from BloggerModel.models import Blogs
from blogger_backend.Blogs import mongo
from BloggerModel.models import Users
'''
BLOG1: {
	title: str,
	id: int,
	date: str (2019.01.31)
	author: str
	description: str
}

'''
def get_blog_list(request):
    msg = {
        "message": "",
        "status": 400,
    }
    status_code = 404
    # blog_lists = Blogs.objects.all()
    try:
        blog_lists = Blogs.objects.all()
    except:
        status_code = 500
        msg["message"] = "Fail to retrieve data."
        ret = HttpResponse(status=status_code, content=json.dumps(msg), content_type="application/json")
        ret['Access-Control-Allow-Origin'] = '*'
        return ret
    print(blog_lists)
    if not blog_lists:
        msg["message"] = "No blogs recorded in the database."
        ret = HttpResponse(status=status_code, content=json.dumps(msg), content_type="application/json")
        ret['Access-Control-Allow-Origin'] = '*'
        return ret
    res = []


    for blog in blog_lists:
        blog_info ={
            'title': blog.title,
            'id': blog.id,
            'date': blog.timestamp.strftime("%Y-%m-%d %H:%M"),
            'author': blog.author.name,
            'description': blog.description
        }
        res.append(blog_info)
    res.sort(key = lambda blog: blog['date'], reverse= True)

    msg["message"] = "Successfully retrieved all the blog lists."
    msg["blogs"] = res
    msg["status"] = 200
    status_code = 200
    ret = HttpResponse(status=status_code, content=json.dumps(msg), content_type="application/json")
    ret['Access-Control-Allow-Origin'] = '*'
    return ret