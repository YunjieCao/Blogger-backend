from django.http import HttpResponse
import json
from BloggerModel.models import Users
from blogger_backend.error_code import Error

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
    # msg = {
    #     "message": "",
    #     "valid": False,
    #     "status": 400,
    # }
    # status_code =  400

    error = Error()
    if not request.body:
        return error.send_response(6)

    data_str= str(request.body, encoding='utf-8')
    data = json.loads(data_str)

    required_attrs = {"email", "password", "name"}
    for attr in required_attrs:
        if attr not in data or not data[attr]:
            # status_code = 400
            # msg["message"] = "Format error or lack key infomation."
            return error.send_response(6)

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
            return error.send_response(12)
        # sucessfuly add
        user_info = Users.objects.filter(email=email).values()
        other_attrs = {}
        if user_info:
            print(user_info)
            new_user = user_info[0]
            return error.send_response(1, {"userId": new_user["id"]})
            # msg["valid"] = True
            # msg["status"] = 200
            # msg["message"] = "Register sucessfully! The user info: " + str(new_user)
        else:
            return error.send_response(12)
    else:
        return error.send_response(13)
