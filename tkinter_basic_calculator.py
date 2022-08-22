"""
Very basic calculator with TKINTER module. Feel free to add thins to code. 
in some definitions. you ll get an error if you press +, /, *, -,  without any data.
I wanted to add basic try/except additional statements for some errors, but i was tired.
"""

from tkinter import *

root = Tk()
root.title("Basic Calculator")
root.geometry("134x312+2500+300")


user_entry = Entry(root)
user_entry.grid(row=0, column=0, columnspan=3)

data_width = 5
data_height = 2

first_data = 0
data_key = None


def button_click(number):
    current = user_entry.get()
    user_entry.delete(0, END)
    user_entry.insert(0, str(current) + str(number))  # Good move, adding a current variable.


def clear_data():
    global first_data, data_key
    first_data = 0
    data_key = None
    user_entry.delete(0, END)
    print("Data cleared by user...")
    print("first_data and data_tag set to None/zero")
    return


def sum_data():
    global first_data, data_key
    data_key = "sys_sum"
    first_data = float(user_entry.get())
    user_entry.delete(0, END)
    print("First data:", first_data)
    return


def sys_multiply():
    global first_data, data_key
    data_key = "sys_multiply"
    first_data = float(user_entry.get())
    user_entry.delete(0, END)
    print("First data: ", first_data)
    return


def sys_divide():
    global first_data, data_key
    data_key = "sys_divide"
    first_data = float(user_entry.get())
    user_entry.delete(0, END)
    print("First data:", first_data)
    return


def sys_extract():
    global first_data, data_key
    data_key = "sys_extract"
    first_data = float(user_entry.get())
    user_entry.delete(0, END)
    print("First data:", first_data)
    return


def data_equals():
    try:
        data_02 = float(user_entry.get())
        user_entry.delete(0, END)
        if data_key == "sys_sum":
            result = first_data + data_02
            user_entry.insert(0, str(result))
        elif data_key == "sys_multiply":
            result = first_data * data_02
            user_entry.insert(0, str(result))
        elif data_key == "sys_divide":
            result = first_data / data_02
            user_entry.insert(0, str(result))
        elif data_key == "sys_extract":
            result = first_data - data_02
            user_entry.insert(0, str(result))
    except:
        user_entry.insert(0, "Enter data...")


def quit_system():
    root.destroy()
    print("Terminated by user...")
    return


# region Button commands
button_1 = Button(root,
                  text="1",
                  width=data_width,
                  height=data_height,
                  command=lambda: button_click(1))
button_2 = Button(root,
                  text="2",
                  width=data_width,
                  height=data_height,
                  command=lambda: button_click(2))
button_3 = Button(root,
                  text="3",
                  width=data_width,
                  height=data_height,
                  command=lambda: button_click(3))
button_4 = Button(root,
                  text="4",
                  width=data_width,
                  height=data_height,
                  command=lambda: button_click(4))
button_5 = Button(root,
                  text="5",
                  width=data_width,
                  height=data_height,
                  command=lambda: button_click(5))
button_6 = Button(root,
                  text="6",
                  width=data_width,
                  height=data_height,
                  command=lambda: button_click(6))
button_7 = Button(root,
                  text="7",
                  width=data_width,
                  height=data_height,
                  command=lambda: button_click(7))
button_8 = Button(root,
                  text="8",
                  width=data_width,
                  height=data_height,
                  command=lambda: button_click(8))
button_9 = Button(root,
                  text="9",
                  width=data_width,
                  height=data_height,
                  command=lambda: button_click(9))
button_0 = Button(root,
                  text="0",
                  width=data_width,
                  height=data_height,
                  command=lambda: button_click(0))
button_clear = Button(root,
                      text="Clear",
                      width=data_width,
                      height=data_height,
                      command=clear_data)
button_sum = Button(root,
                    text="+",
                    width=data_width,
                    height=data_height,
                    command=sum_data)
button_equal = Button(root,
                      text="=",
                      width=18,
                      height=data_height,
                      command=data_equals)

button_multiply = Button(root,
                         text="*",
                         width=data_width,
                         height=data_height,
                         command=sys_multiply)

button_divide = Button(root,
                       text="/",
                       width=data_width,
                       height=data_height,
                       command=sys_divide)

button_extract = Button(root,
                        text="-",
                        height=data_height,
                        width=data_width,
                        command=sys_extract)

button_quit = Button(root,
                     text="Quit",
                     width=18,
                     height=data_height,
                     command=quit_system)
# endregion

# region Button places
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0)
button_clear.grid(row=5, column=2)
button_sum.grid(row=5, column=0)
button_equal.grid(row=6, column=0, columnspan=3)
button_multiply.grid(row=5, column=1)
button_divide.grid(row=4, column=1)
button_extract.grid(row=4, column=2)
button_quit.grid(row=7, column=0, columnspan=3)
# endregion

root.mainloop()
