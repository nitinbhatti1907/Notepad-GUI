# Title :- Notepad GUI
# Discription :- A notepad using Tkinter in Python is a simple text editor that allows users to create, edit, and save text files. The notepad is built using Tkinter, a GUI library for Python that makes it easy to create graphical interfaces for desktop applications. The notepad interface is created using Tkinter's widgets such as buttons, labels, and a text box. The buttons represent the various actions such as "Open," "Save," "Cut," "Copy," "Paste," etc. The text box is used to display and edit the contents of the text file.

from tkinter import *
from tkinter import messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

# Create a Tkinter GUI window
root = Tk()
root.geometry("700x500")
root.resizable(0,0)
root.title("Untitled - Notepad")
root.wm_iconbitmap("notepad.ico")

def newFile():
    '''
    This function is used to create a new text file in notepad
    '''

    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0,END)

def openFile():
    '''
    This function is used to open the pre-build text files in the pc
    '''

    global file
    file = askopenfilename(defaultextension=".txr",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file == "":
        file = None

    else:
        root.title(os.path.basename(file) + "- Notepad")
        TextArea.delete(1.0,END)
        f = open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()

def saveas():
    '''
    This file is use to update the content of the pre-bhild file
    '''

    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txr",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    else:
        #save old file with new content
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
        tmsg.showinfo("Save","Your file has been updated.")

def saveFile():
    '''
    This method is used to save the file on user system based on his choice
    '''

    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txr",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file == "":
            file = None
        else:
            # Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file + "- Notepad"))
    else:
        #save old file with new content
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def delete():
    '''
    This method is used to delete any pre-build file in the user system
    '''

    file_path = os.path.basename(file)
    if os.path.isfile(file_path):
        os.remove(file_path)
        TextArea.delete(1.0, END)
        tmsg.showinfo("Deleted!!","File has been deleted.")

    else:
        tmsg.showinfo("Not Found!!", "File does not exist.")

def cut():
    '''
    Use to cut the content in texbox
    '''

    TextArea.event_generate(("<<Cut>>"))

def copy():
    '''
    Use to copy the content in texbox
    '''
    TextArea.event_generate(("<<Copy>>"))

def paste():
    '''
    Use to paste the content in texbox
    '''
    TextArea.event_generate(("<<Paste>>"))

def about():
    '''
    Tells the information about creaters of this notepad
    '''

    tmsg.showinfo("Notepad","Created by NB - Coder.")

def rate():
    '''
    Users can rate the notepad through this function
    '''

    value = tmsg.askquestion("Rate US","Was Your Experience Good??")
    if value=="yes":
        msg = tmsg.showinfo("Experience","Great. Rate us on Appstore please.")
    else:
        msg = tmsg.showinfo("Experience","Tell us what went wrong.")

mainmenu = Menu(root)

#--> Create a menubar using Menu() function
m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="New",command=newFile)
m1.add_command(label="Open",command=openFile)
m1.add_command(label="Save",command=saveFile)
m1.add_separator()
m1.add_command(label="Save As",command=saveas)
m1.add_command(label="Delete",command=delete)
mainmenu.add_cascade(label="File",menu=m1)

m2=Menu(mainmenu,tearoff=0)
m2.add_command(label="Cut",command=cut)
m2.add_command(label="Copy",command=copy)
m2.add_command(label="Paste",command=paste)
mainmenu.add_cascade(label="Edit",menu=m2)

m3=Menu(mainmenu,tearoff=0)
m3.add_command(label="About Notepad",command=about)
m3.add_command(label="Rate Us",command=rate)
mainmenu.add_cascade(label="Help",menu=m3)

#--> use for exit from notepad
mainmenu.add_command(label="Exit",command=quit)
root.config(menu=mainmenu)

#--> create a scrollbar on rightend side of a textarea to scroll the content of a file
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
TextArea = Text(root,font="lucida 13",yscrollcommand= scrollbar.set)
file=None
TextArea.pack(expand=True,fill=BOTH)
scrollbar.config(command=TextArea.yview)

root.mainloop()