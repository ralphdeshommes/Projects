from tkinter import *




window = Tk()
window.title("rock papter scissors")
window.geometry("300x300")
frame = Frame(window)
frame.pack()
top_left = Button(frame,text="X")
top_left.pack(side=RIGHT)
middle_left = Button(frame,text="xx")
middle_left.pack(side=LEFT)


window.mainloop()