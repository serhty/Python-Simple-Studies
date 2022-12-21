import json # we imported json

with open("datas.json", "r") as file:
    datas = json.load(file)
    for user in datas["users"]:
        if user["username"] == "user1":
            print(user["password"])