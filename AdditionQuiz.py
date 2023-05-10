import random

#generate random numbers
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

#get an answer from a child

answer = eval(input("what is " +str(number1)+ " + " +str(number2)+ " ? "))
correctAnswer = number1 + number2

#evaluate bool
if correctAnswer =  answer:
    print(number1, "+", number2, "=", answer, "is", number1 + number2 == answer)
else:
    print(sum(number1, number2))

