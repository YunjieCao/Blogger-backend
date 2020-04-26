from django.http import HttpResponse
import json
from BloggerModel.models import Blogs

def post_new_blog(request):
    test1 = Blogs(title='First blog', author_id=1,content=1234, description="I have a dream!")
    test1.save()
    return HttpResponse("successfully")