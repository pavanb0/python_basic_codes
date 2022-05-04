from tkinter import *
def submit():
    us=int( entry.get())
    if us%2==0:
        new=Tk()
        li=Label(new,text="number is even").pack()
        new.mainloop()
    else:
        new=Tk()
        li=Label(new,text="number is odd").pack()
        new.mainloop()
window = Tk()
entry = Entry(window,font=("Arial",50),fg="#00FF00",bg="black")
entry.pack(side=LEFT)
submit_button = Button(window,text="submit",command=submit)
submit_button.pack(side=RIGHT)
window.mainloop()
