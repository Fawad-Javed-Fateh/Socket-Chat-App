from socket import *

server=socket(AF_INET,SOCK_STREAM)
portNo=8000
server.bind(('localhost',portNo))#800 is the port number where server listens 
server.listen()
print('server is listening at port '+ str(portNo))
conn,address=server.accept()
print('Connected to the client')
while(1):
    msgToClient=input("Input message for client : ")
    conn.send(bytes(str(msgToClient),'utf-8'))
    print("Data send to the client")
    msg=conn.recv(1024).decode()
    print("msg from client : "+str(msg))