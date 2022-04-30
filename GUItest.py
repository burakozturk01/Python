from tkinter import *

root = Tk()
root.title("Simp Calc")

e = Entry(root, width=35)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    if type(number) == int:
        global summary
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))

    elif number == "clr":
        e.delete(0, END)

    elif number == "+":
        first_num = e.get()
        if first_num != "":
            global f_num
            f_num = int(first_num)
            e.delete(0, END)

    elif number == "=":
        second_num = e.get()
        if second_num != "":
            e.delete(0, END)
            e.insert(0, f_num + int(second_num))


button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))

button_list = [button_0, button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9]

button_add = Button(root, text="+", padx=39, pady=20, command=lambda: button_click("+"))
button_equal = Button(root, text="=", padx=91, pady=20, command=lambda: button_click("="))
button_clear = Button(root, text="Clear", padx=79, pady=20, command=lambda: button_click("clr"))

for r in range(1, 5):
    if r == 4:
        button_list[0].grid(row=4, column=0)
    else:
        for c in range(3):
            button_list[((-3) * r) + c].grid(row=r, column=c)

button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

root.mainloop()
