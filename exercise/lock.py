import tkinter as tk


def one():
    # Digit 1
    if len(lbl_passw["text"]) == 3:
        lbl_passw["text"]
    else:
        lbl_passw["text"] += btn_one["text"]


def two():
    # Digit 2
    if len(lbl_passw["text"]) == 3:
        lbl_passw["text"]
    else:
        lbl_passw["text"] += btn_two["text"]


def three():
    # Digit 3
    if len(lbl_passw["text"]) == 3:
        lbl_passw["text"]
    else:
        lbl_passw["text"] += btn_three["text"]


def four():
    # Digit 4
    if len(lbl_passw["text"]) == 3:
        lbl_passw["text"]
    else:
        lbl_passw["text"] += btn_four["text"]


def five():
    # Digit 5
    if len(lbl_passw["text"]) == 3:
        lbl_passw["text"]
    else:
        lbl_passw["text"] += btn_five["text"]


def six():
    # Digit 6
    if len(lbl_passw["text"]) == 3:
        lbl_passw["text"]
    else:
        lbl_passw["text"] += btn_six["text"]


def seven():
    # Digit 7
    if len(lbl_passw["text"]) == 3:
        lbl_passw["text"]
    else:
        lbl_passw["text"] += btn_seven["text"]


def eight():
    # Digit 8
    if len(lbl_passw["text"]) == 3:
        lbl_passw["text"]
    else:
        lbl_passw["text"] += btn_eight["text"]


def nine():
    # Digit 9
    if len(lbl_passw["text"]) == 3:
        lbl_passw["text"]
    else:
        lbl_passw["text"] += btn_nine["text"]


def zero():
    # Digit 0
    if len(lbl_passw["text"]) == 3:
        lbl_passw["text"]
    else:
        lbl_passw["text"] += btn_zero["text"]


def reset():
    # Reset
    lbl_passw["text"] = ""


def btn1_incre():
    # Increase by 1 for 1st digit
    if int(lbl1_value["text"]) >= 0 and int(lbl1_value["text"]) < 9:
        lbl1_value["text"] = int(lbl1_value["text"]) + 1


def btn2_incre():
    # Increase by 1 for 2nd digit
    if int(lbl2_value["text"]) >= 0 and int(lbl2_value["text"]) < 9:
        lbl2_value["text"] = int(lbl2_value["text"]) + 1


def btn3_incre():
    # Increase by 1 for 3rd digit
    if int(lbl3_value["text"]) >= 0 and int(lbl3_value["text"]) < 9:
        lbl3_value["text"] = int(lbl3_value["text"]) + 1


def btn1_decre():
    # Decrease by 1 for 1st digit
    if int(lbl1_value["text"]) > 0 and int(lbl1_value["text"]) <= 9:
        lbl1_value["text"] = int(lbl1_value["text"]) - 1


def btn2_decre():
    # Decrease by 1 for 2nd digit
    if int(lbl2_value["text"]) > 0 and int(lbl2_value["text"]) <= 9:
        lbl2_value["text"] = int(lbl2_value["text"]) - 1


def btn3_decre():
    # Decrease by 1 for 3rd digit
    if int(lbl3_value["text"]) > 0 and int(lbl3_value["text"]) <= 9:
        lbl3_value["text"] = int(lbl3_value["text"]) - 1


def enter():
    # Unlock step
    if int(lbl_passw["text"]) == int(str(lbl1_value["text"]) + str(lbl2_value["text"]) + str(lbl3_value["text"])):
        print("Unlocked!!!")
    else:
        print("Locked!!!")


window = tk.Tk()
window.title("Smart Lock")
window.resizable(width=False, height=False)

# Numpad inputs + lock check
frm_numpad = tk.Frame(master=window)
frm_lock = tk.Frame(master=window)

frm_numpad.grid(row=0, column=0)
frm_lock.grid(row=0, column=1)


# Frame 1 - Numpad
lbl_passw = tk.Label(master=frm_numpad, text="", width=12,
                     height=1, fg="#000000", bg="#FFFFFF", relief=tk.FLAT, font="Arial, 14")
btn_one = tk.Button(master=frm_numpad, text="1", width=3,
                    height=1, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 14", command=one)
btn_two = tk.Button(master=frm_numpad, text="2", width=3,
                    height=1, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 14", command=two)
btn_three = tk.Button(master=frm_numpad, text="3", width=3,
                      height=1, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 14", command=three)
btn_four = tk.Button(master=frm_numpad, text="4", width=3,
                     height=1, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 14", command=four)
btn_five = tk.Button(master=frm_numpad, text="5", width=3,
                     height=1, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 14", command=five)
btn_six = tk.Button(master=frm_numpad, text="6", width=3,
                    height=1, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 14", command=six)
btn_seven = tk.Button(master=frm_numpad, text="7", width=3,
                      height=1, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 14", command=seven)
btn_eight = tk.Button(master=frm_numpad, text="8", width=3,
                      height=1, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 14", command=eight)
btn_nine = tk.Button(master=frm_numpad, text="9", width=3,
                     height=1, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 14", command=nine)
btn_zero = tk.Button(master=frm_numpad, text="0", width=12,
                     height=1, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 14", command=zero)
btn_reset = tk.Button(master=frm_numpad, text="Reset", width=5,
                      height=3, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 14", command=reset)

lbl_passw.grid(padx=3, pady=3, row=0, column=0, columnspan=3)
btn_one.grid(padx=3, pady=3, row=1, column=0)
btn_two.grid(padx=3, pady=3, row=1, column=1)
btn_three.grid(padx=3, pady=3, row=1, column=2)
btn_four.grid(padx=3, pady=3, row=2, column=0)
btn_five.grid(padx=3, pady=3, row=2, column=1)
btn_six.grid(padx=3, pady=3, row=2, column=2)
btn_seven.grid(padx=3, pady=3, row=3, column=0)
btn_eight.grid(padx=3, pady=3, row=3, column=1)
btn_nine.grid(padx=3, pady=3, row=3, column=2)
btn_reset.grid(padx=3, pady=3, row=3, column=3, rowspan=2)
btn_zero.grid(padx=3, pady=3, row=4, column=0, columnspan=3)


# Frame 2 - Lock
btn1_up = tk.Button(master=frm_lock, text="\N{UPWARDS BLACK ARROW}", width=5,
                    height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 14", command=btn1_incre)
btn2_up = tk.Button(master=frm_lock, text="\N{UPWARDS BLACK ARROW}", width=5,
                    height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 14", command=btn2_incre)
btn3_up = tk.Button(master=frm_lock, text="\N{UPWARDS BLACK ARROW}", width=5,
                    height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 14", command=btn3_incre)
lbl1_value = tk.Label(master=frm_lock, text="0", width=5,
                      height=2, fg="#000000", bg="#FFFFFF", relief=tk.FLAT, font="Arial, 14")
lbl2_value = tk.Label(master=frm_lock, text="0", width=5,
                      height=2, fg="#000000", bg="#FFFFFF", relief=tk.FLAT, font="Arial, 14")
lbl3_value = tk.Label(master=frm_lock, text="0", width=5,
                      height=2, fg="#000000", bg="#FFFFFF", relief=tk.FLAT, font="Arial, 14")
btn1_down = tk.Button(master=frm_lock, text="\N{DOWNWARDS BLACK ARROW}", width=5,
                      height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 14", command=btn1_decre)
btn2_down = tk.Button(master=frm_lock, text="\N{DOWNWARDS BLACK ARROW}", width=5,
                      height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 14", command=btn2_decre)
btn3_down = tk.Button(master=frm_lock, text="\N{DOWNWARDS BLACK ARROW}", width=5,
                      height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 14", command=btn3_decre)
btn_enter = tk.Button(master=frm_lock, text="ENTER", width=17,
                      height=2, fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 14", command=enter)

btn1_up.grid(padx=3, pady=3, row=0, column=0)
btn2_up.grid(padx=3, pady=3, row=0, column=1)
btn3_up.grid(padx=3, pady=3, row=0, column=2)
lbl1_value.grid(padx=3, pady=3, row=1, column=0)
lbl2_value.grid(padx=3, pady=3, row=1, column=1)
lbl3_value.grid(padx=3, pady=3, row=1, column=2)
btn1_down.grid(padx=3, pady=3, row=2, column=0)
btn2_down.grid(padx=3, pady=3, row=2, column=1)
btn3_down.grid(padx=3, pady=3, row=2, column=2)
btn_enter.grid(padx=3, pady=3, row=3, column=0, columnspan=3)

window.mainloop()
