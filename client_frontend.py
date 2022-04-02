import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import * 
from socket import *
from socket import inet_aton
import client_backend
from threading import Thread

class Lotfi(tk.Entry):
    def __init__(self, master=None, **kwargs):
        self.var = tk.StringVar()
        tk.Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.old_value = ''
        self.var.trace('w', self.check)
        self.get, self.set = self.var.get, self.var.set

    def check(self, *args):
        if self.get().isdigit(): 
            # the current value is only digits; allow this
            self.old_value = self.get()
        else:
            # there's non-digit characters in the input; reject this 
            self.set(self.old_value)


# this is the function called when the button is clicked
def connectButton():
    print('connect clicked')
    inp = ipInput.get()
    inp1 = portInput.get()

    try:
        inet_aton(inp)
        if len(inp1) != 4:
            tk.messagebox.showerror("Error", "Invalid Port Number")
            return
        client_backend.connectServer(inp,int(inp1))
        connection_text['text'] = 'Connected'
        receive_thread.start()

    except OSError:
        tk.messagebox.showerror("Error", "Invalid IP Address.")

def receiving():
    while(1):
        msgReceived= None
        msgReceived = client_backend.receiveMessage()

        if msgReceived != None:
            received_text['text'] = msgReceived
        else:
            print("nothing to print")

def sendButton():
    print('send clicked')
    send_thread = Thread(target=sending)
    send_thread.start()
    
def sending():
    inp = MessageInput.get()

    if len(inp) == 0 or client_backend.connectionFlag == False:
        return

    client_backend.sendMessage(inp)

if __name__ == "__main__":
    root = Tk()
    
    # This is the section of code which creates the main window
    root.geometry('580x410')
    root.configure(background='#F0F8FF')
    root.title('Messenger Client')
    canvas = Canvas(background='#F0F8FF', highlightthickness=1, highlightbackground="grey")
    canvas.place(x=27, y=115, width=525, height=120)

    # This is the section of code which creates the a label
    Label(root, text='Enter IP Address:', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=50, y=32)
    Label(root, text='Port Number:', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=80, y=60)

    # This is the section of code which creates a text input box
    ipInput=Entry(root)
    ipInput.place(x=177, y=32, width=150)

    portInput=Lotfi(root)
    portInput.place(x=177, y=60, width=150)


    # This is the section of code which creates a button
    Button(root, text='Connect', bg='#00CED1', font=('arial', 12, 'normal'), command=connectButton).place(x=347, y=38)
    Button(root, text='Send', bg='#00CED1', font=('arial', 12, 'normal'), command=sendButton, width=10).place(x=452, y=370)

    # This is the section of code which creates a text input box
    MessageInput=Entry(root, width=58, font=('Arial 12'))
    MessageInput.place(x=27, y=242, height=120)


    # This is the section of code which creates the a label
    received_text = Label(root, text='', bg='#F0F8FF', font=('arial', 12, 'normal'))
    received_text.place(x=30, y=120)
    connection_text = Label(root, text='Not Connected', bg='#F0F8FF', font=('arial', 12, 'normal'))
    connection_text.place(x=440, y=40)
    Label(root, text='Incoming Message:', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=27, y=90)

    receive_thread = Thread(target=receiving)

    root.mainloop()