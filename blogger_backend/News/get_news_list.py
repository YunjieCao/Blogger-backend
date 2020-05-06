import time
from django.http import HttpResponse
import json
from BloggerModel.models import News
from blogger_backend.Blogs import mongo
from BloggerModel.models import Users
'''
NEWS1: {
	title: str,
	id: int,
	date: str (2019.01.31)
}

'''
def get_news_list(request):
    msg = {
        "message": "",
        "status": 400,
    }
    status_code = 404
    try:
        news_lists = News.objects.all()
    except:
        status_code = 500
        msg["message"] = "Fail to retrieve data."
        ret = HttpResponse(status=status_code, content=json.dumps(msg), content_type="application/json")
        ret['Access-Control-Allow-Origin'] = '*'
        return ret

    print(news_lists)
    if not news_lists:
        msg["message"] = "No news recorded in the database."
        ret = HttpResponse(status=status_code, content=json.dumps(msg), content_type="application/json")
        ret['Access-Control-Allow-Origin'] = '*'
        return ret

    res = []
    for news in news_lists:
        news_info ={
            'title': news.title,
            'id': news.id,
            'date': news.timestamp.strftime("%Y-%m-%d %H:%M"),
            'url': news.url,
        }
        res.append(news_info)
    # sort by timestamp
    res.sort(key=lambda news: news['date'], reverse=True)
    msg["message"] = "Successfully retrieved all the news lists."
    msg["news"] = res
    status_code = 200
    msg["status"] = 200
    ret = HttpResponse(status=status_code, content=json.dumps(msg), content_type="application/json")
    ret['Access-Control-Allow-Origin'] = '*'
    return ret