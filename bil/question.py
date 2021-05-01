from tkinter import*

newroot = Tk()

newroot.geometry("500x320+400+200")
newroot.title("Menu")



def enter1():
	newroot.destroy()
	import restaurant_management_system


def enter2():
	newroot.destroy()
	import price	

label1 = Label(newroot, text="WELCOME TO BILLING SYSTEM ", fg="red" ,font="50")
label1.place(x=150,y=20)
label11 = Label(newroot, text="Bill", fg="red" ,font="20")
label11.place(x=150,y=50)

press_btn = Button(newroot, text="Press Here ",command= enter1, fg="white" , bg="black")
press_btn.place(x=290, y=50)

label21 = Label(newroot, text="Change Price" , fg="red" ,font="20")        
label21.place(x=150, y=80)

press1_btn = Button(newroot, text="Press Here",  command= enter2, fg="white" , bg="black")
press1_btn.place(x=290, y=80)

newroot.mainloop()
