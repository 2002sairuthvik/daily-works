from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)
def button_clicked():
    print("I got clicked")
    # my_label.config(text="button clicked")
    entry_txt = input.get()
    my_label.config(text=entry_txt)
    
#label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row= 0)

#button

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)
new_button = Button(text="New button")
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
input.grid(column=3, row=2)










window.mainloop()