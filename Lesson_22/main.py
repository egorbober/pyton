# try:
#     x = 5/0
#     int("o")
# except ZeroDivisionError:
#     print("на 0 делить НЕЛЬЗЯ!!!")
# except ValueError:
#     print("Ы это не число!!!")

import json
# WriteF = open("File.json","w",encoding= "utf-8")
# # WriteF.write("True")
# content = [None, True,(1,2,3), [1,2,3],"Hello","Привки"]
# json.dump(content,WriteF,ensure_ascii=False)
# WriteF.close()


# ReadF = open("File.json","r",encoding= "utf-8")
# print(json.load(ReadF))
# ReadF.close


#первый задача
# import json
# readf = open("file.txt","r", encoding="utf-8")
# content = readf.readlines()
# readf.close()
#
# print(content)
# d = {}
# for record in content:
#     splited = record.split(": ")
#     print(splited)
#     d[splited[0]] = splited[1].rstrip()
# print(d)
#
#
#
# f = open("File.json","w",encoding="utf-8")
# json.dump(d,f,ensure_ascii= False)
# f.close()

import requests
respons = requests.get(url = "http://api.open-notify.org/iss-now.json")
data = respons.json()["iss_position"]
print(f"Широта:{data['latitude']}. Долго да: {data['longitude']}")