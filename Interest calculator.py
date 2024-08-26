from tkinter import *

root = Tk()
root.title("Simple interest calculator")
root.configure(background="Light green")
root.geometry("500x300")
root.resizable(False, False)

label = Label(root, background="light green")
label.grid(column=0, row=0)


def calculate():
    a = int(enter_1.get())
    i = int(enter_2.get())
    y = int(enter_3.get())
    total = a*i*y/100
    label_4 = Label(root, text=total, background="Light Green", font=("ds-digital", 20), textvariable=c5)
    label_4.grid(row=5, column=1, padx=20, pady=10)
    enter_3.delete(0, END)
    enter_1.delete(0, END)
    enter_2.delete(0, END)


label_1 = Label(root, text="Enter amount  ", foreground="Black", background="light green", font=("ds-digital", 10))
label_1.grid(column=0, row=1, padx=20, pady=10)
label_1.configure(anchor="w")

enter_1 = Entry(root, font=("ds-digital", 10))
enter_1.grid(column=1, row=1, padx=20, pady=10)

label_2 = Label(root, text="Enter interest rate  ", background="Light Green", font=("ds-digital", 10))
label_2.grid(column=0, row=2, padx=20, pady=10)
label_2.configure(anchor="w")

enter_2 = Entry(root, font=("ds-digital", 10))
enter_2.grid(column=1, row=2, padx=20, pady=10)

label_3 = Label(root, text="Enter year  ", background="Light Green", font=("ds-digital", 10))
label_3.grid(column=0, row=3, padx=20, pady=10)
label_3.configure(anchor="w")

enter_3 = Entry(root, font=("ds-digital", 10))
enter_3.grid(column=1, row=3, padx=20, pady=10)

button = Button(root, height=3, width=15, text="Calculate", font=("ds-digital", 10), activebackground="Black",
                activeforeground="White", background="green", foreground="Black", command=calculate)
button.grid(row=4, column=1, padx=20, pady=10)
button.configure(anchor="center")

root.mainloop()
