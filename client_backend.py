from http import client
from multiprocessing import connection
from socket import *
connectionFlag = False
client1 = socket()

def connectServer(ip, portNo):
    global client1
    client1.connect((ip,portNo))
    global connectionFlag
    connectionFlag = True
    print("Connected to the server")
    

def sendMessage(msgToServer):
    global connectionFlag, client1
    if connectionFlag:
        client1.send(bytes(str(msgToServer),'utf-8'))
        print("Data sent to server")
    else:
        print("Connection not established")

def receiveMessage():
    global connectionFlag
    if connectionFlag:
        msg=client1.recv(1024).decode()
        print('Recived from the server :',str(msg))
        return str(msg)
    else:
        print("Connection not established")
    
    return None