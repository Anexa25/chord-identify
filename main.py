import tkinter as tk
from tkinter import *

root = tk.Tk()

root.title("Chord identifier")
root.minsize(200, 200)
root.configure(background="#365347")

canvas = tk.Canvas(root, width=2560, height=1600, bg="#698176")
canvas.pack()


fret_board = canvas.create_rectangle(0, 430, 1440, 780, fill="#F3D8B8")


frets = 1
string_spacing = 50
fret_spacing = 1350
widthn= 7

spacing = 40
multiplier = 1.253
x=0

for j in range(10):
    x += spacing
    canvas.create_line(x, 430, x, 530 + (5)*string_spacing, width=2, fill="black")
    spacing *= multiplier


for i in range(6):
    y = 480 + i*string_spacing
    canvas.create_line(0, y, 0 + frets*fret_spacing, y, width=widthn - i,fill="#843C08")


x_list = [64,190,390,705]

for i in range(4):
    y, r = 605, 10
    x = x_list[i]
    canvas.create_oval(x-r, y-r, x+r, y+r, fill="black", outline="black")
    

y_list = [480,530,580,630,680,725]
string_letters = ["E","A","D","G","B","e"]

for i in range(6):
    canvas.create_text(1390, y_list[i], text=string_letters[i], font=("Arial", 30), fill="#4A4544")
    
    
    
def on_click(event):
    r = 8
    canvas.create_oval(event.x-r, event.y-r, event.x+r, event.y+r, fill="red", outline="black")
    
canvas.bind("<Button-1>", on_click)



root.mainloop()

