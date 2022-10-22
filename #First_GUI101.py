import tkinter as tk 
from tkinter import ttk
window = tk.Tk()

#Widgets
#=================#
window.title("Python Gui")
window.geometry("400x300+10+20")
window.resizable(False,False)

lb=ttk.Label(window, text='Nhap Ten cua ban')
lb.grid(column=0, row=0)

lb2= ttk.Label(window, text = "...")
lb2.grid(column=0, row=4)

lb3= ttk.Label(window, text = "Choose a number: ")
lb3.grid(column=1, row=0)

#button event
def click_me():
    action.configure(text="Bam vao")
    lb2.configure(text = "Hello" + " " + name.get() + " " + number_chosen.get())
    lb2.configure(foreground= 'green')

    

#add button
action =ttk.Button(window, text="Bam Vao", command= click_me)
action.grid(column=0,row=3)


#name
name = tk.StringVar()
name_entry = ttk.Entry(window, width = 20, textvariable = name)
name_entry.grid(column=0, row=1)

name_entry.focus()

#numberchosen
number = tk.StringVar()
number_chosen = ttk.Combobox(window, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1,2,3,4,5,6,7,8,9,10)
number_chosen.grid(column=1, row =1)
number_chosen.current(0)

#three checkbuttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(window, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=5, sticky=tk.W)                   

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(window, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=5, sticky=tk.W)                   

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(window, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=5, sticky=tk.W) 







#start
window.mainloop()



