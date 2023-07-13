import inspect
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import os
import sys
import shutil

root = Tk()

def get_dir():
    dir=['','']
    dir[0] = filedialog.askdirectory(title='Choose the Root directory pls')
    dir[1] = filedialog.askdirectory(title = 'Choose the Target directory pls') + '/'
    if not os.path.exists(dir[0]): 
        dir[0] = os.path.abspath(inspect.getsourcefile(lambda:0))

    if not os.path.exists(dir[1]):
        dir[1] = os.path.expanduser('~')+'/'



    return dir

def zip_arch():
    ##Creating ZIP archive with name like the last dir name
    #>> Path to user home directory:  os.path.expanduser('~')
    dir_pathes=[]
    dir_pathes = get_dir()
    src = dir_pathes[0]
    trg = dir_pathes[1]
  
    ind = tkinter.messagebox.askyesno(title='ZIP confirmation',message='ZIP whole dir: \n'+src+'\nTo the dir:\n'+trg)
    if ind:
        shutil.make_archive(os.path.join(trg,last_dir),'zip',src)
    
def copy_dir():
    ##Creating Copy of chosen folder in chosen directory
    dir_pathes=[]
    dir_pathes = get_dir()
    src = dir_pathes[0]
    trg = dir_pathes[1]
  
    ind = tkinter.messagebox.askyesno(title='COPY confirmation',message='COPY whole dir: \n'+src+'\nTo the dir:\n'+trg)
    #>>Copy full tree with folders inside all at onece!
    if ind:
        last_dir = src[::-1]
        if last_dir.find('/',1)!=-1:
            pos = last_dir.find('/',1)
        elif last_dir.find('\\',1)!=-1:
            pos= last_dir.find('\\',1)
        check_dir = src[(len(src)-pos):]
        if os.path.exists(trg+check_dir):
            tkinter.messagebox.showinfo(title='Warning',message='The folder '+check_dir+' already exists in \n'+trg)
        else:
            shutil.copytree(src, trg, dirs_exist_ok=True)


def main():
    root.title('Copy / ZIP')
    root.geometry('300x100')
    frm = ttk.Frame(root)
    frm.grid(column=0,row=0,sticky="N")
    frm2 = ttk.Frame(frm,width = 30)
    frm2.grid(column=0,row=1)
    Lab1 =  ttk.Label(frm, text='What do U wanna start from: to Copy or to ZIP')
    Lab1.grid(column=0, row=0, sticky='N', pady = 20, padx=30)
    ttk.Button(frm2, text="Copy", command=copy_dir).grid(column=0, row=0, padx=3)
    ttk.Button(frm2, text='ZIP', command=zip_arch).grid(column=1, row=0, padx=3)
    ttk.Button(frm2, text='Close', command=sys.exit).grid(column=2, row=0, padx=3)
    root.mainloop()

if __name__=='__main__': main()


