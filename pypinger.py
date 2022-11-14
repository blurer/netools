#!/usr/bin/env python3

import pandas as pd
import os
import response
import argparse
import netaddr

'''
Examples:
./main.py -t csv -f ipam <-- csv file named ipam (column named ipAddress w/ ips)
./main.py -t range -n 10.0.0.0/24 <--pings 10.0.0.0-255
./main.py -t ip -i 10.1.1.1 <-- pings 10.1.1.1
./main.py -t txt -f ip <-- txt file named ip (one per line)
'''

parser = argparse.ArgumentParser(
                    prog = 'Pypinger',
                    description = 'This pings hosts to see if they are up or down.',
                    epilog = 'Specify the filename and it pings. Check requirements.txt if issues.')

parser.add_argument('-f','--filename')
parser.add_argument('-t', '--type', required=True)
parser.add_argument('-i', '--ipaddress')
parser.add_argument('-n', '--network')
args = parser.parse_args()

def pingdef():
    response = os.system("ping -c 1 -w 1 " + hostIP + " >> /tmp/output")
    if response == 0:
        print(hostIP + " is up")
    else:
        print(hostIP + " is down")

if args.type == 'csv':
    ipamFile = "/home/bl/dev/ipamTools/"+args.filename+".csv"
    ipam = pd.read_csv(ipamFile)
    for i in ipam['ipAddress']:
        hostIP = str(i)
        pingdef()    
if args.type == 'txt':
    ipFile = "/home/bl/dev/ipamTools/"+args.filename+".txt"
    ipam = pd.read_fwf(ipFile, names=['ipAddress'])
    for i in ipam['ipAddress']:
        hostIP = str(i)
        pingdef()
if args.type == 'range':
    ipam = list(netaddr.IPNetwork(args.network))
    for i in ipam:
        hostIP = str(i)
        pingdef()
if args.type == 'ip':
    hostIP = str(args.ipaddress)
    pingdef()