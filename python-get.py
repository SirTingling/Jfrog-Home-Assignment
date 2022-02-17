import requests
import json

#enter credentials
username = "alexscher"
password = "Alex0246802"
artifactory = "https://alexscher.jfrog.io/artifactory/" #artifactory URL
api = "api/system/ping" #you can change this API URL to any API method you'd like to use

url = artifactory + api
r = requests.get(url, auth = (username, password)) #this script is only for API methods that use GET

if r.status_code == 200:
  print(r.content)
else:
  print("Fail")
  response = json.loads(r.content)
  print(response["errors"])

  print("x-request-id : " + r.headers['x-request-id'])
  print("Status Code : " + r.status_code)