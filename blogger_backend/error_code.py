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


    def add_error(self, code, message):
        self.error_code[code] = message

    def get_message(self, code):
        if code in self.error_code:
            return self.error_code[code]
        else:
            return 'Undefined error type'
