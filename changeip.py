from requests import get

def ChangeIP(username,password,domain,ip):
  fetch_url = "https://nic.changeip.com/nic/update?hostname=%s&myip=%s" %(domain, ip)

  response = get(fetch_url, auth=(username, password))
  Log(response.text)
