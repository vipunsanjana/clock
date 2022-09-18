from tkinter import *



from time import strftime

root=Tk()
root.title("vipun clock")

def time():
    string=strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)

label=Label(root,font=("MontserratAlternates-Bold",150),background="blue",foreground="cyan")
label.pack(anchor="center")
time()

mainloop()
