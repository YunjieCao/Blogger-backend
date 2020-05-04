from django.http import HttpResponse
import json
from BloggerModel.models import Blogs
from blogger_backend.Blogs import mongo
from BloggerModel.models import Users
from django.db import IntegrityError
from bs4 import BeautifulSoup

DEFAULT_TITLE = "Untitled Article"
DEFAULT_CONTENT = "Here is nothing yet ... "
DEFAULT_DES_LEN = 20 # default length of description

def post_new_blog(request):
    '''
     {
        title: str,
        date: str (2019.01.01),
        author: str,
        content: str,
        }

    :param request:
    :return:
    '''
    # changes: content to mangodb
    msg = {
        "message": "",
        "valid": False
    }
    status_code = 400  # for post, default as bad requests
    print(request)
    print(request.body)
    if not request.body:
        status_code = 400 # bad request
        msg["message"] = "Format error or lack key infomation"
        ret = HttpResponse(status=status_code, content=json.dumps(msg), content_type="application/json")
        ret['Access-Control-Allow-Origin'] = '*'
        return ret

    data_str = str(request.body, encoding='utf-8')
    data = json.loads(data_str)

    if "user_id" not in data or not data["user_id"]:
        status_code = 400 # bad request
        msg["message"] = "Required user id to post the blog."
        ret = HttpResponse(status=status_code, content=json.dumps(msg), content_type="application/json")
        ret['Access-Control-Allow-Origin'] = '*'
        return ret

    user_id = data["user_id"]
    # judge whehter user exist
    author = Users.objects.get(id=user_id)
    if not author:
        status_code = 404
        msg["message"] = "The required user does not exit or has not been recorded in the database."
        ret = HttpResponse(status=status_code, content=json.dumps(msg), content_type="application/json")
        ret['Access-Control-Allow-Origin'] = '*'
        return ret

    title = str(data["title"]) if "title" in data else DEFAULT_TITLE
    content = str(data["content"]) if "content" in data else DEFAULT_CONTENT
    if "description" in  data:
        description = str(data["description"])
    else:
        # generate description automatically
        clean_content = BeautifulSoup(content, "lxml").text
        description = clean_content[:DEFAULT_DES_LEN]
        if len(description) < len(clean_content):
            description += "... [ ClICK TO SEE MORE ] "
        print(description)
    # description = str(data["description"]) if "description" in data else content[:DEFAULT_DES_LEN]

   # store in mongo DB
   #  content_to_store = {"content": content}
    mongodb = mongo.Mongo()

    try:
        result = mongodb.blog_collection.contents.insert_one({"content": content})
        article_id = result.inserted_id
        article_id = str(article_id)
    except:
        status_code = 500 # internal server error
        msg["message"] = "Fail to store the content in MongoDB"
        ret = HttpResponse(status=status_code, content=json.dumps(msg), content_type="application/json")
        ret['Access-Control-Allow-Origin'] = '*'
        return ret

    # sucessful, then store in sql
    try:
        new_article = Blogs(author= author, title = title, content = article_id, description = description)
        new_article.save()
        blog_id = new_article.id # can only get after save
    except IntegrityError as e:
        status_code = 500  # internal server error
        msg["message"] = "Fail to store the data in sql. Error" + str(e)
        ret = HttpResponse(status=status_code, content=json.dumps(msg), content_type="application/json")
        ret['Access-Control-Allow-Origin'] = '*'
        return ret
    # suvessfully store

    status_code = 200
    msg["valid"] = True
    msg['content_id'] = article_id #
    msg['blog_id'] = blog_id
    msg["message"] = "Successfully save the articles and the contents."
    ret = HttpResponse(status=status_code, content=json.dumps(msg), content_type="application/json")
    ret['Access-Control-Allow-Origin'] = '*'
    return ret