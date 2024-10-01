import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def random_number():
    current = random.randint(1, 100)
    next = random.randint(1, 100)
    return current, next

def user_input():
    while True:
        guess = input('Guess if the next nunber will be higher or lower than tne current number.\n \nType "H" for higher, "L" for lower\n ').lower()
        if guess in ['h', 'l']:
            return guess
        else:
            print('Invalid input')

def play_again():
    while True:
        replay = input('\nDo you want to play the game again? YES/NO. \n').lower()
        if replay in ['yes', 'no']:
            return replay
        else:
            print('Invalid input.')

def game_logo():
    logo = '''   ____                       _____ _          
 / ___|_   _  ___  ___ ___  |_   _| |__   ___ 
| |  _| | | |/ _ \/ __/ __|   | | | '_ \ / _ \
| |_| | |_| |  __/\__ \__ \   | | | | | |  __/
 \____|\__,_|\___||___/___/   |_| |_| |_|\___|
| \ | |_   _ _ __ ___ | |__   ___ _ __        
|  \| | | | | '_ ` _ \| '_ \ / _ \ '__|       
| |\  | |_| | | | | | | |_) |  __/ |          
|_| \_|\__,_|_| |_| |_|_.__/ \___|_|        

'''
    return logo
def main():
    while True:
        score = 0
        current,next = random_number()
        game_over = False

        while not game_over:
            clear_screen()
            logo = game_logo()
            print(logo)
            print(f'CURRENT SCORE: {score}\n')
            print(f'CURRENT NUMBER: {current}\n')

            
            while next == current:
                next = random.randint(1, 100)

            guess = user_input()
            
            if guess == 'h':
                correct = next > current

            else:
                correct = current > next

            print(f'NEXT NUMBER: {next}\n')
            if correct:
                score += 1
                print('\nYou are correct!')
                current = next
                next = random.randint(1, 100)

            else:
                game_over = True
                print('You are wrong')
                print(f'\nGAME OVER. Your final score is {score}')

        replay = play_again()
        if replay == 'yes':
            main()
        else:
            clear_screen()
            print('THANK YOU FOR PLAYING THE GAME!')
            break



main()
# print(play_game)

