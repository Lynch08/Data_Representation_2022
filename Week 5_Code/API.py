import urllib.parse
from github import Github
import requests
import json
from config import config as cfg



filename = "repos-public.json"
apikey = cfg['APIkey']
#
url = 'https://api.github.com/repos/Lynch08/Data_Rep_API_Test/contents'
#
#
g = Github(apikey)
#
for repo in g.get_user().get_repos():
    print (repo.name)


response = requests.get(url, auth = ('token', apikey))
print (response.status_code)
repoJSON = response.json()
with open (filename, 'w') as fp:
    json.dump(repoJSON, fp, indent = 4)
