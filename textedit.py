from tkinter import *
from tkinter import messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

root = Tk()
root.geometry("700x500")
root.resizable(0,0)
root.title("Untitled - texteditor")
root.wm_iconbitmap("C:\\Users\\USER\\Downloads\\internship\\Text_editor\\textedit.ico")

def newFile(): 
    global file
    root.title("Untitled - texteditor")
    file = None
    TextArea.delete(1.0,END)

def openFile():  
    global file
    file = askopenfilename(defaultextension=".txr",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "- texteditor")
        TextArea.delete(1.0,END)
        f = open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()

def saveas():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txr",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
        tmsg.showinfo("Save","Your file has been updated.")

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txr",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file + "- texteditor"))
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def delete():
    file_path = os.path.basename(file)
    if os.path.isfile(file_path):
        os.remove(file_path)
        TextArea.delete(1.0, END)
        tmsg.showinfo("Deleted!!","File has been deleted.")
    else:
        tmsg.showinfo("Not Found!!", "File does not exist.")

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():    
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    tmsg.showinfo("Notepad","Created by NB - Coder.")

def rate():
    value = tmsg.askquestion("Rate US","Was Your Experience Good??")
    if value=="yes":
        msg = tmsg.showinfo("Experience","Great. Rate us on Appstore please.")
    else:
        msg = tmsg.showinfo("Experience","Tell us what went wrong.")

mainmenu = Menu(root)
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

mainmenu.add_command(label="Exit",command=quit)
root.config(menu=mainmenu)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
TextArea = Text(root,font="lucida 13",yscrollcommand= scrollbar.set)
file=None
TextArea.pack(expand=True,fill=BOTH)
scrollbar.config(command=TextArea.yview)

root.mainloop()