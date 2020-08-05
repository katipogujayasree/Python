from tkinter import *

root = Tk()

#root.geometry("200x150") 
  
w = Label(root, text ='Name of The Tool' , font = ("Helvetica Neue Bold",20)).pack() 
  
frame = Frame(root)
frame.pack()


first_label= Label(frame, text="Please provide the below required information (All Fields marked “ * ” are MANDATORY)")
first_label.grid(row=0, column=0,padx = 5, pady = 15)

second_label = Label(frame, text="* TICKET NUMBER",fg="red",font = ("Helvetica Neue Bold",10)).grid(row=1, column=0,sticky='w',padx = 100, pady = 15)
e1= Entry(frame).grid(row=1, column=1)


third_label= Label(frame, text="  SEVERITY",font = ("Helvetica Neue Bold",10)).grid(row=2, column=0,sticky='w',padx = 100, pady = 15)


ButtonVar1 = IntVar()
ButtonVar2 = IntVar()
ButtonVar3 = IntVar()
ButtonVar4 = IntVar()
ButtonVar5 = IntVar()


e2= Radiobutton(frame, text = "1", variable = ButtonVar1,padx=5, pady=10).grid(row=2, column=1,padx=40,pady=10)
e2= Radiobutton(frame, text = "2", variable = ButtonVar1,padx=5, pady=10).grid(row=2, column=2,padx=40,pady=10)
e2= Radiobutton(frame, text = "3", variable = ButtonVar1,padx=5, pady=10).grid(row=2, column=3,padx=40,pady=10)
e2= Radiobutton(frame, text = "4", variable = ButtonVar1,padx=5, pady=10).grid(row=2, column=4,padx=40,pady=10)
e2= Radiobutton(frame, text = "5", variable = ButtonVar1,padx=5, pady=10).grid(row=2, column=5,padx=40,pady=10)

fourth_label = Label(frame, text="* CLIENT", fg="red",font = ("Helvetica Neue Bold",10)).grid(row=3, column=0, sticky='w',padx = 100, pady = 15)
e3= Entry(frame).grid(row=3, column=1)


fifth_label = Label(frame, text="* SITE / LOCATION", fg="red",font = ("Helvetica Neue Bold",10)).grid(row=4, column=0, sticky='w',padx = 100, pady = 15)
e4= Entry(frame).grid(row=4, column=1)


sixth_label= Label(frame, text="  ISSUE TYPE",font = ("Helvetica Neue Bold",10)).grid(row=5, column=0, sticky='w', padx = 100, pady = 15)

var1 = StringVar(frame)
drop1 = OptionMenu(frame, var1, "A", "B", "C", "D").grid(row=5,column=1)


Seventh_label= Label(frame, text=" CMDB",font = ("Helvetica Neue Bold",10)).grid(row=6, column=0, sticky='w',padx = 100, pady = 15)

ButtonVar6 = IntVar()
ButtonVar7 = IntVar()


e2= Radiobutton(frame, text = "JUMPHOST SERVER", variable = ButtonVar6).grid(row=6, column=1)
e2= Radiobutton(frame, text = "EXCEL SHEET", variable = ButtonVar7).grid(row=6, column=2)


root.mainloop() 
