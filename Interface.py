from netifaces import ifaddresses

def GetIPfromInterface(interface_name):
	return ifaddresses(interface_name)[2][0]['addr']
