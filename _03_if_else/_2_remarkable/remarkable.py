from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    name = simpledialog.askstring(None, 'Please enter a name')
    if name.lower() == 'charlie':
        messagebox.showinfo('Charlie', 'Charlie is very enthusiastic')
    elif name.lower() == 'zachary':
        messagebox.showinfo('Zachary', 'Zachary is very independent')
    elif name.lower() == 'dave':
        messagebox.showinfo('Dave', 'Dave is very funny')
    else:
        messagebox.showinfo(None, "Sorry, I don't know that name")
