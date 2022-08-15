import tkinter as tk


def one():
    if lbl_bin["text"] == "0":
        lbl_bin["text"] = "1"
    elif len(lbl_bin["text"]) == 8:
        lbl_bin["text"]
    elif lbl_bin["text"][-1] == "1" or lbl_bin["text"][-1] == "0":
        lbl_bin["text"] += "1"


def zero():
    if lbl_bin["text"] == "0":
        lbl_bin["text"]
    elif len(lbl_bin["text"]) == 8:
        lbl_bin["text"]
    elif lbl_bin["text"][-1] == "1" or lbl_bin["text"][-1] == "0":
        lbl_bin["text"] += "0"


def enter():
    value = 0
    count = len(lbl_bin["text"]) - 1
    for i in range(0, len(lbl_bin["text"]) - 1):
        if lbl_bin["text"][i] == "1":
            value += 2 ** count
        elif lbl_bin["text"][i] == "0":
            value
        count -= 1
    lbl_dec["text"] = str(value)


def reset():
    lbl_bin["text"] = "0"


def backspace():
    lis = list(lbl_bin["text"])
    lis.pop(-1)
    lis = ''.join(lis)
    lbl_bin["text"] = lis


window = tk.Tk()
window.title("Binary To Decimal")
window.resizable(width=False, height=True)

frm_view = tk.Frame(master=window)
frm_keying = tk.Frame(master=window)

frm_view.grid(row=0, column=0)
frm_keying.grid(row=1, column=0)


lbl_bin = tk.Label(master=frm_view, text="0", width=16, height=2,
                   fg="#000000", bg="#FFFFFF", relief=tk.FLAT, font="Arial, 14")
lbl_dec = tk.Label(master=frm_view, text="0", width=16, height=2,
                   fg="#000000", bg="#FFFFFF", relief=tk.FLAT, font="Arial, 14")

lbl_bin.grid(padx=3, pady=3, row=0, column=0)
lbl_dec.grid(padx=3, pady=3, row=0, column=2)

btn_one = tk.Button(master=frm_keying, text="1", width=5, height=1,
                    fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 14", command=one)
btn_zero = tk.Button(master=frm_keying, text="0", width=5, height=1,
                     fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 14", command=zero)
btn_enter = tk.Button(master=frm_keying, text="Enter", width=5, height=1,
                      fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 14", command=enter)
btn_reset = tk.Button(master=frm_keying, text="Reset", width=5, height=1,
                      fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 14", command=reset)
btn_backspace = tk.Button(master=frm_keying, text="\u232b", width=5, height=1,
                          fg="#000000", bg="#FFFFFF", relief=tk.RAISED, font="Arial, 14", command=backspace)

btn_one.grid(padx=3, pady=3, row=0, column=0)
btn_zero.grid(padx=3, pady=3, row=0, column=1)
btn_enter.grid(padx=3, pady=3, row=0, column=2)
btn_reset.grid(padx=3, pady=3, row=0, column=3)
btn_backspace.grid(padx=3, pady=3, row=0, column=4)

window.mainloop()
