"""
build_tri_flag.py
Build a tricolout flag using tkinter Canvas widget.
"""

import tkinter              #in Python2, the t was uppercase

print("Let's build a tri-colour flag")
orientation = input("Would you like horizontal or vertical stripes? Enter H or V: ")
colour = [ input("Pick the 1st colour: "), input("Pick the 2nd colour: "), input("Pick the 3rd colour: ") ]

#The root widget is the window that will contain everything we draw.
root = tkinter.Tk()
root.title("Tri-colour Flag")

#dimensions of entire flag, in pixels
height = 300 
width = 600 
root.geometry(f"{width}x{height}")

canvas = tkinter.Canvas(root, highlightthickness = 0)
hoffset = 0
voffset = 0

if orientation == "V":
    for i in range(3):
        canvas.create_rectangle(hoffset, 0, hoffset + 200, width, width = 0, fill = colour[i])
        hoffset = hoffset + 200

if orientation == "H":
    for i in range(3):
        canvas.create_rectangle(0, voffset, width, voffset+100, width = 0, fill = colour[i])
        voffset = voffset + 100

#Make the canvas visible by packing it into the root.
canvas.pack(expand = tkinter.YES, fill = "both")

#If the flag had buttons, checkboxes, etc.,
#the mainloop would let them respond to touches.
root.mainloop()
