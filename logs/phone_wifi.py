import subprocess
from datetime import datetime, timedelta

# pip install scapy
# Also needs dnet: https://pypi.python.org/pypi/dnet
try:
	from scapy.all import sniff, Ether, DHCP
except:
	print( "Needs Scapy library.")
	print( "pip install scapy")
	print( "Scapy needs dnet: https://pypi.python.org/pypi/dnet")
	exit()

#Set your interface
interface="en0"
#How long something needs to go dark before mentioning its back
alert_delay = timedelta(hours=2)
#Enter either the hostname or the MAC address
#  as the Key and the Phonetic name as the value to be heard.
#  Otherwise the hostname will try to be spoken
friendly_names = {
	"PersonOne-iPhone": "Person One",
	"aa:bb:cc:dd:ee:ff": "Person Two",
	}

###########
class Device():
	def __init__(self,name="",mac=""):
		self.name = name
		self.mac = mac
		self.last_seen = datetime.fromtimestamp(0)

all_devices = []

def new_join_action():
	""" 
	This can be replaced with any code you want to run
	when a device is joined aftering being unseen for alert_delay
	""" 
	subprocess.Popen(["say",say_string])

print( "Listening on interface {}".format(interface) )

while True:
	current_time = datetime.now()
	#listen on the interface for DHCP traffic
	a = sniff(iface=interface, filter="port 67 or port 68", count = 1)
	hostname = "Unknown"
	mac_address = a[Ether][0].src

	#When a packet is found, go through the DHCP options to find the hostname
	for opt in a[0][DHCP].options:
		#There's a bunch of information in the DHCP traffic, we just want the
		# information that's presented in a tuple
		if isinstance(opt,tuple):
			option,value = opt
			#if the option specifies the hostname, use that as the name
			if option == "hostname":
				say_hostname = hostname = value

	device = None
	for dev in all_devices:
		if dev.mac == mac_address:
			device = dev
	if not device:
		device = Device(name=hostname,mac=mac_address)
		all_devices.append(device)

	#if we have information in friendly_names about either, overwrite the say_hostname
	for item in [device.name,device.mac]:
		if item in friendly_names.keys():
			say_hostname = friendly_names[item]

	say_string =  "{}. has joined".format(say_hostname,mac_address)
	print( "{}: {} ({}) has joined".format(current_time,device.name,device.mac))
	if current_time > device.last_seen + alert_delay:
		new_join_action()
	device.last_seen = current_time