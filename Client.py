import socket
import os
def cls():
    os.system("cls")
s=socket.socket()
host="192.168.1.5"
port=9999
s.connect((host,port))
while True:
    msg=s.recv(1024)
    dmsg=str.decode(msg,"utf-8")
    print("FRIEND:"+str(dmsg))
    smsg=raw_input("ME:")
    if (smsg=="cls"):
        cls()
    s.send(smsg)
