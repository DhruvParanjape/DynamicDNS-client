from hashlib import sha1
from requests import get
from os.path import isfile
from ddclient.Configurators.Logger import Log

def FreeDNS_2(username, password, domain):
	url = "https://%s:%s@freedns.afraid.org/nic/update?hostname=%s&myip=%s" %(username, password, domain, ip)
		update_response = get(url)
		#Updated status written in log file.
		Log(update_response.text)

def FreeDNS2(username, password, domain, ip):
	fetch_url = "https://freedns.afraid.org/api/?action=getdyndns&v=2&sha="
	cache_filename = "ddclient.cache"
	cache = ""
	update_url = ""
	if isfile(cache_filename) == True:
		with open(cache_filename,"w") as f:
			cache = f.read()
	if cache.split("|")[-1] == domain:
		update_url = cache.split("|")[0] + "&address=%s" %(ip)
		Log("sending "+update_url)
		update_response = get(update_url)
		#Updated status written in log file.
		Log(update_response.text)
	else:
		hash_string = username+"|"+password
		token = sha1(str.encode(hash_string))
		response = get(fetch_url+token.hexdigest())
		data = response.text.split("\n")

		for line in data:
			param = line.split("|")
			if domain == param[0]:
				update_url = param[-1]
		Log("sending "+update_url)
	
		update_response = get(update_url)
		#Updated status written in log file.
		Log(update_response.text)
		#write update url with the domain to the cache.
		with open(cache_filename,"w") as f:
			f.write(update_url+"|"+domain)
