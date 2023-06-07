def main():
    print("Change Counter", end = "\n")
    print("Enter the count of each coin type")
    quarters, Dimes, Nickels, Pennies = map(int, input().split()) 
    total = quarters * 0.25 + Dimes * 0.10 + Nickels * 0.05 + Pennies * 0.01
    print()
    print("The total value of your change is: ", total)
main()
