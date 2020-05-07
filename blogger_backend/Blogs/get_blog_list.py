from django.http import HttpResponse
import json
from BloggerModel.models import Blogs
from blogger_backend.error_code import Error
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
    error = Error()
    try:
        blog_lists = Blogs.objects.all()
    except:
        return error.send_response(11)

    print(blog_lists)
    if not blog_lists:
        return error.send_response(11)
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

    other_attrs = dict()
    other_attrs["blogs"] = res
    return error.send_response(1, other_attrs)