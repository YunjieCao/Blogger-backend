from BloggerModel.models import News
from blogger_backend.error_code import Error
'''
NEWS1: {
	title: str,
	id: int,
	date: str (2019.01.31)
}

'''
def get_news_list(request):
    error = Error()
    try:
        news_lists = News.objects.all()
    except:
        return error.send_response(11)

    print(news_lists)
    if not news_lists:
        return error.send_response(11)

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
    other_attrs = dict()
    other_attrs["news"] = res
    return error.send_response(1, other_attrs)