from django.http import HttpResponse
import json
from BloggerModel.models import Blogs

def post_new_blog(request):
    # todo: try catch and judge
    # changes: content to mangodb
    print(request)
    print(request.body)
    data = json.loads(request.body)
    title = data["title"]
    author_id = data["author_id"]
    content = data["content"]
    description = data["description"]
    article = Blogs(title = title, author_id = author_id, description = description, content = content)
    article.save()
    # test1 = Blogs(title='First blog', author_id=1,content=1234, description="I have a dream!")
    # test1.save()
    return HttpResponse("successfully")