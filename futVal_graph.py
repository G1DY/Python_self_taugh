from graphics import *
def main():
    #Title of our graph
    print("This program plots the growth of a 10 year Investment")
    #get the principal and interest as input
    principal = eval(input("Enter the principal amount: "))
    appr = eval(input("Enter the interest rate as a decimal: "))
    #create a graphical window
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    #print label along the left edge of the window
    Text(Point(20, 380), ' 0.0K').draw(win)
    Text(Point(20, 305), ' 2.5K').draw(win)
    Text(Point(20, 230), ' 5.0K').draw(win)
    Text(Point(20, 155), ' 7.5K').draw(win)
    Text(Point(20,  60), '10.0K').draw(win)
    #Right edge: Draw bar for the initial principal
    height = principal * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230 - height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    #draw successive bars
    for year in range(1, 11):
        #calculate value of next year
        principal = principal * (1 + appr)
        #draw bar for this value
        xLL = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(xLL, 230), Point(xLL + 25, 230 - height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)
    
    input("Press <Enter> to quit")
    win.close()

main()
