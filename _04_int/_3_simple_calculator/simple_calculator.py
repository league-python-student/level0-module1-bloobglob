# Write a Python program that asks the user for two numbers.
# Then ask the user if the would like to add, subtract, multiply, or divide.
# Use if-else statements to provide the desired math operation on the numbers and display the result.
from tkinter import Tk, simpledialog, messagebox
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    num1 = simpledialog.askinteger(None, 'Pick a number')
    num2 = simpledialog.askinteger(None, 'Pick another number')
    operation = simpledialog.askstring('Operation', 'Choose an operation (add, subtract, multiply, divide)')
    if operation.lower() == 'add':
        messagebox.showinfo(None, 'The result is ' + str(num1 + num2))
    elif operation.lower() == 'subtract':
        messagebox.showinfo(None, 'The result is ' + str(num1 - num2))
    elif operation.lower() == 'multiply':
        messagebox.showinfo(None, 'The result is ' + str(num1 * num2))
    elif operation.lower() == 'divide':
        messagebox.showinfo(None, 'The result is ' + str(num1 / num2))
    else:
        messagebox.showerror(None, "Sorry, I don't know that")