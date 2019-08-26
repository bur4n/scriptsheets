#!/usr/bin/env python3

"""
MassiveNSlookup - The way to do a massive nslookup.
Usage:
  massivenslookup.py
  massivenslookup.py (-h | --help)
  massivenslookup.py --version
Options:
  -h, --help    Show this screen.
  --version     Show version.
"""

__author__ = 'Burvn'
__credits__ = ['Me', 'Python community']
__license__ = 'GNU General Public License v3.0'
__version__ = '0.1'
__maintainer__ = 'Burvn'
__status__ = 'Development'

import socket
from io import open
import argparse

# Domains list
domains = ['google.com', 'www.google.com', 'yahoo.com', 'errorul.com']

domains_ips = []
error = []
x = 1
y = 1

for domain in domains:

	try: 
		ip = socket.gethostbyname(domain)

		shortlist = [domain, ip]
		print(shortlist)

		domains_ips.append(shortlist)
	except:
		error.append(domain)

resultfl = open("massivenslookup_result.log", "w")
errorfl = open("massivenslookup_error.log", "w")

for i in domains_ips:
	resultfl.write(str(x) + ". " + str(i).strip('[]').replace("'","").replace(","," =>") + "\n\r")
	x += 1

for e in error:
	errorfl.write(str(y) + ". " + str(e).strip('[]').replace("'","").replace(","," =>") + "\n\r")
	y += 1

resultfl.close()
errorfl.close()