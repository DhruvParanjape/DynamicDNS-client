from requests import get
from ddclient.Configurators.Logger import Log

def DuckDNS(token,given_domain, ip):
	domain = entered_domain.split(".",1)[0]
	update_url = ("https://nouser:%s"
		"@www.duckdns.org/nic/update?hostname=%s"
		"&myip=%s&wildcard=NOCHG&mx=NOCHG&backmx=NOCHG") % (token, domain, ip)

	response = get(update_url)

	if response.text == 'good':
		Log("It's successful")

	elif response.text == 'nochg':
		Log("The IP already is "+ip)
	else:
		Log("I failed")
