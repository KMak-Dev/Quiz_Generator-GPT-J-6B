import requests
import json
# Request types
MC_url = "https://shared-api.forefront.link/organization/9aDsThyuopVF/gpt-j-6b-vanilla/completions/O5hBBZA60L1h"
SQ_url = "https://shared-api.forefront.link/organization/9aDsThyuopVF/gpt-j-6b-vanilla/completions/f3v4Itakh61h"

# User inputs
key = input("Enter API-Key: ")

txt = input("Paste Your Input Text Here: ")

choice = input("Enter \"MC\" For Multiple-Choice, \"SQ\" For Short Question: ")
url = ""
if choice == "MC":
    url = MC_url
elif choice == "SQ":
    url = SQ_url
else:
    raise Exception("Invalid Choice")

authorization = "Bearer " + key
headers = {
  "Authorization": authorization,
  "Content-Type": "application/json"
}

body = {
  "text": txt,
  "top_p": 1,
  "top_k": 40,
  "temperature": 0.8,
  "repetition_penalty":  1,
  "length": 100,
  "stop_sequences": ["bird"]
}

res = requests.post(
  url,
  json=body,
  headers=headers
)

data = res.json()

completion = data['result'][0]['completion']

print(completion)

file = open("outputs.txt", "a")
file.write(completion)
file.write('\n')
file.close()
