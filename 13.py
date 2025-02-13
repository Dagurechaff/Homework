from ipaddress import *
ip = '203.75.227.102'
ip_net = '203.75.224.0'
s = []
ip_addr = ip_address(ip)
for mask in range(1, 33):
	net = ip_network(ip + '/' + str(mask), 0)
	if str(net) == ip_net + '/' + str(mask):
		s.append(int(('1' * mask + '0' * 30)[16:24], 2))
print(len(set(s)))