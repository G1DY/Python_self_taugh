import math
def newton_sqrt(x, num_iterations):
    guess = x / 2
    for i in range(num_iterations):
        guess = (guess + (x / guess)) / 2
    return guess
def main():
    x = float(input("Enter the number to get its sqrt: "))
    num_iterations = int(input("Enter the number of iterations: "))

    app_sqrt = newton_sqrt(x, num_iterations)
    diff = math.sqrt(x) - app_sqrt
    
    print("approximate sqrt is: ", app_sqrt)
    print("difference is: ", diff)
main()
