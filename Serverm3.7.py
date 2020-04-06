import sys
import socket

def socket_create():
    try:
        global host
        global port
        global s
        host=''
        port=9999
        s=socket.socket()
    except socket.error() as msg:
        print("SOCKET CREATION ERROR "+msg)
def socket_bind():
    try:
        global host
        global port
        global s
        s.bind((host,port))
        s.listen(5)
        print("YOU ARE ONLINE AND WAITING FOR YOUR FRIEND")
    except socket.error() as msg:
        print ("Socket binding error "+msg+" Retrying")
        socket_bind()
def socket_accept():
    global conn
    global address
    conn,address=s.accept()
    print("A CONNECTION HAS BEEN ESTABLISHED WITH A CLIENT AT "+str(address[0])+" and port "+str(address[1]))
    send_commands(conn)
def send_commands(conn):
    data = input("SEND YOUR IDENTITY:")
    conn.send(str.encode(data,"utf-8"))
    print("IDENTITY SENT TO CLIENT")
    print("WAITING FOR ID FROM CLIENT")
    cid = conn.recv(1024)

    scid = str(cid.decode("utf-8"))
    print("A CONNECTION HAS BEEN ESTABLISHED WITH YOUR FRIEND "+scid)
    while True:

        msg=input("ME:")
        conn.send(str.encode(msg,"utf-8"))
        print("WAITING FOR REPLY FROM  "+scid)
        reply=conn.recv(1024)
        sreply=str(reply.decode("utf-8"))
        print(scid+":"+sreply)
def main():

    socket_create()
    socket_bind()
    socket_accept()

main()
