import json 
import requests

# with open("test.json", "r") as file:
#     obj = json.load(file)

# print(obj)
# print(type(obj))
# print(obj['key'])
# print(obj['key4'](1))
# obj['key'] = "qwerty"
# with open("test.json", "w") as file:
#     json.dump(obj,file)

# resp = requests.get("https://jsonplaceholder.typicode.com/users")
# if resp.status_code == 200:
#     obj = json.loads(resp.text)

# print(obj[0]['address'])

CITY = "Dnipro"
KEY = "144aad8b326f4a8ede3b1521eeadd6ed"
resp = requests.get("https://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}".format(CITY, KEY))
if resp.status_code == 200:
    data = json.loads(resp.text)

print(data['weather'])