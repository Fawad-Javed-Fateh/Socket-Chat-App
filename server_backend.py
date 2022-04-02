from socket import *
connectionFlag = False
conn = None
address = None

# server=socket(AF_INET,SOCK_STREAM)
# portNo=8000
# server.bind(('localhost',portNo))#800 is the port number where server listens 
# server.listen()
# print('server is listening at port '+ str(portNo))
# conn,address=server.accept()
# print('Connected to the client')
# while(1):
#     msgToClient=input("Input message for client : ")
#     conn.send(bytes(str(msgToClient),'utf-8'))
#     print("Data send to the client")
#     msg=conn.recv(1024).decode()
#     print("msg from client : "+str(msg))

def connect(portNo):
    server1=socket(AF_INET,SOCK_STREAM)
    server1.bind(('localhost',portNo))
    server1.listen()
    print('server is listening at port '+ str(portNo))
    global conn, address
    conn,address=server1.accept()
    print('Connected to the client')
    global connectionFlag
    connectionFlag = True


def sendMessage(msgToClient):
    global connectionFlag, conn

    if connectionFlag:
        msgToClient=input("Input message for client : ")
        conn.send(bytes(str(msgToClient),'utf-8'))
        print("Data send to the client")
    else:
        print("Connection not established.")

def receiveMessage():
    global connectionFlag, conn
    if connectionFlag:
        msg=conn.recv(1024).decode()
        print("msg from client : "+str(msg))
        return str(msg)

    else:
        print("Connection not established")

    return None