import requests
from colorama import Fore, Style
import hashlib
# import time

try:
    import simplejson as json
except ImportError:
    import json


class Pwned (object):
    def __init__(self):
        self.account_v2 = "https://haveibeenpwned.com/api/v2/breachedaccount/"
        self.password_v2 = "https://api.pwnedpasswords.com/range/"
        self.paste_v2 = "https://haveibeenpwned.com/api/v2/pasteaccount/"

    def goodResponse(self, ret):
        if ret == 200:
            return True
        elif ret == 400:
            print(Fore.RED + "*** Bad request ***" + Style.RESET_ALL)
        elif ret == 403:
            print(Fore.RED + "*** Forbidden request ***" + Style.RESET_ALL)
        # elif ret == 404:
        #     print(Fore.RED + "*** Not found ***" + Style.RESET_ALL)
        elif ret == 429:
            print(Fore.RED + "*** Sending requests too fast ***" + Style.RESET_ALL)
        return False

    def account(self, email):
        a = self.account_v2 + email
        r = requests.get(a)
        j = None

        if self.goodResponse(r.status_code):
            j = json.loads(r.text)

        return j

    def paste(self, account):
        a = self.paste_v2 + account
        r = requests.get(a)
        j = None

        if self.goodResponse(r.status_code):
            j = json.loads(r.text)

        return j

    def password(self, pwd):
        # hash password
        sha_1 = hashlib.sha1()
        bpwd = pwd.encode('utf-8')
        sha_1.update(bpwd)
        sha1pwd = sha_1.hexdigest()

        # the API only takes the first 5 characters and returns all matches
        # to it. You must match the remaining characters to determine if
        # it has been harvested. the return format is: <hash>:number\r
        r = requests.get(self.password_v2 + sha1pwd[:5])
        if self.goodResponse(r.status_code):
            ss = r.text.split('\r')
            for s in ss:
                num = s.split(':')[1]
                s = s.split(':')[0].lower()
                if s[1:] == str(sha1pwd[5:]):
                    return num
            return 0
        else:
            print("*** Strange, it should have returned something!! ***")
            return 0

    def clean(self, n):
        scale = ['', 'thousand', 'million', 'billion', 'trillion']
        nn = int(n)
        cnt = 0
        while nn > 0:
            nn = nn // 1000  # int div
            cnt += 1
        cnt -= 1
        s = "{} {}".format(n//(1000**cnt), scale[cnt])
        return s
