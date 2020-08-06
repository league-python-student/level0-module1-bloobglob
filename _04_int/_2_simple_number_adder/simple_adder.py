# Write a Python program that asks the user for two numbers. 
# Then display the sum of the two numbers
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    num1 = simpledialog.askinteger(None, 'Enter a number')
    num2 = simpledialog.askinteger(None, 'Enter a number')
    messagebox.showinfo('Sum', 'The sum of the 2 numbers is ' + str(num1+num2))