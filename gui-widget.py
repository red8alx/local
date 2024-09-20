import tkinter
frame = tkinter.Tk()
frame.title("GUI")
# add widgets here
lbl = tkinter.Label(frame, text="Welcome to Heyday")
btn = tkinter.Button(frame, text="Login", width=25)
lbl.pack()
btn.place(x=50,y=100)
frame.mainloop()