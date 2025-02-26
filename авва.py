from tkinter import *
import webbrowser
def click_btn():
    text = ent.get()
    webbrowser.open(text)


window = Tk()
window.geometry('600x600')
window.configure(background="#735184")
btn = Button(window, text="Беляш", command=click_btn)
btn.place(x=300, y=300)
ent = Entry(window)
ent.place(x=150, y=300)
window.mainloop()