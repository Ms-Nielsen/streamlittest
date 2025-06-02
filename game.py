import streamlit as st
import random
import time


p1wins = 0
p2wins = 0

st.title("Number Guessing Game")

st.write("In this game, two players will compete to guess a number in the fastest. Each player will have three guesses. Good Luck")

time.sleep(3)

def name_entries(num):
  player = st.text_input("Enter name of player " + num + ": ")
  return player
  
def getGuess(name):
  st.write(name + " it is your turn.")
  guess = st.slider(name + "Guess a number between 1 and 10", min_value = 1, max_value=10)
  return guess
  
def main():
  player2name = ' '
  player1name = name_entries('1')
  
  if player1name!='':
    player2name=name_entries('2')
    
  p1guess = getGuess(player1name)

  if st.button("Continue"):
    p2guess = getGuess(player2name)
    

main()
