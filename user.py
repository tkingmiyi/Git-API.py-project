import requests
import json

gitResponse=[]
#api url to grab public user data
api_url = f"https://api.github.com/repos/twpayne/go-vfs/pulls?state=all"

#send get request
response = requests.get(api_url).json()
gitResponse.append(response) #line4

#get the data in json or equivalent dict format

for resp in gitResponse:
    for stateResp in resp:
        print(stateResp['title'])
        print(stateResp['state']+f"\n")
        print(stateResp["created_at"])
        print(stateResp["updated_at"])
