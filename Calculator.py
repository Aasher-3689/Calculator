#developed_by_Aasher

from tkinter import *

#-------Functions----------
def show(button_value):
    global equation_text
    equation_text += str(button_value)
    equation_label.set(equation_text)

def clear():
    global equation_text
    equation_text = ''
    equation_label.set(equation_text)

def backspace():
    global equation_text
    equation_text = equation_text[:-1]
    equation_label.set(equation_text)

def update_label():
    global equation_text
    equation_text = equation_label.get()
    try:
        total = str(eval(equation_text))
        total = round((float(total)), 4)
        total = str(total)
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set('ZeroDivisionError')
    except SyntaxError:
        equation_label.set('SyntaxError')
    except ValueError:
        equation_label.set('ValueError')

#-------Window-------------

window = Tk()

window.geometry("500x670")
window.config(bg="#333333")
window.title("Calculator-Aasher")
window.resizable(False, False)

#--------------------------
equation_text = ''
equation_label = StringVar()

label = Label(window, width=16, height=2, textvariable=equation_label,
              font=("Comic Sans", 30), anchor="e",
              bg="#333333", fg="#F8F6F0",
              relief="solid", bd=0,
              highlightbackground="#7c7c7d", highlightcolor="#7c7c7d",
              highlightthickness=1)
label.place(x=17, y=18)
#--------------------------
button_ac = Button(window, text="AC", font=("Roboto", 22), width=8,
                 bg="#8c84e0", fg="#333333",
                 activeforeground="#8c84e0", activebackground="#333333",
                 borderwidth=0, highlightthickness=1, highlightcolor="#8c84e0",
                 highlightbackground="#8c84e0", command=lambda:clear())
button_ac.place(x=17, y=180)
#--------------------------
button_back = Button(window, text="←", font=("Roboto", 37, "bold"),
                 bg="#333333", fg="#8c84e0",
                 activeforeground="#b8333c", activebackground="#333333",
                 borderwidth=0, highlightthickness=0, command=lambda:backspace())
button_back.place(x=260 ,y=167)
#--------------------------
button_div = Button(window, text="÷", font=("Roboto", 37),
                 bg="#333333", fg="#8c84e0",
                 activeforeground="#b8333c", activebackground="#333333",
                 borderwidth=0, highlightthickness=0,
                 command=lambda:show('/'))
button_div.place(x=400 ,y=167)
#--------------------------
button_mult = Button(window, text="×", font=("Roboto", 37),
                 bg="#333333", fg="#8c84e0",
                 activeforeground="#b8333c", activebackground="#333333",
                 borderwidth=0, highlightthickness=0,
                 command=lambda:show('*'))
button_mult.place(x=400 ,y=250)
#--------------------------
button_subs = Button(window, text="—", font=("Roboto", 20, "bold"),
                 bg="#333333", fg="#8c84e0",
                 activeforeground="#b8333c", activebackground="#333333",
                 borderwidth=0, highlightthickness=0,
                 command=lambda:show('-'))
button_subs.place(x=400 ,y=367)
#--------------------------
button_add = Button(window, text="+", font=("Roboto", 37),
                 bg="#333333", fg="#8c84e0",
                 activeforeground="#b8333c", activebackground="#333333",
                 borderwidth=0, highlightthickness=0,
                 command=lambda:show('+'))
button_add.place(x=400 ,y=460)
#--------------------------
button_equal = Button(window, text="=", font=("Roboto", 30, "bold"),
                 bg="#8c84e0", fg="#333333",
                 activeforeground="#8c84e0", activebackground="#333333",
                 padx=55,
                 borderwidth=0, highlightthickness=1, highlightcolor="#8c84e0",
                 highlightbackground="#8c84e0", command=lambda:update_label())
button_equal.place(x=330 ,y=565)

#--------------------------
button_perc = Button(window, text="%", font=("Cambria", 28),
                 bg="#333333", fg="#F8F6F0",
                 activeforeground="#c9be42", activebackground="#333333",
                 borderwidth=0, highlightthickness=0,
                 command=lambda:show('%'))
button_perc.place(x=30, y=578)

#--------------------------
button_0 = Button(window, text="0", font=("Arial", 30, "bold"),
                 bg="#333333", fg="#F8F6F0",
                 activeforeground="#c9be42", activebackground="#333333",
                 borderwidth=0, highlightthickness=0,
                 command=lambda:show(0))
button_0.place(x=149, y=578)

#--------------------------
button_dot = Button(window, text="·", font=("Cambria", 30, "bold"),
                 bg="#333333", fg="#F8F6F0",
                 activeforeground="#c9be42", activebackground="#333333",
                 borderwidth=0, highlightthickness=0,
                 command=lambda:show('.'))
button_dot.place(x=270, y=578)

#--------------------------
button_1 = Button(window, text="1", font=("Cambria", 30, "bold"),
                 bg="#333333", fg="#F8F6F0",
                 activeforeground="#c9be42", activebackground="#333333",
                 borderwidth=0, highlightthickness=0,
                 command=lambda:show(1))
button_1.place(x=30, y=473)

#--------------------------
button_2 = Button(window, text="2", font=("Cambria", 30, "bold"),
                 bg="#333333", fg="#F8F6F0",
                 activeforeground="#c9be42", activebackground="#333333",
                 borderwidth=0, highlightthickness=0,
                 command=lambda:show(2))
button_2.place(x=149, y=473)

#--------------------------
button_3 = Button(window, text="3", font=("Cambria", 30, "bold"),
                 bg="#333333", fg="#F8F6F0",
                 activeforeground="#c9be42", activebackground="#333333",
                 borderwidth=0, highlightthickness=0,
                 command=lambda:show(3))
button_3.place(x=270, y=473)

#--------------------------
button_4 = Button(window, text="4", font=("Cambria", 30, "bold"),
                 bg="#333333", fg="#F8F6F0",
                 activeforeground="#c9be42", activebackground="#333333",
                 borderwidth=0, highlightthickness=0,
                 command=lambda:show(4))
button_4.place(x=30, y=360)

#--------------------------
button_5 = Button(window, text="5", font=("Cambria", 30, "bold"),
                 bg="#333333", fg="#F8F6F0",
                 activeforeground="#c9be42", activebackground="#333333",
                 borderwidth=0, highlightthickness=0,
                 command=lambda:show(5))
button_5.place(x=149, y=360)

#--------------------------
button_6 = Button(window, text="6", font=("Cambria", 30, "bold"),
                 bg="#333333", fg="#F8F6F0",
                 activeforeground="#c9be42", activebackground="#333333",
                 borderwidth=0, highlightthickness=0,
                 command=lambda:show(6))
button_6.place(x=270, y=360)

#--------------------------
button_7 = Button(window, text="7", font=("Cambria", 30, "bold"),
                 bg="#333333", fg="#F8F6F0",
                 activeforeground="#c9be42", activebackground="#333333",
                 borderwidth=0, highlightthickness=0,
                 command=lambda:show(7))
button_7.place(x=30, y=250)

#--------------------------
button_8 = Button(window, text="8", font=("Cambria", 30, "bold"),
                 bg="#333333", fg="#F8F6F0",
                 activeforeground="#c9be42", activebackground="#333333",
                 borderwidth=0, highlightthickness=0,
                 command=lambda:show(8))
button_8.place(x=149, y=250)

#--------------------------
button_9 = Button(window, text="9", font=("Cambria", 30, "bold"),
                 bg="#333333", fg="#F8F6F0",
                 activeforeground="#c9be42", activebackground="#333333",
                 borderwidth=0, highlightthickness=0,
                 command=lambda:show(9))
button_9.place(x=270, y=250)

#--------------------------
window.mainloop()

