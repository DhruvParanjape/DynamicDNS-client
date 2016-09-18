from freedns import freeDNS
from duckdns import DuckDNS
from Changeip import ChangeIP
from daemon import DaemonContext
from time import sleep

#daemonize

with DaemonContext():

	while  True:
		#Read the config
		#get ip from given interface
		#update url
		#sleep for expected time.
		sleep(5)
