def guess_check(number,user_guess):
    if user_guess == number:
        return True
    elif user_guess > number:
        print ("You've Gone over")
        return False
    elif user_guess < number:
        print("You've gone under")
        return False

def main_game(lives_start):
    success = False
    while lives_start != 0 and success == False:
        guess = int(input("Enter a number between 1 and 100:"))
        guess_status = guess_check(num,guess)
        if guess_status == True:
            success = True
        else:
            lives_start-=1
            print(f'You have {lives_start} guesses remaining.')
    if success == True:
        return True
    else:
        return False

def easy(secret_number):
    lives = 10
    success_status = main_game(lives)
    if success_status == True:
        print ("Congratulations! You Guessed Correct")
    else:
        print("Sorry, You're out of Guesses. Game Over!")
        print(f"The correct number was {num}")



def hard(secret_number):
    lives = 5
    success_status = main_game(lives)
    if success_status == True:
        print ("Congratulations! You Guessed Correct")
    else:
        print("Sorry, You're out of Guesses. Game Over!")
        print(f"The correct number was {num}")
        
import random
from art import logo
num = random.randint(1,100)


print(logo)
level = input("Do you want to play in easy mode or hard mode? enter 'easy' or 'hard'. ").lower()
print("I'm thinking of a number between 0 and 100. Can You Guess it?")

if level == "easy":
    easy(num)
else:
    hard(num)
