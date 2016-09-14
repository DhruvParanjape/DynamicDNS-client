from requests import get

username = "dhruv.paranjape@quickheal.com"
password = "admin@123"
domain = "dhruv1.authorizeddns.us"
ip = "4.3.2.1"

fetch_url = "https://nic.changeip.com/nic/update?hostname=%s&myip=%s" %(domain, ip)

response = get(fetch_url, auth=(username, password))

print(response.text)
