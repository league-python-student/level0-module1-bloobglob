'''
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got correct
'''
from tkinter import Tk, messagebox, simpledialog
if __name__ == '__main__':
    score = 0
    window = Tk()
    window.withdraw()
    riddle1 = simpledialog.askstring(None, 'When do astronauts eat their sandwiches?')
    if riddle1.lower() == 'at launch time':
        score+=1
    riddle2 = simpledialog.askstring(None, 'You live in a one story house entirely made of redwood. What color would the stairs be?')
    if riddle2.lower() == 'no color':
        score+=1
    riddle3 = simpledialog.askstring(None, 'What has six faces, but does not wear makeup, has twenty-one eyes, but cannot see? ')
    if riddle3.lower() == 'a die':
        score+=1
