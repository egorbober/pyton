import requests
import random
print(requests.get("https://api.randomdatatools.ru/").json())
class User:
    def __init__(self):
        self.__resp = requests.get("https://api.randomdatatools.ru/").json()
        self.login = self.__resp["Login"]
        self.__password = self.__resp["Password"]
        self.imya = self.__resp["FirstName"]
        self.familia = self.__resp["LastName"]
        self.posts = [self.__rolem[random.randint(0,35):random.randint(36,70)]]