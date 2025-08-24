import random

secret_words = ['apple', 'banana', 'spoon', 'plate', 'table', 'matchbox']

hangman_art = {0: ("     ",
                   "     ",
                   "     "),
               
               1: ("  o  ",
                   "     ",
                   "     "),
               
               2: ("  o  ",
                   "  |  ",
                   "     "),
               
               3: ("  o  ",
                   " /|  ",
                   "     "),
               
               4: ("  o  ",
                   " /|\\",
                   "     "),
               
               5: ("  o  ",
                   " /|\\",
                   " /  "),
               
               6: ("  o  ",
                   " /|\\",
                   " / \\")
               }

for key in hangman_art[6]:
    print(key)
    
    