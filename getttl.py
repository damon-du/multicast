# !/usr/bin/env python
#--*--coding=utf-8--*--
#打印收到的数据包的源IP和TTL值
 
from scapy.all import *
 
def testTTL(pkt):
    print(pkt.summary())
    try:
        if pkt.haslayer(IP):
            ipsrc = pkt.getlayer(IP).src
            ipdst = pkt.getlayer(IP).dst
            ttl = str(pkt.ttl)
            print('[+] Pkt FROM: '+ipsrc+'   TTL: '+ttl)
            print('Pkt dst: ',ipdst)
            print('*'*20)

    except:
        pass
 
def main():
    sniff(iface='Intel(R) Ethernet Connection (2) I219-LM', filter = 'ip src 172.17.2.68',prn=testTTL, store=0,count=0)
 
if __name__ == '__main__':
    main()