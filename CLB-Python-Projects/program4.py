# rock, paper scissors game
import random

"""
rock wins over scissors 
paper wins over rock
scissors wins over paper
"""

choices = ['rock', 'paper', 'scissors']
user_choice = ''
limit = 6
count = 0

print('---YOU HAVE SIX ATTEMPTS TO PLAY---\n')

while count < limit:
    computer_choice = random.choice(choices) # random.choice() is an inbuilt function
    user_choice = input('Enter your choice (rock, paper, scissors): ')

    if user_choice == computer_choice:
        print(f'You tied with the computer, the computer chose {computer_choice}')
    elif user_choice == 'rock' and computer_choice == 'scissors':
        print(f'You won, the computer chose {computer_choice}')
    elif user_choice == 'paper' and computer_choice == 'rock':
        print(f'You won, the computer chose {computer_choice}')
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print(f'You won, the computer chose {computer_choice}')
    else:
        print('The computer won!')

    count += 1