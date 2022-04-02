import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from client_frontend import keepReceiving 
import server_backend

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
def startListeningButton():
    print("start listening clicked")
    inp = portInput.get()

    if len(inp) != 4:
        tk.messagebox.showerror("Error", "Invalid Port Number")
        return

    server_backend.connect(int(inp))
    keepReceiving()

def keepReceiving():
    while(1):
        msgReceived= None
        msgReceived = server_backend.receiveMessage()

        if msgReceived != None:
            received_text['text'] = msgReceived

def sendButton():
    print('send clicked')
    inp = MessageInput.get()

    if len(inp) == 0:
        return

    server_backend.sendMessage(inp)
    keepReceiving()

if __name__ == "__main__":
    root = Tk()

    # This is the section of code which creates the main window
    root.geometry('580x410')
    root.configure(background='#F0F8FF')
    root.title('Messenger Server')


    # This is the section of code which creates the a label
    Label(root, text='Port Number:', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=67, y=32)


    # This is the section of code which creates a text input box
    portInput=Lotfi(root)
    portInput.place(x=177, y=32, width=150)


    # This is the section of code which creates a button
    Button(root, text='Start Listening', bg='#00CED1', font=('arial', 12, 'normal'), command=startListeningButton).place(x=347, y=22)
    Button(root, text='Send', bg='#00CED1', font=('arial', 12, 'normal'), command=sendButton, width=10).place(x=452, y=370)

    # This is the section of code which creates a text input box
    MessageInput=Entry(root, width=58, font=('Arial 12'))
    MessageInput.place(x=27, y=242, height=120)


    # This is the section of code which creates the a label

    received_text = Label(root, text='', bg='#F0F8FF', font=('arial', 12, 'normal'))
    received_text.place(x=27, y=62)

    root.mainloop()
