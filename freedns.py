from hashlib import sha1
from requests import get

username = "dhruvparanjape"
password = "admin@123"
domain = "dhruv.chickenkiller.com"
fetch_url = "https://freedns.afraid.org/api/?action=getdyndns&v=2&sha="
update_url = ""
hash_string = username+"|"+password

token = sha1(str.encode(hash_string))

response = get(fetch_url+token.hexdigest())

data = response.text.split("\n")

for line in data:
	param = line.split("|")
	print(param)
	if domain == param[0]:
		update_url = param[-1]

print(update_url)
update_response = get(update_url)

print(update_response.text)