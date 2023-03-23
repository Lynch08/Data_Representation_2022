from ast import Delete
from urllib import response
import requests
import json
import urllib.parse

url = "https://api.valoff.ie/api/Property/GetProperties"

ParamsDict = {
    "Download":"false",
    "Format":"json",
    "CategorySelected":"OFFICE",
    "LocalAuthority":"WICKLOW COUNTY COUNCIL",
    "Fields":"LocalAuthority,Category,Level,AreaPerFloor,NavTotal,CarPark,PropertyNumber,IG,Use,FloorUse,Address,PublicationDate"

}

def getAll():
    parameters = urllib.parse.urlencode(ParamsDict)
    #print(parameters)
    fullurl = url + '?' + parameters
    response = requests.get(fullurl)
    
    return response.json()

if __name__== "__main__":
    with open ("valorr.json", "wt") as fp:
        print(json.dumps(getAll()), file = fp)