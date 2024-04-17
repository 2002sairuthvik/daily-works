from tkinter import *

def miles_km():
    miles= float(miles_input.get())
    km = miles * 1.689
    kilometer_result.config(text=f"{km}")

window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_eq_label = Label(text="is equal to")
is_eq_label.grid(column=0, row=1)

kilometer_result = Label(text=0)
kilometer_result.grid(column=1, row=1)

kilometer_label = Label(text="km")
kilometer_label.grid(column=2,row=1)

cal_button = Button(text="Calculate", command=miles_km)
cal_button.grid(column=1, row=2)










window.mainloop()