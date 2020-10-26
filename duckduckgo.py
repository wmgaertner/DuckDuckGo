import requests, pytest, json

url_ddg = "https://api.duckduckgo.com"


presidents_lastname = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson", "Buren", "Harrison", "Tyler", "Polk", 
    "Taylor", "Fillmore", "Pierce", "Buchanan", "Lincoln", "Johnson", "Grant", "Hayes", "Garfield", "Arthur", "Cleveland", "Harrison", "Cleveland", 
    "McKinley", "Roosevelt", "Taft", "Wilson", "Harding", "Coolidge", "Hoover", "Roosevelt", "Truman", "Eisenhower", "Kennedy", "Johnson", 
    "Nixon", "Ford", "Carter", "Reagan", "Bush", "Clinton", "Bush", "Obama", "Trump"]

resp = requests.get(url_ddg + "/?q=presidents of the united states&format=json")

rsp_data = json.dumps(resp.json())

for lastname in presidents_lastname:
        if lastname in rsp_data:
            print(lastname, ": true")

