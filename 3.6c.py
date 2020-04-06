import socket
import os
def cls():
    os.system("cls")
def socket_connect():
    global host
    global port
    global s
    s=socket.socket()
    host=input("Enter a host:")
    port=input("Enter the port of the host(9999):")
    port=int(port)
    s.connect((host,port))
def socket_identity():
    global msg
    global dmsg
    msg = s.recv(1024)
    dmsg = str.decode(msg, "utf-8")
    print("A connection has been established with ur friend " + str(dmsg))
    myid = input("Send ur identity:")
    myid=str(myid)
    print("The identity has been sent")
    s.send(str.encode(myid))
def socket_chat():
    while True:
        fc=s.recv(1024)
        sfc=str.decode(fc)
        print(str(dmsg)+":"+str(sfc))
        ms=raw_input("ME:")
        s.send(str.encode(ms))
def main():
    socket_connect()
    socket_identity()
    socket_chat()
main()





