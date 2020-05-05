import datetime

from django.http import HttpResponse
import json
from BloggerModel.models import Users

# some default values for not essential fields
DEFAULT_BIRTHDAY_STR = "1970-01-01"
DEFAULT_INTRO = "A wonderful blog writer"
DEFAULT_AVATAR = 'https://bootdey.com/img/Content/avatar/avatar3.png'
DEFAULT_GENDER_SET = 'not set'
def user_register(request):
    """
    request format: {email: str, password: str}
    :return:
        {status: int, 200, 201
        message: str(explain for status),
         valid: boolean}
    """
    msg = {
        "message": "",
        "valid": False
    }
    status_code =  400
    print(request)
    print(request.body)
    if not request.body:
        status_code = 400
        msg["message"] = "Format error or lack key infomation."
        ret = HttpResponse(status=status_code, content=json.dumps(msg), content_type="application/json")
        ret['Access-Control-Allow-Origin'] = '*'
        return ret

    data_str= str(request.body, encoding='utf-8')
    data = json.loads(data_str)

    required_attrs = {"email", "password", "name"}
    for attr in required_attrs:
        if attr not in data or not data[attr]:
            status_code = 400
            msg["message"] = "Format error or lack key infomation."
            ret = HttpResponse(status=status_code, content=json.dumps(msg), content_type="application/json")
            ret['Access-Control-Allow-Origin'] = '*'
            return ret

    email = data["email"]
    user_info = Users.objects.filter(email = email).values() # list of object

    if not user_info: # has not be registered
        # curtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        pwd= data["password"]
        name = data["name"]
        birthday = data["birthday"] if "birthday" in data else DEFAULT_BIRTHDAY_STR # if empty, enter default time
        occupation = str(data["occupation"]) if "occupation" in data else " "
        introduction = str(data["introduction"]) if "introduction" in data else DEFAULT_INTRO
        avatar = data["avatar"] if "avatar" in data else DEFAULT_AVATAR
        gender = data["gender"] if "gender" in data else DEFAULT_GENDER_SET
        try:
            new_user = Users(email = email, pwd = pwd, name = name, birthday = birthday,
                             occupation = occupation, introduction = introduction, avatar = avatar, gender = gender)
            print(new_user)
            new_user.save()
        except:
            status_code = 500
            msg["message"] = "Fail to save in the databases."
            ret = HttpResponse(status=status_code, content=json.dumps(msg), content_type="application/json")
            ret['Access-Control-Allow-Origin'] = '*'
            print(ret)
        # sucessfuly add
        user_info = Users.objects.filter(email=email).values()
        if user_info:
            print(user_info)
            new_user = user_info[0]
            status_code = 200
            msg["userId"] = new_user["id"]
            msg["valid"] = True
            msg["message"] = "Register sucessfully! The user info: " + str(new_user)
        else:
            status_code = 500
            msg["message"] = "The user with targeted email has not been recorded into the database correctly."
    else:
        status_code = 403 # request forbidden
        msg["message"] = "The email has been registered."

    ret = HttpResponse(status=status_code, content=json.dumps(msg), content_type="application/json")
    ret['Access-Control-Allow-Origin'] = '*'
    return ret
