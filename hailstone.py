# Print the hailstone sequence starting at a given number and
# terminates at 1 and also returns its length.
# This code is compatible with Python v3.x

from ucb import main

def hailstone (num):
    """ Print the hailstone sequence starting at a given number and
        terminates at 1 and also returns its length. """
    step = 0
    while num != 1:
      if num%2 == 0 :
        num = num / 2
        step = step + 1
        print(int(num))
      else:
        num = (num * 3) + 1
        step = step + 1
        print(int(num))
    print("Steps taken : ",step)
    
@main
def main():
    num = int(input("Enter a number : "))
    if num > 0:
      hailstone(num)
    else:
      print("Invalid number", num)
    