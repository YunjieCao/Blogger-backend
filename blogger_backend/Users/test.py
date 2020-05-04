# from django.http import HttpResponse
# import pymysql
# import json
# import pymongo
# from bson.objectid import ObjectId
# # from BloggerModel.models import Users
#
# def hello(request):
#     return HttpResponse("Hello world ! ")
#
# def testdb(request):
#     print(request)
#     user_name = 'yunjie'
#     # test1 = Users(name=user_name)
#     # test1.save()
#     data = {
#         'Name': 'test1',
#         'Gender': 'Male',
#         'Occupation': 'Student',
#         'Description': 'hello',
#     }
#     ret = HttpResponse(json.dumps(data))
#     ret['Access-Control-Allow-Origin'] = '*'
#     # ret['Content-Type'] = 'text/html'
#     # data = {
#     #     'Name': 'test1',
#     #     'Gender': 'Male',
#     #     'Occupation': 'Student',
#     #     'Description': 'hello',
#     # }
#     # ret['info'] = json.dumps(data)
#     return ret
#
# def try_connect():
#     db_connect_info = {
#         'host': 'blogger-mysql.cp2o8exigrko.us-east-1.rds.amazonaws.com',
#         'user': 'admin',
#         'password': 'cloudcomputing',
#         'port': 3306,
#         'db': 'blogger',
#         'charset': 'utf8'
#     }
#     c_info = db_connect_info
#     result = pymysql.connect(
#         host=c_info['host'],
#         user=c_info['user'],
#         password=c_info['password'],
#         port=c_info['port'],
#         db=c_info['db'],
#         charset='utf8mb4',
#         cursorclass=pymysql.cursors.DictCursor
#     )
#     print('successfully connect')
#
# def try_mongodb():
#     client = pymongo.MongoClient(
#         "mongodb+srv://documents:cloudcomputing@cluster0-byuor.mongodb.net/test?retryWrites=true&w=majority")
#     db = client.test
#     temp = {'body': "hello world"}
#     # result=db.reviews.insert_one(temp)
#     # print(result.inserted_id) #
#
#     id = "5ead8cbd29a50a52fa522350"
#     obj = ObjectId(id)
#     res = db.reviews.find({"_id": obj})
#     # res = db.reviews.find({"body": "hello world"})
#     print(res)
#     for r in res:
#         print(r)
#
#
#
# if __name__=="__main__":
#     try_mongodb()