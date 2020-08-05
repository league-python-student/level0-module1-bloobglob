from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    password = 'the password'
    secret_message = simpledialog.askstring('Secret Message', 'Enter your secret message:')
    input = simpledialog.askstring('Password', 'What is the password?')
    if input.lower() == password.lower():
        messagebox.showinfo('Secret Message', 'The secret message is: ' + secret_message)
    else:
        messagebox.showerror('INTRUDER', 'INTRUDER!!!!!!')