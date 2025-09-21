import random, time

responses = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes - definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful.",
    "No."
]


def magic_ball_8():
    print("Welcome to Magic Ball 8 game!")
    
    while True:
        user_q = input('Ask a random yes/no question OR "exit" to quit: ')
        
        if user_q == "exit":
            break
        elif not user_q:
            print('Kindly ask a question...')
            continue
            
        response = random.choice(responses)
        time.sleep(3)
        
        print(response) 
    
if __name__ == "__main__":
    magic_ball_8()