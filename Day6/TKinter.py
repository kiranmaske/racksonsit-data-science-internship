# import tkinter as Tk
# #Button
# m = Tk.Tk()
# m.title("AIML Batch")
# btn = Tk.Button(m,text="Stop",width=25,command=m.destroy)
# btn.pack()
# m.mainloop()


#  canvas

from tkinter import *
# master = Tk()
# w = Canvas(master,width=40,height=60)
# w.pack()
# cn_height = 20
# cn_width = 200
# w.create_line(0,cn_height,cn_width,cn_height)
# mainloop()



# m = Tk()
# a = IntVar()
# b = IntVar()
# Checkbutton(m,text="Cricket",variable=a).grid(row=0,sticky=W)
# Checkbutton(m,text="Football",variable=b).grid(row=1,sticky=W)
# mainloop()


# m = Tk()
# Label(m,text="First Name:").grid(row=0)
# Label(m,text="Lasts Name:").grid(row=1)
# textbox1 = Entry(m)
# textbox2 = Entry(m)
# textbox1.grid(row=0,column=1)
# textbox2.grid(row=2,column=1)
# mainloop()




m = Tk()
frame = Frame(m)
frame.pack()
bottomfram = Frame(m)
bottomfram.pack(side = BOTTOM)
redBtn = Button(frame,text="RedBtn",fg="red")
redBtn.pack(side=LEFT)
blueBtn = Button(frame,text="BlueBtn",fg="blue")
blueBtn.pack(side=LEFT)
greenBtn = Button(frame,text="GreenBtn",fg="green")
greenBtn.pack(side=LEFT)
blackBtn = Button(bottomfram,text="BlackBtn",fg="black")
blackBtn.pack(side=BOTTOM)
mainloop()

