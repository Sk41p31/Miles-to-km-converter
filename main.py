import tkinter as tk
FONT = ("Arial", 16,)


def calc_km():
    new_text = 1.609 * float(miles_entry.get())
    new_text = round(new_text, 3)
    km_label.config(text=new_text)


window = tk.Tk()
window.title("Miles to kilometers")
window.config(padx=60, pady=30)

tk.Label(text="is equal to", font=FONT).grid(column=0, row=1)
tk.Label(text="Miles", font=FONT).grid(column=2, row=0)
tk.Label(text="Km", font=FONT).grid(column=2, row=1)

km_label = tk.Label(text="0", font=FONT)
km_label.grid(column=1, row=1)

miles_entry = tk.Entry(width=10,font=FONT)
miles_entry.grid(column=1, row=0)

calc_button = tk.Button(text="Calculate", font=FONT, command=calc_km)
calc_button.grid(column=1, row=2)

window.mainloop()
