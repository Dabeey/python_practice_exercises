import random
from list import word_list
from artword import logo
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def random_word(word_list):
    return random.choice(word_list)

def replace_letter(word):
    return [" _ " for _ in word]

def user_guess():
    while True:
        guess = input('Guess a letter\n').lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print('Invalid input. Please enter a single letter.')

def validate_input(display, guess, word):
    for position in range(len(word)):
        if word[position] == guess:
            display[position] = guess
    return display

def play_again():
    while True:
        replay = input('\nDo you want to play again? YES/NO \n').lower()
        if replay in ['yes', 'no']:
            return replay
        else:
            print('Invalid input. Please enter YES or NO.')

def main():
    while True:
        lives = 10
        game_over = False

        word = random_word(word_list)
        display = replace_letter(word)

        print(logo)
        print(f"The word has {len(word)} letters.")
        
        while not game_over:
            print(' '.join(display))
            guess = user_guess()

            if guess in word:
                display = validate_input(display, guess, word)
            else:
                lives -= 1
                print(f'Incorrect guess. You have {lives} lives remaining.\n')

            if lives <= 0:
                game_over = True
                print(f'Sorry, you ran out of lives. The word was "{word}".')

            if " _ " not in display:
                game_over = True
                print(f'\nCongratulations, YOU WIN! The word was "{word}".')

        replay = play_again()
        if replay == 'no':
            clear_screen()
            print('GOODBYE!')
            break
        else:
            clear_screen()

if __name__ == "__main__":
    main()
