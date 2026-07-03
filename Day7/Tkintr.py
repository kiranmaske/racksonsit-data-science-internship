# listbox
# from tkinter import *
# m = Tk()
# lst = Listbox(m)
# lst.insert(1,"Python")
# lst.insert(2,"Data Science")
# lst.insert(3,"AIML")
# lst.insert(4,"C & C++")
# lst.insert(5,"Java EE")
# lst.insert(6,"Other language")
# lst.pack()
# m.mainloop()

# Menu

# from tkinter import *
# m = Tk()
# menu = Menu(m)
# m.config(menu=menu)
# filemenu = Menu(menu)
# menu.add_cascade(label = 'File', menu=filemenu)
# filemenu.add_command(label="New")
# filemenu.add_command(label="Open")
# filemenu.add_separator()
# filemenu.add_command(label="Exit",command=m.quit)
# helpmenu = Menu(menu)
# menu.add_cascade(label="Help",menu=helpmenu)
# helpmenu.add_command(label="About")
# m.mainloop()



# message

from tkinter import *
m = Tk()
# msg = "This is our GUI Batch in AIML"
# msgmain = Message(m,text=msg)
# msgmain.config(bg="Yellow")
# msgmain.pack()
# m.mainloop()


# radio button
# a = IntVar()
# Radiobutton(m,text="Male",variable=a,value=1).pack(anchor= W)
# Radiobutton(m,text="Female",variable=a,value=2).pack(anchor=W)
# m.mainloop()



# Scale
# s = Scale(m,from_=0,to=40)
# s.pack()
# s = Scale(from_=0,to=150,orient=HORIZONTAL)
# s.pack()
# m.mainloop()

 # scrollbar
scrbar = Scrollbar(m)
scrbar.pack(side=RIGHT,fill=Y)
lst = Listbox(m,yscrollcommand=Scrollbar.set)
for ln in range(120):
    lst.insert(END,'This is scrollbar with line n',str(ln))
    lst.pack(side=LEFT,fill=BOTH)
    scrbar.config(command=lst.yview)
    m.mainloop()
    
    
    
# txt = Text(m,height=3,width=40)
# txt.pack()
# txt.insert(END,"Python-Programing\nBest Teaching")
# m.mainloop()