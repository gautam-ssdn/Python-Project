from tkinter import*
import tkinter.messagebox
left1 = Tk()
left1.geometry("1600x800+0+0")
left1.title("Change Price")

label4 = Label(left1, font = ('arial',50,'bold'), text ="Change Price", fg = "black", bd = 10, anchor = 'w')
label4.grid(row = 0)

fries_inp_p = StringVar()
Sandwich_inp_p = StringVar()
burger_inp_p = StringVar()
drinks_inp_p = StringVar()
Pasta_inp_p = StringVar()
Tacos_inp_p = StringVar()

def update():
        
        import pymysql
        db=pymysql.connect("localhost","root","","gautam")
        cursor=db.cursor()
        sql1="UPDATE MENU SET PRICE='%s' WHERE ITEM_NAME='fries'" %(int(fries_inp_p.get()))
        sql2="UPDATE MENU SET PRICE='%s' WHERE ITEM_NAME='sandwich'" %(int(Sandwich_inp_p.get()))     
        sql3="UPDATE MENU SET PRICE='%s' WHERE ITEM_NAME='burger'" %(int(burger_inp_p.get()))
        sql4="UPDATE MENU SET PRICE='%s' WHERE ITEM_NAME='drinks'" %(int(drinks_inp_p.get()))
        sql5="UPDATE MENU SET PRICE='%s' WHERE ITEM_NAME='pasta'" %(int(Pasta_inp_p.get()))
        sql6="UPDATE MENU SET PRICE='%s' WHERE ITEM_NAME='tacos'" %(int(Tacos_inp_p.get()))

        try:
                cursor.execute(sql1)
                cursor.execute(sql2)
                cursor.execute(sql3)
                cursor.execute(sql4)
                cursor.execute(sql5)
                cursor.execute(sql6) 
                db.commit()
        except Exception as e :
                
                print(e)
                db.rollback()

        db.close()    

        tkinter.messagebox.showinfo('Update Box','Successfully Updated')
	#f2.close()	

def reset1():
	fries_inp_p.set("")
	Sandwich_inp_p.set("")
	burger_inp_p.set("")
	drinks_inp_p.set("")
	Pasta_inp_p.set("")
	Tacos_inp_p.set("")

def qexit1():
	left1.destroy()

def printfn():
        import pymysql
        
	
def backfn():
	left1.destroy()
	import question


fries = Label(left1, font=('arial',16,'bold'),text = "Fries", bd = 16, anchor = 'w' )
fries.grid(row=1,column=0,sticky = E)
txt_fries = Entry(left1,font=('arial',16,'bold'), textvariable=fries_inp_p, bd=10, insertwidth =4,bg = "red", justify ='right')
txt_fries.grid(row=1,column=1)

Sandwich = Label(left1, font=('arial',16,'bold'),text = "Sandwich", bd = 16, anchor = 'w' )
Sandwich.grid(row=2,column=0,sticky = E)
txt_Sandwich = Entry(left1,font=('arial',16,'bold'), textvariable=Sandwich_inp_p, bd=10, insertwidth =4,bg = "red", justify ='right')
txt_Sandwich.grid(row=2,column=1)


burger = Label(left1, font=('arial',16,'bold'),text = "Burger", bd = 16, anchor = 'w' )
burger.grid(row=3,column=0,sticky = E)
txt_burger = Entry(left1,font=('arial',16,'bold'), textvariable=burger_inp_p, bd=10, insertwidth =4,bg = "red", justify ='right')
txt_burger.grid(row=3,column=1)

drinks = Label(left1, font=('arial',16,'bold'),text = "Drinks", bd = 16, anchor = 'w' )
drinks.grid(row=4,column=0,sticky = E)
txt_drinks = Entry(left1,font=('arial',16,'bold'), textvariable=drinks_inp_p, bd=10, insertwidth =4,bg = "red", justify ='right')
txt_drinks.grid(row=4,column=1)

Pasta = Label(left1, font=('arial',16,'bold'),text = "Pasta", bd = 16, anchor = 'w' )
Pasta.grid(row=5,column=0,sticky = E)
txt_Pasta = Entry(left1,font=('arial',16,'bold'), textvariable=Pasta_inp_p, bd=10, insertwidth =4,bg = "red", justify ='right')
txt_Pasta.grid(row=5,column=1)

Tacos = Label(left1, font=('arial',16,'bold'),text = "Tacos", bd = 16, anchor = 'w' )
Tacos.grid(row=6,column=0,sticky = E)
txt_Tacos = Entry(left1,font=('arial',16,'bold'), textvariable=Tacos_inp_p, bd=10, insertwidth =4,bg = "red", justify ='right')
txt_Tacos.grid(row=6,column=1)


btn_update = Button(left1, padx= 16, pady= 8, bd= 16, fg= "white", font=('arial',16,'bold'), width=10, text= "Update", bg= "red",command = update)
btn_update.grid(row=7, column= 1)

btn_reset1 = Button(left1, padx= 16, pady= 8, bd= 16, fg= "white", font=('arial',16,'bold'), width=10, text= "Reset", bg= "red",command = reset1)
btn_reset1.grid(row=7, column= 2)

btn_exit1 = Button(left1, padx= 16, pady= 8, bd= 16, fg= "white", font=('arial',16,'bold'), width=10, text= "Exit", bg= "red",command = qexit1)
btn_exit1.grid(row=7, column= 3)

btn_print = Button(left1, padx= 16, pady= 8, bd= 16, fg= "white", font=('arial',16,'bold'), width=10, text= "print", bg= "red",command = printfn)
btn_print.grid(row=7, column= 4)

btn_back = Button(left1, padx= 16, pady= 8, bd= 16, fg= "white", font=('arial',16,'bold'), width=10, text= "Back", bg= "red",command = backfn)
btn_back.grid(row=8, column= 3)



left1.mainloop()





