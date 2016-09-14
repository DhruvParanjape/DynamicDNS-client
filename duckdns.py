from requests import get

entered_domain = "dhruv.duckdns.org"
domain = entered_domain.split(".",1)[0]
token = "e3e437a4-6322-43a0-a15c-f9e5910443ca"
ip = "1.2.3.4"

update_url = ("https://nouser:%s"
"@www.duckdns.org/nic/update?hostname=%s"
"&myip=%s&wildcard=NOCHG&mx=NOCHG&backmx=NOCHG") % (token, domain, ip)

response = get(update_url)

if response.text == 'good':
	print("It's successful")

elif response.text == 'nochg':
	print("The IP already is "+ip)
else:
	print("I failed")