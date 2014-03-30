# Calculates the distance between the two cartesian coordinates
# (x_start,y_start) and (x_fin,y_fin) 
# Please note code works with Python ver 3.x

from ucb import main
from math import sqrt

def square (num): 
    return num * num

def distance (x_start, y_start, x_fin, y_fin):
    """ Calculates the distance between the two cartesian coordinates
	(x_start,y_start) and (x_fin,y_fin) """
    return sqrt(square(x_fin - x_start) + square(y_fin - y_start))
  
@main
def main():
    x_start = float(input("Enter the starting x co-ordinate : "))
    y_start = float(input("Enter the starting y co-ordinate : "))
    x_fin   = float(input("Enter the ending x co-ordinate : "))
    y_fin   = float(input("Enter the ending y co-ordinate : "))
    print ("Distance is ",distance(x_start, y_start, x_fin, y_fin))