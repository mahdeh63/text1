from tkinter import*
from random import*
def change_():
    color_="0123456789abcdef"
    sharp1w="#"
    sharp2bx="#"
    for i in range (6):
        sharp1w+=choices(color_)
        sharp2bx+=choices(color_)
    win.config(bg=sharp1w)
    lbright_.config(text=sharp1w)
    lwelcom_.config(bg=sharp1w)
    lwelcom_.config(fg=sharp2bx)
    lbleft_.config(text=sharp2bx)


        





win=Tk()
win.geometry("400x500")
win.title("change color")
win.resizable(0,0)
lwelcom_=Label(win,text="welcome",fg="black",font="arial  20 bold")
lwelcom_.pack()
btchange_=Button(win,text="change",command=change_)
btchange_.pack(pady=15)
lbright_=Label(win,text="backgrand?")
lbright_.pack(side=RIGHT,padx=30,pady=150)

lbleft_=Label(win,text='text welcome')
lbleft_.pack(side=LEFT,padx=30,pady=150)



win.mainloop()