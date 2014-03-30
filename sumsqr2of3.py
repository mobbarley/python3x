from ucb import main

def square (num):
    return num * num

def two_of_three( num1, num2, num3):
    return (num1 * num1) + (num2 * num2) + (num3 * num3) - square(min(num1, num2, num3))

@main
def main():
    num1 = float(input("Enter the number #1 : "))
    num2 = float(input("Enter the number #2 : "))
    num3 = float(input("Enter the number #3 : "))
    print ("Sum of squares of max 2 of 3 numbers is ", two_of_three(num1, num2, num3))