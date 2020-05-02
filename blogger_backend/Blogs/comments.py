# import comment_collection
from django.http import HttpResponse
import json
import pymongo
from BloggerModel.models import Comments


def add_comment(request, blog_id, user_id):
    """

    :param request:
    :param blog_id:
    :param user_id:
    :return:
    """
    # comment = Comments(blogid=blog_id, u)

    pass