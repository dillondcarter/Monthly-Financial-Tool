#!/usr/local/bin/python
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Monthly Financial Tool")

def calculate(*args):
    try:
        value = float(income.get())
        expenses.set("$"+str("%.2f" %(value * .60)))
        longTerm.set("$"+str("%.2f" %(value * .10)))
        vacation.set("$"+str("%.2f" %(value * .04)))
        carDown.set("$"+str("%.2f" %(value * .04)))
        homeDown.set("$"+str("%.2f" %(value * .02)))
        guiltFree.set("$"+str("%.2f" %(value * .20)))
        projection.set("$"+str("%.2f" %(value * .10 *( 1 + 0.05/4) ** (4*30))))

    except ValueError:
        pass
   

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

income = StringVar()
expenses = StringVar()
longTerm = StringVar()
vacation = StringVar()
carDown = StringVar()
homeDown = StringVar()
guiltFree = StringVar()
projection = StringVar()

income_entry = ttk.Entry(mainframe, width=7, textvariable=income)
income_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=expenses, foreground="#27ae60").grid(column=2, row=2, sticky=(W, E))
ttk.Label(mainframe, textvariable=longTerm, foreground="#27ae60").grid(column=2, row=3, sticky=(W, E))
ttk.Label(mainframe, textvariable=vacation, foreground="#27ae60").grid(column=2, row=4, sticky=(W, E))
ttk.Label(mainframe, textvariable=carDown, foreground="#27ae60").grid(column=2, row=5, sticky=(W, E))
ttk.Label(mainframe, textvariable=homeDown, foreground="#27ae60").grid(column=2, row=6, sticky=(W, E))
ttk.Label(mainframe, textvariable=guiltFree, foreground="#27ae60").grid(column=2, row=7, sticky=(W, E))
ttk.Label(mainframe, textvariable=projection, foreground="#27ae60").grid(column=2, row=9, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=8, sticky=W)


ttk.Label(mainframe, text="Enter Amount Here:", foreground = "#2c3e50").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="Income", foreground = "#2c3e50").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Expenses:", foreground = "#2c3e50").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="To Bills", foreground = "#2c3e50").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="Long Term Investing:", foreground = "#2c3e50").grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, text="To Vanguard", foreground = "#2c3e50").grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="Vaction Savings:", foreground = "#2c3e50").grid(column=1, row=4, sticky=E)
ttk.Label(mainframe, text="To Capital One", foreground = "#2c3e50").grid(column=3, row=4, sticky=W)
ttk.Label(mainframe, text="Car Down Payment Savings:", foreground = "#2c3e50").grid(column=1, row=5, sticky=E)
ttk.Label(mainframe, text="To Capital One", foreground = "#2c3e50").grid(column=3, row=5, sticky=W)
ttk.Label(mainframe, text="Home Down Payment Savings:", foreground = "#2c3e50").grid(column=1, row=6, sticky=E)
ttk.Label(mainframe, text="To Capital One", foreground = "#2c3e50").grid(column=3, row=6, sticky=W)
ttk.Label(mainframe, text="Guilt Free Spending:", foreground = "#2c3e50").grid(column=1, row=7, sticky=E)
ttk.Label(mainframe, text="To Schwab", foreground = "#2c3e50").grid(column=3, row=7, sticky=W)
ttk.Label(mainframe, text="Investing Will Yield:", foreground = "#2c3e50").grid(column=1, row=9, sticky=E)
ttk.Label(mainframe, text="in 30 Years", foreground = "#2c3e50").grid(column=3, row=9, sticky=W)


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

income_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()
