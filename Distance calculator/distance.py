from tkinter import *
import tkinter.font as font

window = Tk()
window.geometry("500x300")

window.config(background = "lightblue")

def distance_conv():
    s = float(speed_input.get())
    t = float(time_input.get())
    dist = (s * t)
    distance_output.delete("1.0",END)
    distance_output.insert(END,dist)


distance_output = Text(window,height = 2,width = 17)

speed_input = Entry(window)
time_input = Entry(window)

distancebtn = Button(window,text = "Distance", command = distance_conv, width = 8,pady = 5)


speedtxt = Label(window,text = "Enter speed in Km/h:",font = font.Font(size = 21))
timetxt = Label(window,text = "Time spent in Hr:",font = font.Font(size = 21))


speedtxt.place(x = 20, y = 30)
timetxt.place(x = 20, y = 70)

distancebtn.place(x = 190, y = 180)

distance_output.place(x = 180, y = 230)

speed_input.place(x = 250, y = 30)
time_input.place(x = 250, y = 70)

window.mainloop()