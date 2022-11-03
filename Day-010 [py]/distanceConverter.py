
## 2/11/2022

import tkinter

window = tkinter.Tk()
window.title("Miles to Kilometer")
window.minsize(height=20, width=200)
window.config(padx=20, pady=20)


def convert():
    miles = userInput.get()
    if miles:
        km = float(miles)*1.609
        kilometerOutputLabel.config(text=km)
    else:
        kilometerOutputLabel.config(text='"Enter a number"')


userInput = tkinter.Entry(width=20)
userInput.grid(column=1, row=0)

milesLabel = tkinter.Label(text='Miles')
milesLabel.grid(column=2, row=0)

kilometerOutputLabel = tkinter.Label(text="0")
kilometerOutputLabel.grid(column=1, row=2)
kilometerOutputLabel.config(padx=20, pady=20)

kilometerLabel = tkinter.Label(text='Kilometers')
kilometerLabel.grid(column=2, row=2)

button = tkinter.Button(text='convert', command=convert)
button.grid(column=2, row=3)

window.mainloop()
