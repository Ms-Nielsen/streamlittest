import streamlit as st
import random
import time


st.title("Number Guessing Game")

st.write("In this game, two players will compete to guess a number in the fastest. Each player will have three guesses. Good Luck")

time.sleep(3)


player1 = st.text_input("Enter name of player 1: ")
player2 = st.text_input("Enter name of player 2: ")
p1wins = 0
p2wins = 0
