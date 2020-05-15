from django.http import HttpResponse
import json

class Singleton(object):
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]


@Singleton
class Error(object):
    def __init__(self):
        self.error_code = dict()
        self.error_code[1] = 'successfully executed'
        self.error_code[2] = 'Something wrong with user info'
        self.error_code[3] = 'Invalid user id'
        self.error_code[4] = 'Something wrong with blog or user info'
        self.error_code[5] = 'Wrong action type'
        self.error_code[6] = 'Bad request format'
        self.error_code[7] = 'MongoDB failed'
        self.error_code[8] = 'Something wrong with blog info'
        self.error_code[9] = 'Invalid blog / news id'
        self.error_code[10] = 'Can not find blog / news'
        self.error_code[11] = 'Fail to retrieve data from mysql'
        self.error_code[12] = 'Fail to store data in sql'
        self.error_code[13] = "[User Registeration] The email has been registered."
        self.error_code[14] = "[User Login] The email has not been registered."
        self.error_code[15] = "[User Login] Password incorrect. "


    def add_error(self, code, message):
        self.error_code[code] = message

    def get_message(self, code):
        if code in self.error_code:
            return self.error_code[code]
        else:
            return 'Undefined error type'

    def send_response(self, code, other_attrs = None):
        body = dict()
        body["status"] = code
        body["message"] = self.get_message(code)
        if other_attrs:
            body.update(other_attrs)
        ret = HttpResponse(content=json.dumps(body), content_type="application/json")
        ret['Access-Control-Allow-Origin'] = '*'
        return ret

