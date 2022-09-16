
from tkinter import *
from math import pi


root = Tk()
root.geometry("390x324")
root.resizable(0,0)
root.title("Calculator")

i=0

def btn_click(num):
    global i
    display.insert(i,num)
    i+=1

def bt_clear():
    display.delete(0,END)

def btn_undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        bt_clear()
        display.insert(0,new_string)
    else:
        bt_clear()
        display.insert(0,"error")

def btn_clickoperator(opr):
    global i
    length = len(opr)
    display.insert(i,opr)
    i+=length

def bt_equal():
    entire_string = display.get()
    try:
        result = eval(entire_string)
        bt_clear()
        display.insert(0,result)
    except Exception:
        bt_clear()
        display.insert(0,"error")









display = Frame(root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)

display.pack(side=TOP)


display= Entry(display, font=('arial', 18, 'bold'), textvariable=display, width=50, bg="#eee", bd=0,
                    justify=RIGHT)

display.grid(row=0, column=0)
display.pack(ipady=10)

btns_frame = Frame(root, width=312, height=272.5, bg="grey")

btns_frame.pack()



clear = Button(btns_frame, text="C", fg="black", width=21, height=3, bd=0, bg="#778CF7", cursor="hand2",
               command=lambda: bt_clear()).grid(row=0, column=0,columnspan=2, padx=1, pady=1)

pi = Button(btns_frame, text="pi", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                command=lambda: btn_clickoperator("3.14")).grid(row=0, column=2, padx=1, pady=1)

divide = Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                command=lambda: btn_clickoperator("/")).grid(row=0, column=3, padx=1, pady=1)

undo = Button(btns_frame, text="<-", fg="black", width=10, height=3, bd=0, bg="#778CF7", cursor="hand2",
              command=lambda: btn_undo()).grid(row=0, column=4, padx=0, pady=0)





seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)

eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)

nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)

multiply = Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                  command=lambda: btn_clickoperator("*")).grid(row=1, column=3, padx=1, pady=1)


square = Button(btns_frame, text="**", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                command=lambda: btn_clickoperator("**")).grid(row=1, column=4, padx=1, pady=1)






four = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)

five = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)

six = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)

minus = Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: btn_clickoperator("-")).grid(row=2, column=3, padx=1, pady=1)

point = Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: btn_clickoperator(".")).grid(row=2, column=4, padx=1, pady=1)






one = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)

two = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)

three = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)

plus = Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
              command=lambda: btn_clickoperator("+")).grid(row=3, column=3, padx=1, pady=1)

percentage = Button(btns_frame, text="%", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                command=lambda: btn_clickoperator("%")).grid(row=3, column=4, padx=1, pady=1)




zero = Button(btns_frame, text="0", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(0)).grid(row=4, column=0, padx=1, pady=1)

bracket_open = Button(btns_frame, text="(", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                  command=lambda: btn_clickoperator("(")).grid(row=4, column=1, padx=1, pady=1)

bracket_close = Button(btns_frame, text=")", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: btn_clickoperator(")")).grid(row=4, column=2, padx=1, pady=1)

equals = Button(btns_frame, text="=", fg="black", width=21, height=3, bd=0, bg="#778CF7", cursor="hand2",
                command=lambda: bt_equal()).grid(row=4,column=3,columnspan=2, padx=1, pady=1)

root.mainloop()
