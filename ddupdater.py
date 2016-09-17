from freedns import freeDNS
from duckdns import DuckDNS
from Changeip import ChangeIP
from os import fork
from time import sleep

#daemonize
process_id = fork()

if process_id != 0:

	while  True:
		#Read the config
		#get ip from given interface
		#update url
		#sleep for expected time.
		sleep(5)
