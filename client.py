from http import client
from socket import *

client=socket()
portNo=8000
client.connect(('localhost',portNo))
print("Connected to the server")
while(1):  
    msg=client.recv(1024).decode()
    print('Recived from the server :',str(msg))
    msgToServer=input("Enter msg to send to the server :")
    client.send(bytes(str(msgToServer),'utf-8'))
    print("Data sent to server")