import socket
import os
import time
def cls():
    os.system("cls")
def socket_connect():
    global host
    global port
    global s
    s=socket.socket()
    host=input("ENTER A HOST:")
    port=input("ENTER THE PORT(9999):")
    port=int(port)
    s.connect((host,port))
def socket_identity():
    global msg
    global dmsg
    print("WAITING FOR ID FROM SERVER")
    msg = s.recv(1024)
    dmsg=msg.decode("utf-8")

    print("A connection has been established with ur friend " + str(dmsg))
    myid = input("Send ur identity:")

    print("The identity has been sent")
    s.send(str.encode(myid, "utf-8"))
    print("Waiting for reply from  " + str(dmsg))

def socket_chat():
    while True:
        fc=s.recv(1024)
        sfc=fc.decode("utf-8")
        print(str(dmsg)+":"+str(sfc))
        ms=input("ME:")
        s.send(str.encode(ms,"utf-8"))
        print("Waiting for reply from"+str(dmsg))
def main():
    socket_connect()
    socket_identity()
    socket_chat()
main()





