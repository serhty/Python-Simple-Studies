import json # we imported json
datas = {}
datas["users"] = []
datas["users"].append({"username" : "user1", "password" : "123456", "mail" : "user1@mail.com"}) # we add the data in json format
datas["users"].append({"username" : "user2", "password" : "456789", "mail" : "user2@mail.com"}) # we add the data in json format

with open("datas.json", "w") as file: # We create the data.json file and print the data. If we print with open, the file will be closed automatically at the end of the process. in the other method, we would have to close the file with file.close() at the end of the process.
    json.dump(datas,file)