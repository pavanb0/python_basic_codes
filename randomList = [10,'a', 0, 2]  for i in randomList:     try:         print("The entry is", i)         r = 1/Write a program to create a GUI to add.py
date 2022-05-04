from tkinter import *
def submit():
    us=int( entry.get())
    us2=int( entry2.get())
    us3=str(us+us2)
    new=Tk()
    li=Label(new,text="the addition is "+us3,font=("Arial",25)).pack()
    new.mainloop()

window = Tk()
entry = Entry(window,font=("Arial",25),fg="#00FF00",bg="black")
entry.pack(side=LEFT)
entry2= Entry(window,font=("Arial",25),fg="#00FF00",bg="black")
entry2.pack(side=LEFT)
submit_button = Button(window,text="add",command=submit)
submit_button.pack(side=RIGHT)

window.mainloop()
