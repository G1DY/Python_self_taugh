'''To illustrate software development process we create a program
that compute loan payment i.e car loan, student loan or home mortgage'''

# prompt the user to enter annual interest rate as a percentage
annualInterestRate = eval(input("Enter the annual interest rate e.g 10.0: "))

# calculates the monthly interest rate
monthlyInterestRate = annualInterestRate // 1200

#prompt the user to enter the loan period in years
numberOfYears = eval(input("Enter the number of years as an int eg 5: "))

# prompt the user to enter the loan amount
loanAmount = eval(input("Enter the loan amount e.g 500: "))

# calculate payment
monthlyPayment = loanAmount * monthlyInterestRate / (1
- 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))

totalPayment = monthlyPayment * numberOfYears * 12

# Display results
print("The monthly payment is", int(monthlyPayment * 100) / 100)
print("The total payment is", int(totalPayment * 100) /100)
