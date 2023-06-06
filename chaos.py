def main():
    print("This program illustrates a chaotic problem")
    x, y = eval(input("Enter number between 0 and 1: "))
    for i in range(10):
        x, y = 3.9 * x * (1-x), 3.9 * y * (1 - y)
        print(x, y(11.9f))
main()
