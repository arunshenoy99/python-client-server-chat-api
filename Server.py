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
    conn,address=s.accept()
    print("The connection has been established at "+str(address[0])+" and port "+str(address[1]))
    send_commands(conn)
    s.close()
def send_commands(conn):
    while True:
        msg=raw_input("ME:")
        conn.send(str.encode(msg))
        reply=conn.recv(1024)
        sreply=str.decode(reply)
        print("REDWIZZ:"+sreply)
def main():
    socket_create()
    socket_bind()
    socket_accept()
main()
