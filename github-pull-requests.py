import requests

url = 'https://api.github.com/repos/LandmakTechnology/spring-boot-docker/pulls'

response = requests.get(url) #This script will get the pull requests using the api provisded in a JSON format.

pull_requests = response.json() #This converts the pull requests from a JSON format to a list of dictionaries

id = pull_requests[2]["body"] #This will return the value for the "body" key in the 2nd dictionary in the list of pull requests.

print(id)

#You must first intall the "request" module to be able to import it into your work environment. #This script will get the pull requests using the api provisded in a JSON format, 
#convert it to a dictionary. 
---
import requests

url = 'https://api.github.com/repos/LandmakTechnology/spring-boot-docker/pulls'

response = requests.get(url)

pull_requests = response.json()
for i in range(len(pull_requests)):
    print(pull_requests[i]["user"]["login"]) # This will return all the names in the pull request

---
import requests

url = 'https://api.github.com/repos/LandmakTechnology/spring-boot-docker/pulls'

response = requests.get(url)

pull_requests = response.json()
for i in range(len(pull_requests)):
    print(pull_requests[i]["body"]) # This will return all the body messages for the pull requests
