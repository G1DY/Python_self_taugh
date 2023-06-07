import math
def main():
    print("This programs solves a quadratic equation")
    print()
    a, b, c = eval(input("Enter the values of (a, b, c): "))
    sqrtpart = math.sqrt((b * b) - (4 * a * c))
    root1 = (-b + sqrtpart) / (2 * a)
    root2 = (-b - sqrtpart) / (2 * a)
    print("The solution of x is: ", root1, root2)
    print()
main()
