from tkinter import*
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("Scientific calculator")
root.configure(background='powder blue')
root.resizable(width=False,height=False)
#root.geometry("480*568+0+0")

calc= Frame(root)
calc.grid()

menubar=Menu(calc)

filemenu = Menu(menubar ,tearoff=0)
menubar.add_cascade(label="False" , menu=filemenu)
filemenu.add_command(label="Standard")
filemenu.add_command(label="Scientific")
filemenu.add_separator()
filemenu.add_command(label="Exit")

root.config(menu=menubar)
root.mainloop()


#def Division(x,y):
   # try:
    #    total=(x / y)
    #except TypeError:
     #   total="You provided the wrong object type"
      #  return total


