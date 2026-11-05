
print("Welcome to quiz in python")

score = 0

print("\n 1. Who is developed python?")
print("A. Dennis ritchi")
print("B. Guido Van Rossum")
print("C. Elon Musk")
print("D. Ajahar Pathan")

answer = input("Select your answer:")

if answer == "B":
    score+= 1
   

print("\n2. Which symbol is used for comments in Python?")
print("A. //")
print("B. #")
print("C. /* */")
print("D. &/")
answer = input("Select your answer: ")

if answer == "B":
    score += 1


print("\n3. Which function is used to display output?")
print("A. print()")
print("B. input()")
print("C. display()")
print("D. scanf()")
answer = input("Select your answer: ") 

if answer == "A":
    score+=1
    

print("\n4. Which data type stores text?")
print("A. int")
print("B. float")
print("C. str")
print("D. char")
answer = input("Select your answer: ")

if answer == "C":
    score+=1
    

print("\n5. Which operator is used for multiplication?")
print("A. +")
print("B. *")
print("C. /")
print("D. %")
answer = input("Select your answer: ")  

if answer == "B":
    score += 1
    

print("\n6. when python language developed?")
print("A. 1991")
print("B. 1890")
print("C. 1990")
print("D. 1970")
answer = input("Select your answer: ")  

if answer == "A":
    score+=1
   

print("\n7. Which loop is used for store sequence of character?")
print("A. if")
print("B. for")
print("C. def")
print("D. while")
answer = input("Select your answer: ")   

if answer == "B":
    score+=1
    

print("\n8. Which datatype stores unique value?")
print("A. List")
print("B. Tuple")
print("C. Set")
print("D. Dict")
answer = input("Select your answer: ") 

if answer == "C":
    score+=1
    


print("\n9. What is the output of 10 + 3?")
print("A. 3")
print("B. 13")
print("C. 1")
print("D. 12")
answer = input("Select your answer: ")  

if answer == "B":
    score+=1
    

print("\n10. What is the output of 10 / 5?")
print("A. 2")
print("B. 3")
print("C. 1")
print("D. 15")
answer = input("Select your answer: ")

if answer == "A":
    score+=1
    


print("Your Score is:", score, "/ 10")    


# questions = {"\n 1. Who is developed python?",
#             "\n 2. What is the output of 10 / 5",
#              "\n3. What is the output of 10 + 3?",
#              "\n4. Which datatype stores unique value?",
#               "\n5. Which loop is used for store sequence of character?",
#              "\n6. when python language developed?",
#               }

# for i in questions:
#     print(i)

# for i in range(len(questions)):
#     print(i + 1, questions[i]) 

# for i in range(len(questions)):
#     print(i + 1, questions[i])
#     answer = input("Enter your answer: ")       