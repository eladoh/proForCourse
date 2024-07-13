from scapy.all import *
import time 
from scapy.layers.http import HTTPRequest, HTTPResponse # import HTTP packet
from colorama import init, Fore
import scapy.layers.l2
from scapy.layers.inet import IP



def sniff_packets(iface=None):
    if iface:
        sniff(filter="tcp port 80", prn=process_packet, iface=iface, store=False)
    else:
        sniff(filter="tcp port 80", prn=process_packet, store=False)


def process_packet(packet):
    #print(",ferkgio", type(packet))
    
    if packet.haslayer(HTTPRequest):
        url = packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode()
        ip = packet[IP].src
        #method = packet[HTTPRequest].Method.decode()
        for obj in packet:
            if HTTPRequest in obj:
                http_request = obj[HTTPRequest]

                method = http_request.Method.decode('utf-8')
                #print(method)
                if obj.haslayer("Raw"):
                    payload = obj[Raw].load.decode('utf-8')
                else:
                    payload = ""

                print(f"Payload: {payload}")



                # #print(obj.show())
                # http_request = obj[HTTPRequest]
                # print(http_request)

                # method = http_request.Method.decode('utf-8') if http_request.Method else ""
                # url = http_request.Path.decode('utf-8') if http_request.Path else ""
                
                # headers = http_request.fields
                # payload = http_request.payload
                
                # print(f"HTTP Request: {method} {url}")
                # print(f"Headers: {headers}")
                # print(f"Payload: {payload}")


        
        
sniff_packets()
