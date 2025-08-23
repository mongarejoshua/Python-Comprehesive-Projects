# number guessing game 
import random 

secret_number = random.randint(1,100)
user_number = ''
limit = 20
count = 0

while user_number != secret_number:
    try:
        if count <= limit:
            user_number = int(input('Enter a random number between 1 and 100: '))
            count += 1
            if user_number == secret_number:
                print(f'Congratulations, You have got it correct at {count} attempts.')
            elif user_number < secret_number:
                print('You were below the secret number...try again.\n')
            elif user_number > secret_number:
                print('You were above the secret number...try again.\n')
        else:
            print('Out of guesses, You loose!\n')
            break

    except:
        print('Invalid input, please enter an integer.')
