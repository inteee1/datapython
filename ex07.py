from tkinter import *
window = Tk()
window.title("고양이")
photo = PhotoImage(file='cat2.gif')
label1 = Label(window, image = photo)
label1.pack()
window.mainloop()