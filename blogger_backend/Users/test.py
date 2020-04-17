from django.http import HttpResponse
import pymysql
# from BloggerModel.models import Users

def hello(request):
    return HttpResponse("Hello world ! ")

def testdb(request):
    print(request)
    user_name = 'yunjie'
    # test1 = Users(name=user_name)
    # test1.save()
    return HttpResponse("<p>{} is successfully registered</p>".format(user_name))

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