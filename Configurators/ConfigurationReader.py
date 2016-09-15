from configparser import ConfigParser

def FetchParameters(filename):
	config = ConfigParser()
	config.read(filename)

	username = config['Credentials']['username']
	password = config['Credentials']['password']
	domain = config['Credentials']['domain']
	interface = config['System']['interface']
	update = config['System']['update_interval']
	provider = config['System']['provider']

	return provider, username, password, domain, interface, update
