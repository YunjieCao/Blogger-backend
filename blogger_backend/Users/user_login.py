from django.http import HttpResponse
import json
from BloggerModel.models import Users

def user_login(request):
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
    status_code =  404
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

    if "email" not in data or "password" not in data:
        status_code = 400
        msg["message"] = "Format error or lack key infomation."
        # ret = HttpResponse(status=201, content=json.dumps(msg), content_type="application/json")
        # return ret
    else:
        email, password = data["email"], data["password"]
        user_info = Users.objects.filter(email = email).values('id', 'pwd') # list of objects

        if not user_info:
            status_code = 403 # request forbidden ?
            msg["message"] = "The email has not been registered."

        else:
            user_info = user_info[0]
            if password != user_info["pwd"]:
                status_code = 403
                # password mismatch
                msg["message"] = "Password Incorrect!"
            else: # login successfully
                status_code = 200
                msg["message"] = "Successfully Login!"
                msg["valid"] = True
                msg["userId"] = user_info['id']

        # ret['Content-Type'] = 'text/html'
    ret = HttpResponse(status= status_code, content=json.dumps(msg), content_type="application/json")
    ret['Access-Control-Allow-Origin'] = '*'
    print(ret)
    return ret