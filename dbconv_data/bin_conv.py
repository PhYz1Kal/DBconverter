from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import webbrowser
import os

def app():
    if os.path.isdir('/home/pi/Desktop/')==True:
        if os.path.isfile('/boot/config.txt')==True:
            root=Tk()
            root.title("DBconv")
            root.geometry('270x90')
            root.resizable(False,False)
            root.config(bg='white')
            f=Frame(root,bg="white")
            f.pack(fill="both",expand=1)
            val=Entry(f,width=28)
            val.place(x=6,y=5)
            def deci():
                try:
                    global num
                    global a
                    global hexadecimal
                    num=str(val.get())
                    number=int(num)
                    hexadecimal=hex(number)
                    a=bin(number)
                    lb.config(text=hexadecimal)
                    lb1.config(text=a)
                except ValueError:
                    lb.config(text='input must be only integer')
                    lb1.config(text='')
                root.after(1, deci)
            def save():
                if(os.path.isfile('/home/pi/Desktop/conversion.txt'))==True:
                    if mb.askyesno('Warning','The file already exists, overwrite it?')==True:
                        with open('/home/pi/Desktop/conversion.txt','w') as f:
                            f.write('Input: '+num)
                        with open('/home/pi/Desktop/conversion.txt','a') as f:
                            f.write('\nbin: '+a)
                        with open('/home/pi/Desktop/conversion.txt','a') as f:
                            f.write('\nhex: '+hexadecimal)
                        if os.path.isfile('/home/pi/Desktop/conversion.txt')==True:
                            mb.showinfo('Info','The file "conversion.txt" has been saved in the Desktop')
                        else:
                            mb.showwarning('Error','Something went wrong, retry')
                    else:
                        print()
                else:
                    with open('/home/pi/Desktop/conversion.txt','w') as f:
                        f.write('Input: '+num)
                    with open('/home/pi/Desktop/conversion.txt','a') as f:
                        f.write('\nbin: '+a)
                    with open('/home/pi/Desktop/conversion.txt','a') as f:
                        f.write('\nhex: '+hexadecimal)
                    if os.path.isfile('/home/pi/Desktop/conversion.txt')==True:
                        mb.showinfo('Info','The file "conversion.txt" has been saved in the Desktop')
                    else:
                        mb.showwarning('Error','Something went wrong, retry')
            def openf():
                file=fd.askopenfile(initialdir='/home/pi/Desktop/',mode='r',filetypes =[('Conversion Files', '*.conv')])
                content=file.read()
                val.delete(0,END)
                val.insert(0,content)
                if content=='':
                    mb.showerror('Error','The file is empty!')
            
            def gen():
                file=fd.asksaveasfile(initialdir='/home/pi/Desktop/',filetypes=[('Conversion Files','*.conv')])
                file.write(num)

            def link():
                url='file:///home/pi/Desktop/.DBconv/index.html'
                webbrowser.open(url,new=2)

            menubar = Menu(root)
            filemenu = Menu(menubar, tearoff=0,activeborderwidth=0,bd=1)
            filemenu.add_command(label="New",command=app)
            filemenu.add_command(label="Open",command=openf)
            filemenu.add_command(label="Save as txt",command=save)
            filemenu.add_command(label="Exit",command=root.destroy)
            menubar.add_cascade(label="File",menu=filemenu)
            toolmenu=Menu(menubar,tearoff=0,activeborderwidth=0,bd=1)
            toolmenu.add_command(label="Generate conv file",command=lambda:gen())
            menubar.add_cascade(label="Tools",menu=toolmenu)
            helpmenu = Menu(menubar,tearoff=0,activeborderwidth=0,bd=1)
            helpmenu.add_command(label="Bug report",command=link)
            menubar.add_cascade(label="Help",menu=helpmenu)

            b=Button(f,text="",bg="white",fg="black",width=3,border=0,highlightthickness = 0, bd = 0,activebackground='white',command=root.after(20, deci))
            b.place(x=11005,y=5)
            lb=Label(f,bg="white",fg="black")
            lb.place(x=10,y=35)
            lb1=Label(f,bg="white",fg="black")
            lb1.place(x=10,y=60)
            root.config(menu=menubar)
            root.mainloop()
        else:
            root=Tk()
            root.title("")
            root.geometry('1x1')
            mb.showerror("Error","Sorry, your device is not supported")
            exit()
    else:
        root=Tk()
        root.title("")
        root.geometry('1x1')
        mb.showerror("Error","Sorry, your device is not supported")
        exit()

app()