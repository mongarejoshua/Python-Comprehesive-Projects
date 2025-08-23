# secret word game (version 1)
guess = ''
count = 0
limit = 5
playing = ''
secret_word = 'cow'
# any input from the user is considered as a string

while True:
    playing =  input('Do you want to play? (yes/no) or "q" to quit: ')

    if playing.lower() == 'yes':
        while True:
            guess = input('1. Enter a word (Hint --- an animal, gives us milk): ')
            count += 1
                    
            if guess != secret_word:
                    print('Incorrect, please try again')
            elif count == limit:
                print('You are out of guesses.')
                break
            elif guess == secret_word:
                print('Congratulations, you got it right.\n')
                guess = input('2. Enter another word --- (Hint ---- a communication device): ')
                if guess != secret_word:
                    print('Incorrect, please try again')
                elif count == limit:
                    print('You are out of guesses.')
                break

    elif playing.lower() == 'no' or 'q':
        print('Goodbye')
        break
    else:
        print('Invalid choice entry, please try again.')
    

