import streamlit as st

def getGrade():
  grade = st.text_input("Enter a grade")
  return grade

def main():
  total = getGrade()
  count=1
  
  if st.button("Yes"):
    grade = getGrade()
    total +=grade
    count+=1
  
  if st.button("No"):
    average=total/count

main()
