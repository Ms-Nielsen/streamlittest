import streamlit as st
import random
import time


p1wins = 0
p2wins = 0

st.title("Number Guessing Game")

st.write("In this game, two players will compete to guess a number in the fastest. Each player will have three guesses. Good Luck")

time.sleep(3)

def name_entries():
  player1 = st.text_input("Enter name of player 1: ")
  player2 = st.text_input("Enter name of player 2: ")
  return player1, player2
  
def getGuess(name):
  st.write(name + " it is your turn.)
  guess = st.slider("Guess a number between 1 and 10", min_value = 1, max_value=10)
  return guess
def main():

  player1name, player2name = name_entries()
  p1guess = getGuess(player1name)

main()
