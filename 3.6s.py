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
        print("Socket creation error "+msg)
def socket_bind():
    try:
        global host
        global port
        global s
        s.bind((host,port))
        s.listen(5)
        print("The socket has been binded and is listening for open connections")
    except socket.error() as msg:
        print ("Socket binding error "+msg+" Retrying")
        socket_bind()
def socket_accept():
    global conn
    global address
    conn,address=s.accept()
    print("The connection has been established at "+str(address[0])+" and port "+str(address[1]))
    send_commands(conn)
def send_commands(conn):
    data = input("SEND YOUR IDENTITY:")
    conn.send(str.encode(data))
    print("Identity sent to client")
    cid = conn.recv(1024)
    scid = str.decode(cid)
    while True:

        msg=input("ME:")
        conn.send(str.encode(msg))
        reply=conn.recv(1024)
        sreply=str.decode(reply)
        print(scid+":"+sreply)
def main():

    socket_create()
    socket_bind()
    socket_accept()

main()
