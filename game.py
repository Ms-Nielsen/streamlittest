import streamlit as st

st.write
print('Hello world, today you two players will be playing a guessing game to guess a number between 1 and 10. You will each have three tries.')

player1 = input("Enter name of player 1: ")
player2 = input("Enter name of player 2: ")
p1wins = 0
p2wins = 0
gameround = 1


for x in range (1,4):
    import random
    secretnum = random.randint(1,10)
    guess = 0
    game = 1
    
    
     
    
    print("Round:", gameround)
    while guess != secretnum and game < 7: 
            if game %2 != 2:
             guess = int(input(str(player1) + ", input your guess: "))
        
            if guess < secretnum:
                print("Your number is too low.")
                game = game + 1
            
            elif guess > secretnum:
                print("Your number is too high.")
                game = game + 1
            
            if game %2 == 0:
                
            
                guess = int(input(str(player2) + ", input your guess: "))
            if guess < secretnum:
                print("Your number is too low.")
                game = game + 1
                
            elif guess > secretnum:
                print("Your number is too high.")
                game = game + 1
        
            if guess == secretnum and game %2 == 0:
                print("Congratulations,", player2, "you got the number correct!")
                p2wins = p2wins + 1
                gameround = gameround + 1
                
            if guess == secretnum and game %2 != 0:
                print("Congratulations,", player1, "you got the number correct!")
                p1wins = p1wins + 1
                gameround = gameround + 1
                
        
                
            if game > 6:
                print("Oops, you have both guessed three times. \n", player1, "and", player2, "you guys are losers. Game Over.")
                gameround = gameround + 1
if p1wins > 1:
    print("Congratulations,", player1, "you have won a majority of the games. You are the true winner," , player2 , "you are a loser.")
if p2wins > 1:
    print("Congratulations,",player2, "you have won a majority of the games. You are the true winner,", player1, "you are a loser.")
print('Thanks for playing!')
