from random import randint
from art import logo

EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5

def check_ans(guess, answer,turns):
    if guess>answer:
        print("too high")
        return turns-1
    
    elif guess<answer:
        print("too low")
        return turns-1
    
    else:
        print(f"you got it, The ans is: {answer}")
        
def difficulty():
    level= input("Choose a difficulty.Type'easy' or'hard':")
    if level=="easy":
        return EASY_LEVEL_TURNS
    
    if level=="hard":
        return HARD_LEVEL_TURNS
    
def play_game():
    print(logo)
    print("Welcome to the Number Guessing game..!!!")
    print("I am thinking of the number game between 1 and 100.")
    ans = randint(1,100)
    # print(f"the ans is {ans}")
    turns= difficulty()
    guess=0
    while guess!=ans:
        print(f"you have{turns} remaining to guess the ans")
        
        guess=int(input("enter a number:"))
        turns=check_ans(guess,ans,turns)
        if guess!=ans:
            print("guess again")
        elif turns==0:    
            print("you run out of guesses")
            return

play_game()
        
        

                    
    

