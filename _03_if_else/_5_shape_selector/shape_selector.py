import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    lucas = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring('Shape Selection', 'Enter a shape (Triangle, Square, Circle)')
    # Draw the shape requested by the user using if-elif-else statements
    if shape.lower() == 'triangle':
        turtle.circle(50, 360, 3)
    elif shape.lower() == 'square':
        turtle.circle(50, 360, 4)
    elif shape.lower() == 'circle':
        turtle.circle(50)
    else:
        messagebox.showerror(None, "Sorry, I don't know that one")
    # Call the turtle .done() method
    turtle.done()
    window.mainloop()