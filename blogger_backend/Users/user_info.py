from django.http import HttpResponse
import pymysql
import json
from BloggerModel.models import Users


def get_profile(request, user_id):
    # get all attributes from database
    # user_info = Users.objects.filter(id=user_id).values()
    # get specific attributes from database
    user_info = Users.objects.filter(id=user_id).values('name', 'birthday', 'occupation', 'introduction') # list of objects
    user_info = user_info[0]
    user_info['birthday'] = json.dumps(user_info['birthday'], indent=4, sort_keys=True, default=str) # jsonify datatime

    ret = HttpResponse(json.dumps(user_info))
    ret['Access-Control-Allow-Origin'] = '*'
    # ret['Content-Type'] = 'text/html'

    return ret

def try_connect():
    db_connect_info = {
        'host': 'blogger-mysql.cp2o8exigrko.us-east-1.rds.amazonaws.com',
        'user': 'admin',
        'password': 'cloudcomputing',
        'port': 3306,
        'db': 'blogger',
        'charset': 'utf8'
    }
    c_info = db_connect_info
    result = pymysql.connect(
        host=c_info['host'],
        user=c_info['user'],
        password=c_info['password'],
        port=c_info['port'],
        db=c_info['db'],
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    print('successfully connect')


if __name__=="__main__":
    try_connect()