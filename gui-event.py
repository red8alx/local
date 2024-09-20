import tkinter

def change_color():
    frame.configure(bg="black")

frame = tkinter.Tk()
frame.title("GUI")
btn = tkinter.Button(frame, text="Login", width=50, command=change_color)

btn.pack()
frame.mainloop()
