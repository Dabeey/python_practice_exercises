import os
import random
from art import logo, vs
from game_data import data

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def random_account(data):
    account_a = random.choice(data)
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    return account_a, account_b
# account_a, account_b = random_account(data)

def format(account):
    def verb(description):
        if description[0].lower() in ['a','e','i','o','u']:
            return 'an'
        else:
            return 'a'
        '''a simpler method'''
        # return 'an' if description[0].lower() in ['a','e','i','o','u'] else 'a'
    name = account['name']
    description = account['description']
    country = account['country']
    return (f'{name}, {description} from {country}')

def user_guess():
    while True:
        guess = input("\nWho has higher followers? A' or 'B'\n").lower()
        if guess in ['a', 'b']:
            return guess
        else:
            print('Invalid input')
        
def follower_count(account):
    followers = account['follower_count']
    return followers

score = 0
game_over = False
account_b = random.choice(data)

while not game_over:
    clear_screen()
    print(f'\nYour current score is {score}\n')
    print(logo)
    
    account_a = account_b
    while account_a == account_b:
        account_b = random.choice(data)

    format_a = format(account_a)
    format_b = format(account_b)

    print(f'ACCOUNT_A: {format_a}')
    print(vs)
    print(f'ACCOUNT_B: {format_b}')

    guess = user_guess()
    followers_a = follower_count(account_a)
    followers_b = follower_count(account_b)

    if guess == 'a':
        correct = followers_a > followers_b

    else:
        correct = followers_b > followers_a

    print(f'Account A followers: {followers_a}')
    print(f'Account B followers: {followers_b}')

    if correct:
        score += 1
        print('You are right!')

    else:
        game_over = True
        print('You are wrong.')


print(f' GAME OVER. Your final score is {score}')
