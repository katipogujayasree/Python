# importing everything that exists in tkinter module
from tkinter import *

# create window
root = Tk()

#Window Size
root.geometry("550x450") #Width x Height
#main frame
w = Label(root, text ='Name of The Tool', font = ("Georgia",20)).pack() 
  
frame = Frame(root)
frame.pack()

#Create a Label
first_label= Label(frame, text="Please provide the below required information (All Fields marked “ * ” are MANDATORY)")
first_label.grid(row=0, column=0,padx = 2, pady = 15,columnspan=3)
#Create a Label with Entry
second_label = Label(frame, text="* TICKET NUMBER",fg="red").grid(row=1, column=0,sticky='w',padx = 50, pady = 15)
e1= Entry(frame).grid(row=1, column=1)
#Create a Label with dropdown list
third_label= Label(frame, text="  SEVERITY").grid(row=2, column=0,sticky='w',padx = 50, pady = 15)

var1 = StringVar(frame)
drop1 = OptionMenu(frame, var1, "Sev 1", "Sev 2", "Sev 3", "Sev 4", "Sev 5").grid(row=2,column=1)

#Create a Label with dropdown list
fourth_label = Label(frame, text="* CLIENT", fg="red").grid(row=3, column=0, sticky='w',padx = 50, pady = 15)

var1 = StringVar(frame)
drop1 = OptionMenu(frame, var1, "Client A", "Client B", "Client C", "Client D").grid(row=3,column=1)

#Create a Label with Entry
fifth_label = Label(frame, text="* SITE / LOCATION", fg="red").grid(row=4, column=0, sticky='w',padx = 50, pady = 15)
e4= Entry(frame).grid(row=4, column=1)

#Create a Label with dropdown list
sixth_label= Label(frame, text="  ISSUE TYPE").grid(row=5, column=0, sticky='w', padx = 50, pady = 15)

var1 = StringVar(frame)
drop1 = OptionMenu(frame, var1, "A", "B", "C", "D").grid(row=5,column=1)

#Create a Label with Radio Buttons
Seventh_label= Label(frame, text=" CMDB").grid(row=6, column=0, sticky='w',padx = 50, pady = 15)

ButtonVar6 = IntVar()


e2= Radiobutton(frame, text = "JUMPHOST SERVER", variable = ButtonVar6 , value=1).grid(row=6, column=1)
e2= Radiobutton(frame, text = "EXCEL SHEET", variable = ButtonVar6, value=2).grid(row=6, column=2)
#Function to call
def submit():
    return
#Create label button to submit
btn1 = Button(frame, text="Submit", command=submit,font = ("bauhaus 93",20), background= "blue").grid(row=7, column=2)

root.mainloop() 

