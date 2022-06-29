import tkinter as tk


def clear():
    lbl["text"] = "0"


def negate():
    if ((btn_divide["text"] in lbl["text"]) or (btn_multiply["text"] in lbl["text"]) or ((btn_minus["text"] in lbl["text"]) and (lbl["text"][0] != btn_minus["text"])) or (btn_plus["text"] in lbl["text"])):
        lbl["text"]
    else:
        lbl["text"] = float(lbl["text"]) * -1
        lbl["text"] = str(lbl["text"])


def divide():
    if (lbl["text"][-1] == btn_divide["text"]) or (lbl["text"][-1] == btn_multiply["text"]) or (lbl["text"][-1] == btn_minus["text"]) or (lbl["text"][-1] == btn_plus["text"]):
        lbl["text"]
    else:
        lbl["text"] += btn_divide["text"]


def multiply():
    if (lbl["text"][-1] == btn_divide["text"]) or (lbl["text"][-1] == btn_multiply["text"]) or (lbl["text"][-1] == btn_minus["text"]) or (lbl["text"][-1] == btn_plus["text"]):
        lbl["text"]
    else:
        lbl["text"] += btn_multiply["text"]


def minus():
    if (lbl["text"][-1] == btn_divide["text"]) or (lbl["text"][-1] == btn_multiply["text"]) or (lbl["text"][-1] == btn_minus["text"]) or (lbl["text"][-1] == btn_plus["text"]):
        lbl["text"]
    else:
        lbl["text"] += btn_minus["text"]


def plus():
    if (lbl["text"][-1] == btn_divide["text"]) or (lbl["text"][-1] == btn_multiply["text"]) or (lbl["text"][-1] == btn_minus["text"]) or (lbl["text"][-1] == btn_plus["text"]):
        lbl["text"]
    else:
        lbl["text"] += btn_plus["text"]


def decimal():
    if btn_decimal["text"] in lbl["text"]:
        lbl["text"]
    else:
        lbl["text"] += btn_decimal["text"]


def equal():
    if (lbl["text"][-1] == btn_divide["text"]) or (lbl["text"][-1] == btn_multiply["text"]) or (lbl["text"][-1] == btn_minus["text"]) or (lbl["text"][-1] == btn_plus["text"]) or (lbl["text"][-1] == btn_decimal["text"]):
        lbl["text"]
    else:
        total = str(eval(lbl["text"]))
        lbl["text"] = total


def zero():
    value = btn_zero["text"]
    if lbl["text"] == btn_zero["text"]:
        lbl["text"] = value
    else:
        lbl["text"] += value


def one():
    value = btn_one["text"]
    if lbl["text"] == btn_zero["text"]:
        lbl["text"] = value
    else:
        lbl["text"] += value


def two():
    value = btn_two["text"]
    if lbl["text"] == btn_zero["text"]:
        lbl["text"] = value
    else:
        lbl["text"] += value


def three():
    value = btn_three["text"]
    if lbl["text"] == btn_zero["text"]:
        lbl["text"] = value
    else:
        lbl["text"] += value


def four():
    value = btn_four["text"]
    if lbl["text"] == btn_zero["text"]:
        lbl["text"] = value
    else:
        lbl["text"] += value


def five():
    value = btn_five["text"]
    if lbl["text"] == btn_zero["text"]:
        lbl["text"] = value
    else:
        lbl["text"] += value


def six():
    value = btn_six["text"]
    if lbl["text"] == btn_zero["text"]:
        lbl["text"] = value
    else:
        lbl["text"] += value


def seven():
    value = btn_seven["text"]
    if lbl["text"] == btn_zero["text"]:
        lbl["text"] = value
    else:
        lbl["text"] += value


def eight():
    value = btn_eight["text"]
    if lbl["text"] == btn_zero["text"]:
        lbl["text"] = value
    else:
        lbl["text"] += value


def nine():
    value = btn_nine["text"]
    if lbl["text"] == btn_zero["text"]:
        lbl["text"] = value
    else:
        lbl["text"] += value


window = tk.Tk()
window.title("Calculator")
window.resizable(width=False, height=False)

# Separate display of value and calculate of value
frm1 = tk.Frame()
frm2 = tk.Frame()
frm1.grid(row=0, column=0)
frm2.grid(row=1, column=0)

# Current value
lbl = tk.Label(master=frm1, text="0", width=25,
               height=5, fg="#000000", bg="#FFFFFF", relief=tk.FLAT, font="Arial, 24")
lbl.grid(row=0, column=0, sticky="E")

# Row 0
btn_clear = tk.Button(master=frm2, text="C", width=5,
                      height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=clear)
btn_negate = tk.Button(master=frm2, text="+/-", width=5,
                       height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=negate)
btn_divide = tk.Button(master=frm2, text="/", width=5,
                       height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=divide)
btn_multiply = tk.Button(master=frm2, text="*", width=5,
                         height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=multiply)

btn_clear.grid(padx=5, pady=5, row=0, column=0)
btn_negate.grid(padx=5, pady=5, row=0, column=1)
btn_divide.grid(padx=5, pady=5, row=0, column=2)
btn_multiply.grid(padx=5, pady=5, row=0, column=3)

# Row 1
btn_seven = tk.Button(master=frm2, text="7", width=5,
                      height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=seven)
btn_eight = tk.Button(master=frm2, text="8", width=5,
                      height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=eight)
btn_nine = tk.Button(master=frm2, text="9", width=5,
                     height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=nine)
btn_minus = tk.Button(master=frm2, text="-", width=5,
                      height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=minus)

btn_seven.grid(padx=5, pady=5, row=1, column=0)
btn_eight.grid(padx=5, pady=5, row=1, column=1)
btn_nine.grid(padx=5, pady=5, row=1, column=2)
btn_minus.grid(padx=5, pady=5, row=1, column=3)

# Row 2
btn_four = tk.Button(master=frm2, text="4", width=5,
                     height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=four)
btn_five = tk.Button(master=frm2, text="5", width=5,
                     height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=five)
btn_six = tk.Button(master=frm2, text="6", width=5,
                    height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=six)
btn_plus = tk.Button(master=frm2, text="+", width=5,
                     height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=plus)

btn_four.grid(padx=5, pady=5, row=2, column=0)
btn_five.grid(padx=5, pady=5, row=2, column=1)
btn_six.grid(padx=5, pady=5, row=2, column=2)
btn_plus.grid(padx=5, pady=5, row=2, column=3)

# Row 3
btn_one = tk.Button(master=frm2, text="1", width=5,
                    height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=one)
btn_two = tk.Button(master=frm2, text="2", width=5,
                    height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=two)
btn_three = tk.Button(master=frm2, text="3", width=5,
                      height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=three)

btn_one.grid(padx=5, pady=5, row=3, column=0)
btn_two.grid(padx=5, pady=5, row=3, column=1)
btn_three.grid(padx=5, pady=5, row=3, column=2)

# Others
btn_equal = tk.Button(master=frm2, text="=", width=5,
                      height=5, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=equal)
btn_zero = tk.Button(master=frm2, text="0", width=11,
                     height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=zero)
btn_decimal = tk.Button(master=frm2, text=".", width=5,
                    height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=decimal)

btn_equal.grid(padx=5, pady=5, row=3, rowspan=4, column=3)
btn_zero.grid(padx=5, pady=5, row=4, column=0, columnspan=2)
btn_decimal.grid(padx=5, pady=5, row=4, column=2)

window.mainloop()
