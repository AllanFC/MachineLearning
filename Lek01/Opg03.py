from tkinter import *


def isprime(num):
    if num == 2 or num == 3:
        return True
    if num < 2 or num % 2 == 0:
        return False
    if num < 9:
        return True
    if num % 3 == 0:
        return False
    a = int(num ** 0.5)
    b = 5
    while b <= a:
        if num % b == 0:
            return False
        if num % (b + 2) == 0:
            return False
        b = b + 6
    return True


def checkPrime():
    number = txt.get()
    if isprime(int(number)):
        lblNumber.configure(text=number + " is a prime")
    else:
        lblNumber.configure(text=number + " is not a prime")


window = Tk()
window.title("opgave 3")
width = 450
height = 200
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
window.geometry('%dx%d+%d+%d' % (width, height, x, y))

lbl = Label(window, text="Enter a number and click the button", font=("Arial Bold", 25))
lbl.grid(column=1, row=0)
lblNumber = Label(window, text="", font=("Arial Bold", 14))
lblNumber.grid(column=1, row=1)
txt = Entry(window, width=10)
txt.grid(column=1, row=2)
quitBtn = Button(window, text="Submit", command=checkPrime)
quitBtn.grid(column=1, row=3)

window.mainloop()
