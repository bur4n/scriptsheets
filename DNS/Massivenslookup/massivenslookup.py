#!/usr/bin/env python3

"""
MassiveNSlookup - The way to do a massive nslookup.
Usage:
  massivenslookup.py
  massivenslookup.py (-d | --domains) domain1 domain2 domain3 ... (-le | --log-error)  (-v | --verbose) (--filter)
  massivenslookup.py (-f | --file) filename (-le | --log-error) (-v | --verbose) (--filter)
  massivenslookup.py (-h | --help)
  massivenslookup.py --version
Options:
  -h, --help    Show this screen.
  --version     Show version.
"""

__author__ = 'Burvn'
__credits__ = ['Me', 'Python community']
__license__ = 'GNU General Public License v3.0'
__version__ = '0.4'
__maintainer__ = 'Burvn'
__status__ = 'Development'

import socket, sys, argparse
import os.path
from io import open

# Functions	
def is_valid_file(parser, arg):
    if not os.path.isfile(arg):
        parser.error("[+] The file \'%s\' does not exist!" % arg)
    else:
        return open(arg, 'r')  # return an open file handle

# Vars
domains_ips = []
ips = []
error = []

# Arguments
parser = argparse.ArgumentParser(description='Get IP from a list of domains/subdomains.')
parser.add_argument("-d", "--domains", nargs="*", dest="domains", help="single domain or a list of domains separated by space")
parser.add_argument("-f", "--file", dest="filename", metavar="FILE", type=lambda x: is_valid_file(parser, x), help="get domains from external file (a domain per line)")
parser.add_argument("-le", "--log-error", action="store_true", dest="log_error", help="log not resolved domains in a separated file")
parser.add_argument("-v", "--verbose", action="store_true", dest="verbose", help="verbose mode")
parser.add_argument("--filter", action="store_true", dest="filter", help="group domains in the same IP")
parser.add_argument("--version", action="store_true", dest="version", help="script version")
args = parser.parse_args()

# Get script version
if args.version:
	print("[+] Massivenslookup version: " + __version__)
	sys.exit()

# Domains list
if args.domains:
	domains = args.domains
	domains = list(set(domains)) # Erase duplicated domains
# External file
elif args.filename:
	domains = args.filename.read().splitlines()
	domains = list(set(domains)) # Erase duplicated domains
# Default domains
# [DEV] keep default domains? Is it usefull?
else:
	domains = ['google.com', 'www.google.com', 'yahoo.com', 'notavalidurl.com']

# Processing
print("[+] Processing... ")

for domain in domains:
	try: 
		ip = socket.gethostbyname(domain)
		ips.append(ip)
		# List: domain => ip
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
	i = str(i).strip('[]')
	i = i.replace("'","")
	i = i.replace(",","")
	#  resultfl.write(str(i).strip('[]').replace("'","").replace(",","") + "\n")
	resultfl.write(i + "\n")
resultfl.close()

# Filter
if args.filter:
	uniq_ips = list(set(ips))
	with open("massivenslookup_result.log", "r") as logfile:
		content = logfile.readlines()

	for ip in uniq_ips:
		if args.verbose:
			print("[+] Domains hosted in IP \'" + ip + "\': ")

		filtered_ips = filter(lambda item: ip in item , content)

		for domain_same_ip in filtered_ips:
			domain_same_ip = domain_same_ip.replace("\n","")
			domain_same_ip = domain_same_ip.split(" ")
			if args.verbose:
				print(domain_same_ip[0])
			print("\n")

# Log errors
if args.log_error:
	errorfl = open("massivenslookup_error.log", "w")
	for e in error:
		# errorfl.write(str(y) + ". " + str(e).strip('[]').replace("'","").replace(","," =>") + "\n\r")
		errorfl.write(str(e).strip('[]').replace("'","").replace(","," =>") + "\n\r")
	errorfl.close()