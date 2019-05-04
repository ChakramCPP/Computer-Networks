import ipaddr
import random
 
network = ipaddr.IPv4Network('59.185.23.0/24')
randmon_ip = ipaddr.IPv4Address(random.randrange(int(network.network) + 1, int(network.broadcast) - 1))
