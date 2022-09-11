def guess_check(secret_number,user_guess):
    '''
Check if the user's guess is equal to, greater than or less than the secret number and only return 'True' if the guess is equal. The input is secret number and user's guess.
If the guess is incorrect, the user is informed whether they were above or below the correct value.
'''
    if user_guess == secret_number:
        return True
    elif user_guess > secret_number: 
        print ("You've Gone over")
        return False
    elif user_guess < secret_number:
        print("You've gone under")
        return False

def main_game(lives_start):
    '''
    Takes in the number of lives at the start depending on difficulty level and returns True only if the user guesses the secret number before running out of lives (guesses)
    '''
    success = False #create a variable called success that is false by default
    while lives_start != 0 and success == False: #Initiate while loop that runs until number of lives is equal to zero or the user guesses the correct secret number
        guess = int(input("Enter a number between 1 and 100:")) #Prompt user to guess a number between 1 and 100
        guess_status = guess_check(num,guess) #Run the user's guess through the guess-check function and assign the falue to a variable 'guess status'
        if guess_status == True: #If the check returns True, the success variable is set to True
            success = True
        else:                   #If the check returns False, the user loses one life and the computer informs them how many lives they have left
            lives_start-=1 
            print(f'You have {lives_start} guesses remaining.')
    if success == True: #At the end of the while loop, the function returns 'True' only if the success variable is also True
        return True
    else:
        return False

def easy(secret_number):
    '''
    Function is executed if the user chooses the easy mode. The lives variable is equal to 10. 
    '''
    lives = 10
    success_status = main_game(lives) #The success_status variable is assigned the value that is output after the 'main_game' function has finished running
    if success_status == True: #If the success_status variable is equal to true, the user is informed they won, else they're informed that they lost and shown the actual secret number
        print ("Congratulations! You Guessed Correct")
    else:
        print("Sorry, You're out of Guesses. Game Over!")
        print(f"The correct number was {num}")



def hard(secret_number):
    '''
    Function is executed if the user chooses the hard mode. The lives variable is equal to 5. 
    '''
    lives = 5
    success_status = main_game(lives) #The success_status variable is assigned the value that is output after the 'main_game' function has finished running
    if success_status == True: #If the success_status variable is equal to true, the user is informed they won, else they're informed that they lost and shown the actual secret number
        print ("Congratulations! You Guessed Correct")
    else:
        print("Sorry, You're out of Guesses. Game Over!")
        print(f"The correct number was {num}")
        
import random #import the random library
from art import logo #import the logo variable from the art script
num = random.randint(1,100) #assign a random number between 1 and 100 to the num variable


print(logo) #Print the logo variable
level = input("Do you want to play in easy mode or hard mode? enter 'easy' or 'hard'. ").lower() #Prompt user to enter difficulty level
print("I'm thinking of a number between 0 and 100. Can You Guess it?") #Tell user instructions

if level == "easy": #If user chose easy mode, execute the easy() function, else execute the hard() function
    easy(num)
else:
    hard(num)
