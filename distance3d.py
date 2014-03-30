# Calculates the distance between the two 3d cartesian coordinates
# (x_start,y_start,z_start) and (x_fin,y_fin,z_fin) 
# Please note code works with Python ver 3.x

from ucb import main
from math import sqrt

def square (num): 
    return num * num

def distance3d (x_start, y_start, z_start, x_fin, y_fin ,z_fin):
    """ Calculates the distance between the two 3d cartesian coordinates
	(x_start,y_start,z_start) and (x_fin,y_fin,z_fin) """
    return sqrt(square(x_fin - x_start) + square(y_fin - y_start) + square(z_fin - z_start))
  
@main
def main():
    x_start = float(input("Enter the starting x co-ordinate : "))
    y_start = float(input("Enter the starting y co-ordinate : "))
    z_start = float(input("Enter the starting z co-ordinate : "))
    x_fin   = float(input("Enter the ending x co-ordinate : "))
    y_fin   = float(input("Enter the ending y co-ordinate : "))
    z_fin   = float(input("Enter the ending z co-ordinate : "))
    print ("Distance is ",distance3d(x_start, y_start, z_start, x_fin, y_fin ,z_fin))