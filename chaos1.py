def main():
    print("This program illustrates a chaotic problem")
    x = eval(input("Enter number between 0 and 1: "))
    n = eval(input("How many numbers should I print? "))
    for i in range(n):
        x = 2.0 * x * (1-x)
        print(x)
main()
