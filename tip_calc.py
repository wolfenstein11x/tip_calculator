# this won't work on linux

import tkinter as tk

def calc_tip():
    tip = float(ent_tip.get())
    bill = float(ent_bill.get())
    tip_result = bill * (tip / 100)
    total = bill + tip_result
    lbl_tip_result["text"] = f"${round(tip_result, 2)}"
    lbl_total_result["text"] = f"${round(total, 2)}"
    

window = tk.Tk()
window.title("Tip Quackulator")

frm_1 = tk.Frame(master=window, width=100, height=100, borderwidth=1)
ent_bill = tk.Entry(master=frm_1, width=10)
lbl_bill = tk.Label(master=frm_1, text="Bill:")

frm_2 = tk.Frame(master=window, width=100, height=100, borderwidth=1)
ent_tip = tk.Entry(master=frm_2, width=10)
lbl_tip = tk.Label(master=frm_2, text="Tip(%):")

frm_3 = tk.Frame(master=window, width=100, height=100, borderwidth=1)
btn_calc = tk.Button(master=frm_3, text="Quackulate", command = calc_tip)

frm_4 = tk.Frame(master=window, width=100, height=100, borderwidth=1)
lbl_tip_label = tk.Label(master=frm_4, text="Tip:", fg="blue")
lbl_tip_result = tk.Label(master=frm_4, text="$0.00", fg="blue")
lbl_total_label = tk.Label(master=frm_4, text="Total:", fg="blue")
lbl_total_result = tk.Label(master=frm_4, text="$0.00", fg="blue")

frm_1.grid(row=0, column=0, padx=5, pady=5)
ent_bill.grid(row=0, column=1)
lbl_bill.grid(row=0, column=0)

frm_2.grid(row=1, column=0, padx=5, pady=5)
ent_tip.grid(row=0, column=1)
lbl_tip.grid(row=0, column=0)

frm_3.grid(row=2, column=0, padx=5, pady=5)
btn_calc.pack()

frm_4.grid(row=3, column=0, padx=5, pady=5)
lbl_tip_label.grid(row=0, column=0)
lbl_tip_result.grid(row=0, column=1)
lbl_total_label.grid(row=1, column=0)
lbl_total_result.grid(row=1, column=1)

window.mainloop()
