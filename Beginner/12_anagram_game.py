import random

words = ['ideas', 'alert', 'elbow', 'dog', 'earth', 'vile', 'wolf', 'angle', 'night', 'rates']

rand_word = random.choice(words)

unp = list(rand_word)
random.shuffle(unp)
scr_word = "".join(unp)

print(scr_word)

while True:
    user_g = input('Enter your guess: ')
    
    if user_g == rand_word:
        print('Correct!')
        break
    else:
        print('Incorrect') 