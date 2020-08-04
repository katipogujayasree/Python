from tkinter import *

root = Tk()

#root.geometry("300x150") 
  
w = Label(root, text ='Name of The Tool',background = 'blue', foreground ="white" , font = ("forte" ,25)).pack()
  
frame = Frame(root) 
frame.pack()


first_label= Label(frame, text="Please provide the below required information (All Fields marked “*” are MANDATORY)")
first_label.grid(row=0, column=0,padx = 5, pady = 15)

second_label = Label(frame, text="* TICKET NUMBER",fg="red").grid(row=1, column=0,sticky='w',padx = 5, pady = 15)

e1= Entry(frame)
e1.grid(row=1, column=0)

third_label= Label(frame, text="   SEVERITY").grid(row=2, column=0, sticky='w',padx = 5, pady = 15)

ButtonVar1 = IntVar()
ButtonVar2 = IntVar()
ButtonVar3 = IntVar()
ButtonVar4 = IntVar()
ButtonVar5 = IntVar()

e2= Radiobutton(frame, text = "1", variable = ButtonVar1)
e2.grid(row=2, column=0,)
e2= Radiobutton(frame, text = "2", variable = ButtonVar1)
e2.grid(row=2, column=1)
e2= Radiobutton(frame, text = "3", variable = ButtonVar1)
e2.grid(row=2, column=2)
e2= Radiobutton(frame, text = "4", variable = ButtonVar1)
e2.grid(row=2, column=3)
e2= Radiobutton(frame, text = "5", variable = ButtonVar1)
e2.grid(row=2, column=4)

fourth_label = Label(frame, text="* CLIENT", fg="red").grid(row=3, column=0, sticky='w',padx = 5, pady = 15)

e3= Entry(frame)
e3.grid(row=3, column=0)

fifth_label = Label(frame, text="* SITE / LOCATION", fg="red").grid(row=4, column=0, sticky='w',padx = 5, pady = 15)

e4= Entry(frame)
e4.grid(row=4, column=0)

sixth_label= Label(frame, text="  ISSUE TYPE").grid(row=5, column=0, sticky='w', padx = 5, pady = 15)

# n = tk.StringVar() 
# monthchoosen = ttk.Combobox(window, width = 27, textvariable = n)

# monthchoosen['values'] = (' January',  
#                           ' February', 
#                           ' March', 
#                           ' April', 
#                           ' May', 
#                           ' June', 
#                           ' July', 
#                           ' August', 
#                           ' September', 
#                           ' October', 
#                           ' November', 
#                           ' December') 
  
# monthchoosen.grid(column = 1, row = 5) 
# monthchoosen.current() 

root.mainloop() 