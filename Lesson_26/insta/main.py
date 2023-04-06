import requests
import random
print(requests.get("https://api.randomdatatools.ru/").json())
class User:
    def __init__(self,im="",fa="",log="",pas=""):
        self.__lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque quis diam vitae mauris tincidunt fringilla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. In vel risus augue. Cras gravida maximus massa, nec interdum nulla accumsan nec. Integer et diam sed lectus malesuada rhoncus sit amet eget elit. Suspendisse tincidunt nulla vitae lacus auctor luctus. Pellentesque."
        self.__resp = requests.get("https://api.randomdatatools.ru/").json()
        self.login = self.__resp["Login"] if not log else log
        self.__password = self.__resp["Password"]if not pas else pas
        self.imya = self.__resp["FirstName"]if not im else im
        self.familia = self.__resp["LastName"]if not fa else fa
        self.posts = [self.__lorem[random.randint(0,35):random.randint(36,70)]]