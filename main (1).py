import Admin
import student
import teacher
import parent
from tkinter import *

window = Tk()
window.geometry('1280x600')
window.title('Start Window')
def start():
    window = Toplevel()
    window.geometry('1080x600')
    l = Label(window, text='Login As', font='Times 20 bold')
    l.grid(row=0, column=3)
    Button(window, text='Admin', command=Admin.start, width=25, font=("Times New", 10), bd=5,
           bg="light blue").grid(row=2, column=0, sticky=N + S + E + W)
    Button(window, text='Student', command=student.start, width=25, font=("Times New", 10), bd=5,
           bg="light blue").grid(row=3, column=0, sticky=N + S + E + W)
    Button(window, text='Parent', command=parent.start, width=25, font=("Times New", 10), bd=5,
           bg="light blue").grid(row=4, column=0, sticky=N + S + E + W)
    Button(window, text='Teacher', command=teacher.start, width=25, font=("Times New", 10), bd=5,
           bg="light blue").grid(row=5, column=0, sticky=N + S + E + W)

##############################################################################################
Button(window, text='start', command=start, width=20, font=("Times New", 15),bd=-5,bg="light blue").place(x=410, y=290)
Label(window,text='E-SCHOOL',font=("Times New",60)).place(x=320,y=120)
window.mainloop()
