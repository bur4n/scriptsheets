#!/usr/bin/env python3

"""
MassiveNSlookup - The way to do a massive nslookup.
Usage:
  massivenslookup.py
  massivenslookup.py (-d | --domains) domain1 domain2 domain3 ... (-le | --log-error)  (-v | --verbose)
  massivenslookup.py (-f | --file) filename (-le | --log-error) (-v | --verbose)
  massivenslookup.py (-h | --help)
  massivenslookup.py --version
Options:
  -h, --help    Show this screen.
  --version     Show version.
"""

__author__ = 'Burvn'
__credits__ = ['Me', 'Python community']
__license__ = 'GNU General Public License v3.0'
__version__ = '0.3'
__maintainer__ = 'Burvn'
__status__ = 'Development'

import socket, sys, time, argparse
import os.path
from io import open

# Functions	
def is_valid_file(parser, arg):
    if not os.path.isfile(arg):
        parser.error("[+] The file \'%s\' does not exist!" % arg)
    else:
        return open(arg, 'r')  # return an open file handle


# Arguments
parser = argparse.ArgumentParser(description='Get IP from a list of domains/subdomains.')
parser.add_argument("-d", "--domains", nargs="*", dest="domains", help="single domain or a list of domains separated by space")
# check nargs, does not work with read() :S 
# parser.add_argument("-f", "--file", nargs="1", dest="filename", metavar="FILE", type=lambda x: is_valid_file(parser, x), help="get domains from external file (a domain per line)")
parser.add_argument("-f", "--file", dest="filename", metavar="FILE", type=lambda x: is_valid_file(parser, x), help="get domains from external file (a domain per line)")
parser.add_argument("-le", "--log-error", action="store_true", dest="log_error", help="store not resolved urls in a separated file")
parser.add_argument("-v", "--verbose", action="store_true", dest="verbose", help="verbose mode")
parser.add_argument("--version", action="store_true", dest="version", help="script version")
args = parser.parse_args()

# Get script version
if args.version:
	print("[+] Massivenslookup version: " + __version__)
	sys.exit()

# Domains list
if args.domains:
	domains = args.domains
# External file
elif args.filename:
	domains = args.filename.read().splitlines()
# Default domains
else:
	domains = ['google.com', 'www.google.com', 'yahoo.com', 'notavalidurl.com']

domains_ips = []
error = []
x = 1
y = 1

# Processing
print("[+] Processing... ")

for domain in domains:
	try: 
		ip = socket.gethostbyname(domain)
		shortlist = [domain, ip]

		# Verbose
		if args.verbose:
			print(shortlist)
			
		domains_ips.append(shortlist)
	except:
		error.append(domain)

# Log url => ip
resultfl = open("massivenslookup_result.log", "w")
for i in domains_ips:
	resultfl.write(str(x) + ". " + str(i).strip('[]').replace("'","").replace(","," =>") + "\n\r")
	x += 1
resultfl.close()

# Log errors
if args.log_error:
	errorfl = open("massivenslookup_error.log", "w")
	for e in error:
		errorfl.write(str(y) + ". " + str(e).strip('[]').replace("'","").replace(","," =>") + "\n\r")
		y += 1
	errorfl.close()