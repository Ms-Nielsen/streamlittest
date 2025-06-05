import math
import streamlit as st

def main():
  x1 = st.text_input("Enter the first x coordinate:")
  y1 = st.text_input("Enter the first y coordinate:")
  x2 = st.text_input("Enter the second x coordinate:")
  y2 = st.text_input("Enter the second y coordinate:")

  if st.button("Calculate the distance!"):
    x1=int(x1)
    x2=int(x2)
    y1=int(y1)
    y2=int(y2)
    
    ans = calculate(x1, y1, x2, y2)
    ans_str = str(round(ans, 2))

    st.write("The distance is " + ans_str)

def calculate(x1, y1, x2, y2):
  xSubtract = x1 - x2
  ySubtract = y1 - y2
  
  print("x sub:", xSubtract)
  print("y sub:", ySubtract)
  
  xSquare = xSubtract ** 2
  ySquare = ySubtract ** 2

  print("x square:", xSquare)
  print("y square:", ySquare)

  add = xSquare + ySquare
  
  print(add)
  
  answer = math.sqrt(add)

  return answer


main()
