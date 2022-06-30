import tkinter as tk
from turtle import window_height

# Buttons' command
def clear():
    # Reset
    lbl["text"] = "0"


def negate():
    # Negation
    if ((btn_divide["text"] in lbl["text"]) or (btn_multiply["text"] in lbl["text"]) or ((btn_minus["text"] in lbl["text"]) and (lbl["text"][0] != btn_minus["text"])) or (btn_plus["text"] in lbl["text"])):
        lbl["text"]
    else:
        lbl["text"] = float(lbl["text"]) * -1
        lbl["text"] = str(lbl["text"])


def divide():
    # Division
    if (lbl["text"][-1] == btn_divide["text"]) or (lbl["text"][-1] == btn_multiply["text"]) or (lbl["text"][-1] == btn_minus["text"]) or (lbl["text"][-1] == btn_plus["text"]):
        lbl["text"]
    else:
        lbl["text"] += btn_divide["text"]


def multiply():
    # Multiplication
    if (lbl["text"][-1] == btn_divide["text"]) or (lbl["text"][-1] == btn_multiply["text"]) or (lbl["text"][-1] == btn_minus["text"]) or (lbl["text"][-1] == btn_plus["text"]):
        lbl["text"]
    else:
        lbl["text"] += btn_multiply["text"]


def minus():
    # Subtraction
    if (lbl["text"][-1] == btn_divide["text"]) or (lbl["text"][-1] == btn_multiply["text"]) or (lbl["text"][-1] == btn_minus["text"]) or (lbl["text"][-1] == btn_plus["text"]):
        lbl["text"]
    else:
        lbl["text"] += btn_minus["text"]


def plus():
    # Addition
    if (lbl["text"][-1] == btn_divide["text"]) or (lbl["text"][-1] == btn_multiply["text"]) or (lbl["text"][-1] == btn_minus["text"]) or (lbl["text"][-1] == btn_plus["text"]):
        lbl["text"]
    else:
        lbl["text"] += btn_plus["text"]


def decimal():
    # Decimal point
    if btn_decimal["text"] in lbl["text"]:
        lbl["text"]
    else:
        lbl["text"] += btn_decimal["text"]


def equal():
    # Equal sign
    if (lbl["text"][-1] == btn_divide["text"]) or (lbl["text"][-1] == btn_multiply["text"]) or (lbl["text"][-1] == btn_minus["text"]) or (lbl["text"][-1] == btn_plus["text"]) or (lbl["text"][-1] == btn_decimal["text"]):
        lbl["text"]
    else:
        total = str(eval(lbl["text"]))
        lbl["text"] = total


def zero():
    # Digit 0
    if lbl["text"] == btn_zero["text"]:
        lbl["text"] = btn_zero["text"]
    elif lbl["text"][-1] == btn_divide["text"]:
        lbl["text"]
    else:
        lbl["text"] += btn_zero["text"]


def one():
    # Digit 1
    if lbl["text"] == btn_zero["text"]:
        lbl["text"] = btn_one["text"]
    else:
        lbl["text"] += btn_one["text"]


def two():
    # Digit 2
    if lbl["text"] == btn_zero["text"]:
        lbl["text"] = btn_two["text"]
    else:
        lbl["text"] += btn_two["text"]


def three():
    # Digit 3
    if lbl["text"] == btn_zero["text"]:
        lbl["text"] = btn_three["text"]
    else:
        lbl["text"] += btn_three["text"]


def four():
    # Digit 4
    if lbl["text"] == btn_zero["text"]:
        lbl["text"] = btn_four["text"]
    else:
        lbl["text"] += btn_four["text"]


def five():
    # Digit 5
    if lbl["text"] == btn_zero["text"]:
        lbl["text"] = btn_five["text"]
    else:
        lbl["text"] += btn_five["text"]


def six():
    # Digit 6
    if lbl["text"] == btn_zero["text"]:
        lbl["text"] = btn_six["text"]
    else:
        lbl["text"] += btn_six["text"]


def seven():
    # Digit 7
    if lbl["text"] == btn_zero["text"]:
        lbl["text"] = btn_seven["text"]
    else:
        lbl["text"] += btn_seven["text"]


def eight():
    # Digit 8
    if lbl["text"] == btn_zero["text"]:
        lbl["text"] = btn_eight["text"]
    else:
        lbl["text"] += btn_eight["text"]


def nine():
    # Digit 9
    if lbl["text"] == btn_zero["text"]:
        lbl["text"] = btn_nine["text"]
    else:
        lbl["text"] += btn_nine["text"]


window = tk.Tk()
window.title("Simple Calculator")
window.resizable(width=False, height=False)


# Output screen + Input buttons
frm_output = tk.Frame(master=window)
frm_input = tk.Frame(master=window)
frm_output.grid(row=0, column=0)
frm_input.grid(row=1, column=0)


# Frame 1 - Output screen
lbl = tk.Label(master=frm_output, text="0", width=25,
               height=5, fg="#000000", bg="#FFFFFF", relief=tk.FLAT, font="Arial, 24")

lbl.grid(row=0, column=0, sticky="E")


# Frame 2 - Input buttons
# Row 0
btn_clear = tk.Button(master=frm_input, text="C", width=5,
                      height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=clear)
btn_negate = tk.Button(master=frm_input, text="+/-", width=5,
                       height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=negate)
btn_divide = tk.Button(master=frm_input, text="/", width=5,
                       height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=divide)
btn_multiply = tk.Button(master=frm_input, text="*", width=5,
                         height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=multiply)

btn_clear.grid(padx=5, pady=5, row=0, column=0)
btn_negate.grid(padx=5, pady=5, row=0, column=1)
btn_divide.grid(padx=5, pady=5, row=0, column=2)
btn_multiply.grid(padx=5, pady=5, row=0, column=3)


# Row 1
btn_seven = tk.Button(master=frm_input, text="7", width=5,
                      height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=seven)
btn_eight = tk.Button(master=frm_input, text="8", width=5,
                      height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=eight)
btn_nine = tk.Button(master=frm_input, text="9", width=5,
                     height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=nine)
btn_minus = tk.Button(master=frm_input, text="-", width=5,
                      height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=minus)

btn_seven.grid(padx=5, pady=5, row=1, column=0)
btn_eight.grid(padx=5, pady=5, row=1, column=1)
btn_nine.grid(padx=5, pady=5, row=1, column=2)
btn_minus.grid(padx=5, pady=5, row=1, column=3)


# Row 2
btn_four = tk.Button(master=frm_input, text="4", width=5,
                     height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=four)
btn_five = tk.Button(master=frm_input, text="5", width=5,
                     height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=five)
btn_six = tk.Button(master=frm_input, text="6", width=5,
                    height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=six)
btn_plus = tk.Button(master=frm_input, text="+", width=5,
                     height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=plus)

btn_four.grid(padx=5, pady=5, row=2, column=0)
btn_five.grid(padx=5, pady=5, row=2, column=1)
btn_six.grid(padx=5, pady=5, row=2, column=2)
btn_plus.grid(padx=5, pady=5, row=2, column=3)


# Row 3
btn_one = tk.Button(master=frm_input, text="1", width=5,
                    height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=one)
btn_two = tk.Button(master=frm_input, text="2", width=5,
                    height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=two)
btn_three = tk.Button(master=frm_input, text="3", width=5,
                      height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=three)
btn_equal = tk.Button(master=frm_input, text="=", width=5,
                      height=5, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=equal)

btn_one.grid(padx=5, pady=5, row=3, column=0)
btn_two.grid(padx=5, pady=5, row=3, column=1)
btn_three.grid(padx=5, pady=5, row=3, column=2)
btn_equal.grid(padx=5, pady=5, row=3, rowspan=4, column=3)

# Row 4
btn_zero = tk.Button(master=frm_input, text="0", width=11,
                     height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=zero)
btn_decimal = tk.Button(master=frm_input, text=".", width=5,
                        height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 24", command=decimal)

btn_zero.grid(padx=5, pady=5, row=4, column=0, columnspan=2)
btn_decimal.grid(padx=5, pady=5, row=4, column=2)

window.mainloop()
