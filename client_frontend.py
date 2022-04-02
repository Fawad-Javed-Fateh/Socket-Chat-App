import tkinter as tk
from tkinter import ttk
from tkinter import * 

# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = portInput.get()
	return userInput


# this is the function called when the button is clicked
def connectButton():
	print('clicked')

def sendButton():
	print('send clicked')


# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = MessageInput.get()
	return userInput

root = Tk()

# This is the section of code which creates the main window
root.geometry('580x410')
root.configure(background='#F0F8FF')
root.title('Messenger Client')


# This is the section of code which creates the a label
Label(root, text='Enter IP Address:', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=50, y=32)
Label(root, text='Port Number:', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=80, y=60)

# This is the section of code which creates a text input box
ipInput=Entry(root)
ipInput.place(x=177, y=32, width=150)

portInput=Entry(root)
portInput.place(x=177, y=60, width=150)


# This is the section of code which creates a button
Button(root, text='Connect', bg='#00CED1', font=('arial', 12, 'normal'), command=connectButton).place(x=347, y=38)
Button(root, text='Send', bg='#00CED1', font=('arial', 12, 'normal'), command=sendButton, width=10).place(x=452, y=370)

# This is the section of code which creates a text input box
MessageInput=Entry(root, width=58, font=('Arial 12'))
MessageInput.place(x=27, y=242, height=120)


# This is the section of code which creates the a label
Label(root, text='', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=27, y=90)


root.mainloop()
