import tkinter as tk
from tkinter import ttk
from tkinter import * 

# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = portInput.get()
	return userInput


# this is the function called when the button is clicked
def startListeningButton():
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
root.title('Messenger Server')


# This is the section of code which creates the a label
Label(root, text='Port Number:', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=67, y=32)


# This is the section of code which creates a text input box
portInput=Entry(root)
portInput.place(x=177, y=32, width=150)


# This is the section of code which creates a button
Button(root, text='Start Listening', bg='#00CED1', font=('arial', 12, 'normal'), command=startListeningButton).place(x=347, y=22)
Button(root, text='Send', bg='#00CED1', font=('arial', 12, 'normal'), command=sendButton, width=10).place(x=452, y=370)

# This is the section of code which creates a text input box
MessageInput=Entry(root, width=58, font=('Arial 12'))
MessageInput.place(x=27, y=242, height=120)


# This is the section of code which creates the a label
Label(root, text='', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=27, y=62)


root.mainloop()
