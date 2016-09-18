from ddclient.providers.freedns import freeDNS
from ddclient.providers.duckdns import DuckDNS
from ddclient.providers.Changeip import ChangeIP
from ddclient.Configurators.Logger import Log
from ddclient.Configurators.ConfigurationReader import FetchParameters
from ddclient.Configurators.Interface import GetIPfromInterface
from daemon import DaemonContext
from time import sleep


#config file path
config_file_path = "/etc/ddupdater.conf"

#daemonize
with DaemonContext():

	while  True:
		#Read the config
		provider, username, password, domain, iface_name, update_interval = FetchParameters(config_file_path)
		if (provider == freeDNS):
			freeDNS(username, password, domain)
		elif (provider == DuckDNS):
			ip = GetIPfromInterface(iface_name)
			DuckDNS(password,domain,ip)
		elif (provider == ChangeIP):
			ip = GetIPfromInterface(iface_name):
			ChangeIP(username,password,domain,ip)
		else :
			Log("Unknown provider configured shutting down...")
			Log("Provider configured : "+provider)
		
		#sleep for expected time.
		sleep(update_interval)
