import tkinter as tk
from tkinter import *

root = tk.Tk()

root.title("Chord identifier")
root.minsize(200, 200)
root.configure(background="#365347")

# Canvas creation
canvas = tk.Canvas(root, width=2560, height=1600, bg="#698176")
canvas.pack()

canvas.create_text(710, 100, text="Chord Identifier", font=("Arial", 65), fill="black")
bottom_text_id = canvas.create_text(710, 870, text="Click to place note", font=("Arial", 20), fill="black")





# Fretboard creation
fret_board = canvas.create_rectangle(0, 430, 1440, 800, fill="#6E5E4C", outline="#6E5E4C")
fret_board = canvas.create_rectangle(0, 430, 1440, 780, fill="#F3D8B8", outline="#F3D8B8")

string_spacing = 50
fret_spacing = 1350
width_n = 7

spacing = 40
multiplier = 1.253
x = 0


# Adding the frets
fret_positions = [0]  # include nut at x=0
for i in range(10):
    x += spacing
    fret_positions.append(x)
    canvas.create_line(x, 430, x, 530 + (5) * string_spacing, width=2, fill="black")
    spacing *= multiplier

# Adding the strings
for i in range(6):
    y = 480 + i * string_spacing
    canvas.create_line(0, y, 0 + fret_spacing, y, width=width_n - i, fill="#843C08")

x_list = [64, 190, 390, 705]
for i in range(4):
    y, r = 605, 10
    x = x_list[i]
    canvas.create_oval(x - r, y - r, x + r, y + r, fill="black", outline="black")

# Adding the string base notes
y_list = [480, 530, 580, 630, 680, 725]
string_letters = ["E", "A", "D", "G", "B", "e"]
for i in range(6):
    canvas.create_text(1390, y_list[i], text=string_letters[i], font=("Arial", 30), fill="#4A4544")


STRING_TUNING = ["E","A","D","G","B","E"]

NOTES = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]


def get_note(string_index,fret_index):
    open_note = STRING_TUNING[string_index]
    note_index = NOTES.index(open_note)
    STRING_TUNING = ["E","A","D","G","B","E"]

NOTES = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]


def get_note(string_index,fret_index):
    open_note = STRING_TUNING[string_index]
    note_index = NOTES.index(open_note)
    
    pressed_note_index = (note_index + fret_index) % 12
    note = NOTES[pressed_note_index]
    
 
    return note







# Interactivity with snapping
note_display_id = None

dots = []



def on_click(event):
    global note_display_id
    r = 13  

    # Fretboard vertical limits
    fret_top = 480
    fret_bottom = 780
    string_count = 6
    string_spacing = 50

    if event.y < fret_top or event.y > fret_bottom:
        return

    # Snap to nearest string
    string_index = round((event.y - fret_top) / string_spacing)
    string_index = max(0, min(string_count - 1, string_index))
    snapped_y = fret_top + string_index * string_spacing

    # Fret positions
    fret_positions = []
    x = 0
    spacing = 40
    multiplier = 1.253
    for i in range(10):
        x += spacing
        fret_positions.append(x)
        spacing *= multiplier

    if event.x < fret_positions[0] or event.x > fret_positions[-1]:
        return

    # Determine fret number 
    num_frets = len(fret_positions)
    fret_index = 0  
    for i in range(num_frets - 1):
        if fret_positions[i] <= event.x < fret_positions[i + 1]:
            fret_index = num_frets - 1 - i  
            break
    if event.x >= fret_positions[-1]:
        fret_index = 1 

    # Center dot in that fret
    if fret_index == 0:
        snapped_x = fret_positions[0] / 2  
    else:
        left = fret_positions[num_frets - fret_index - 1]
        right = fret_positions[num_frets - fret_index]
        snapped_x = (left + right) / 2

    # Draw dot
    dot_id = canvas.create_oval(
        snapped_x - r, snapped_y - r, snapped_x + r, snapped_y + r,
        fill="red", outline="red"
    )
    dots.append(dot_id)


    note_name = get_note(string_index,fret_index)

    if note_display_id is None:
        note_display_id = canvas.create_text(710, 250, text=note_name, font=("Arial", 50), fill="white")
    else:
        canvas.itemconfig(note_display_id, text=note_name)

    canvas.delete(bottom_text_id)
    
    




# Clear dots
def clear_dots():
    global note_display_id, bottom_text_id
    for dot in dots:
        canvas.delete(dot)
    dots.clear()
    
    if note_display_id is not None:
        canvas.itemconfig(note_display_id, text="-")
        
        
    # Restore the bottom instruction text
    if bottom_text_id is not None:
        canvas.delete(bottom_text_id)
        
    bottom_text_id = canvas.create_text(710, 870, text="Click to place note", font=("Arial", 20), fill="black")
    


canvas.bind("<Button-1>", on_click)

clear_button = tk.Button(root, text="Clear", command=clear_dots, padx=2, pady=2)
canvas.create_window(1390, 870, window=clear_button)








root.mainloop()
