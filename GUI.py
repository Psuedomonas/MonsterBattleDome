#!/usr/bin/python3.8
#filename: GUI.py

'''
GUI.py
Nicholas Zehm
2021-3-23
Tk graphical user interface
version 0.1
'''

from tkinter import *
import tkinter.scrolledtext as scrolledtext
from MenuOptions import *

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()


def txtEvent(event):
    if(event.state==12 and event.keysym=='c' ):
        return
    else:
        return "break"

'''Options Menu functions'''
def makeMonster():
    f = AddToPen
    #f.getOutput() #put stuff in the output box of the main window/frame
    del f

    
def dmMakeMonster():
    f = DMAddToPen
    del f


def kill():
    f = KillMonster
    del f


def feedingTime():
    pass


def selectMonsters():
    pass
    


''' Primary window and user interface '''
root = Tk()

frame1 = Frame(root)
menubar = Menu(frame1)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="New Pen", command = donothing)
filemenu.add_command(label = "Open Pen", command = donothing)
filemenu.add_command(label = "Save Pen", command = donothing)
filemenu.add_command(label = "Save Pen as...", command = donothing)

filemenu.add_separator()

filemenu.add_command(label = "Exit", command = root.quit)
menubar.add_cascade(label = "File", menu = filemenu)
optionsmenu = Menu(menubar, tearoff=0)

optionsmenu.add_command(label = "Show the monster pen", command = donothing)
optionsmenu.add_command(label = "Add a monster to the pen", command = makeMonster)
optionsmenu.add_command(label = "Dungeon Master: Add a custom monster to the pen", command = donothing)
optionsmenu.add_command(label = "Kill a monster in the pen", command = donothing)
optionsmenu.add_command(label = "Feed monsters in the pen", command = donothing)
optionsmenu.add_command(label = "Select monsters for the battle dome!", command = donothing)

menubar.add_cascade(label = "Options", menu = optionsmenu)

root.config(menu=menubar)

output = scrolledtext.ScrolledText(frame1, undo=True)#Text(frame1, fg='white', bg='black')
output['fg']='white'
output['bg']='black'
#scrollb = Scrollbar(frame1, command=output.yview)
#output['xscrollcommand']=scrollb.set

output.insert(INSERT,"python")
output.bind("<Key>", lambda e: txtEvent(e))
output.pack()
frame1.pack()

root.geometry("500x500")

#creation of an instance
#app = Window(root)

#mainloop 
root.mainloop()
root.destroy()
