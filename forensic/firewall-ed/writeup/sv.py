from Crypto.Util.number import *
from scapy.all import *

client = '172.21.30.1'
pkts = rdpcap('log.pcap')
res = dict()

for pkt in pkts:    
    src = pkt[IP].src
    dst = pkt[IP].dst
    dport = pkt[TCP].dport
    flags = pkt[TCP].flags

    key = tuple(sorted([src, dst]))
    val = res.get(key, list())

    if not val: 
        res[key] = val

    val.append([src, dst, dport, flags])

for key, val in res.items():
    prevPort = None
    prevFlag = ''
    curFlag = ''
    result = ''
    count = 0

    for e, i in enumerate(val):
        src, dst, dport, flags = i
        curFlag += str(flags)

        if curFlag == 'SSA':
            curFlag = ''
        elif curFlag == 'SRA':
            curFlag = ''
        elif curFlag == 'R':
            curFlag = ''
        elif curFlag == 'SS':
            result += long_to_bytes(prevPort)
            curFlag = str(flags)

        prevPort = dport

    if curFlag == 'S':
        result += long_to_bytes(prevPort)
    
    print(result)