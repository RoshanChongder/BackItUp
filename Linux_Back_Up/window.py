import tkinter as tk
from tkinter import filedialog , messagebox 
import os , time , subprocess 

# setting up the window 
root=tk.Tk()    
root.geometry("800x500")

ent1=tk.Entry(root,font=40)
ent1.insert(0,"select folder to zip")
ent1.grid(row=2,column=2)

ent2=tk.Entry(root,font=40)
ent2.insert(0,"Browse to the desired file")
ent2.grid(row=4,column=2)

# setting up the label 
l1=tk.Label(root,font=40)
l1.grid(row=6,column=2) 



path = ''

def browsefunc():
    global path 
    print("Browsing the file system")
    filepath = filedialog.askdirectory() 
    print(filepath) 
    ent1.delete(0,'end')
    ent1.insert( 0 , filepath ) # add this 
    path = filepath

def Clear() :
    l1.config(text="")
    subprocess.call("rm test", shell = True )


def backUp() :
    global path 
    if path == '' : 
        messagebox.showerror("Error" , "First select the target folder")
    else :
        #print("./File_BackUp.sh "+ path)
        #l1.config(text="")
        Clear()
        #l1.config( text = "Please select the target folder and click backUp and the please wait . . . . ")
        pro = subprocess.call("./File_BackUp.sh "+ path , shell = True )
        #time.sleep(5) 
        fp = open('test','r') 
        s = fp.read()
        l1.config(text = s) 

def Exit() :
    exit()

def browsefile() :
    global path 
    filename = filedialog.askopenfilename(initialdir = '/' ,title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*"))) 
    print(filename) 
    ent2.delete(0,'end')
    ent2.insert(0,filename) 
    path = filename 

def extract() :
    global path
    if path == '' :
        messagebox.showerror("Error" , "First select the target file")
    elif False :
        pass  # add if not tar.gz file is selected 
    else :
        #print("./File_BackUp.sh "+ path)
        #l1.config( text = " ") 
        Clear() 
        print("./Extact_tar.sh "+ path )
        pro = subprocess.call("./Extact_tar.sh "+ path , shell = True )
        #time.sleep(5) 
        fp = open('test','r')
        s = fp.read()
        l1.config(text = s) 




b1=tk.Button(root,text="Browse",font=40,command=browsefunc)
b2=tk.Button(root,text="BackUp",font=40,command=backUp)
b3=tk.Button(root,text="exit",font=40,command=Exit) 

b4=tk.Button(root,text="Browse",font=40,command=browsefile)
b5=tk.Button(root,text="Extract",font=40,command=extract)
b4.grid(row=4,column=4)
b5.grid(row=4,column=6)




b1.grid(row=2,column=4)
b2.grid(row=2,column=6)
b3.grid(row=4,column=8)
root.mainloop()
