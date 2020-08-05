from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    birthday = simpledialog.askstring("Birthday", 'What is your birthday? (MM/DD)')
    if birthday == '08/05':
        messagebox.showinfo(None, 'Happy Birthday!')
    else:
        messagebox.showinfo(None, 'Happy Unbirthday!')