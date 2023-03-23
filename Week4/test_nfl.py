import requests
import json
import urllib.parse

url = "https://nfl-schedule.p.rapidapi.com/v1/schedules"

headers = {
	"X-RapidAPI-Key": "8bb473069emsh74359e60faae05bp1d5381jsndd60e82327cb",
	"X-RapidAPI-Host": "nfl-schedule.p.rapidapi.com"
}


def getAll():
    response = requests.request("GET", url, headers=headers)
    return response.json()

if __name__== "__main__":
    with open ("nfl_test.json", "wt") as fp:
        print(json.dumps(getAll()), file = fp)


#print(response.text)