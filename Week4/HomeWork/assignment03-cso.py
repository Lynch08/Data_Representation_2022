
import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

def getAll():
    response = requests.get(url)
    return response.json()

def getAllAsFile():
    with open("cso.json", "wt") as fp:
        print(json.dumps(getAll()), file = fp)

print (getAllAsFile())