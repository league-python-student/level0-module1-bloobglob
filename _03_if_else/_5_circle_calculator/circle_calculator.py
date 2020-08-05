from tkinter import simpledialog, Tk, messagebox
import math
# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    radius = simpledialog.askinteger('Radius', 'Please enter a radius for your circle')
    input = simpledialog.askstring('Area or Circumference', 'Would you like the area or circumference?')
    if input.lower() == 'area':
        calculation = radius*radius*math.pi
        messagebox.showinfo('Area', 'The area is ' + str(calculation))
    elif input.lower() == 'circumference':
        calculation = 2*math.pi*radius
        messagebox.showinfo('Circumference', 'The circumference is ' + str(calculation))
    else:
        messagebox.showerror('Option Not Found', "Sorry, I don't understand")