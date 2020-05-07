from django.http import HttpResponse
import json
from BloggerModel.models import Users
from blogger_backend.error_code import Error

def user_login(request):
    """
    request format: {email: str, password: str}
    :return:
        {status: int, 200, 201
        message: str(explain for status),
         valid: boolean}
    """
    error = Error()
    if not request.body:
        return error.send_response(6)

    data_str= str(request.body, encoding='utf-8')
    data = json.loads(data_str)

    if "email" not in data or "password" not in data:
        return error.send_response(6)

    else:
        email, password = data["email"], data["password"]
        user_info = Users.objects.filter(email = email).values('id', 'pwd') # list of objects

        if not user_info:
            return error.send_response(14)

        else:
            user_info = user_info[0]
            if password != user_info["pwd"]:
               return error.send_response(15)
            else: # login successfully
                return error.send_response(1, {"userId": user_info['id']})