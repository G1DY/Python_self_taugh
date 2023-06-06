import math

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return (result)
    except Excemption as error:
        print("Invalid expression: ", error)
def main():
    for i in range(100):
        expression = input("Enter an expression or q to quit: ")
        if expression.lower() == 'q':
            break
        result = evaluate_expression(expression)
        if result is not None:
            print("Result is: ", result)
        print()

if __name__ == '__main__':
    main()
