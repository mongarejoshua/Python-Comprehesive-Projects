import random

word_list = ['apple', 'banana', 'spoon', 'plate', 'table', 'matchbox']
word = random.choice(word_list).upper()

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

print(word)
    
    