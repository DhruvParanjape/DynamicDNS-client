try:
	from syslog import syslog
	isUnix = True
except ImportError:
	from logging import basicConfig, debug
	isUnix = False
	logging.basicConfig(filename="ddclient.log", level=logging.DEBUG)


def Log(message):
	if isUnix = True:
		syslog(message)
	else:
		debug(message)
