import streamlit as st
total = 0
count = 0
def getGrade(count):
  grade = st.text_input("Enter grade " + str(count))
  return grade

def main():
  global count, total
  count=1
  total = getGrade(count)
  
  buttons()
  
def buttons():
  global count, total
  st.write("Do you want to enter another grade?")
  if st.button("Yes, enter grade " + str(count + 1)):
    count+=1
    grade = getGrade(count)
    total +=grade
    st.write("Do you want to enter another grade?")
    buttons()
    
  if st.button("No, " + str(count)+ " grades are enough."):
    average=total/count
    st.write("Your grade average is " + str(average))
    
main()
