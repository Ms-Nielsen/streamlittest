import streamlit as st

def getGrade(count):
  grade = st.text_input("Enter grade " + str(count))
  return grade

def main():
  count=1
  total = getGrade(count)
  
  st.write("Do you want to enter another grade?")
  if st.button("Yes"):
    count+=1
    grade = getGrade(count)
    total +=grade
    
  if st.button("No"):
    average=total/count

main()
