#Coordinates
#Samuel Renneke, 3/1/2026

import math

def distance_calculation (coordinate_set1, coordinate_set2):
    distance = math.sqrt((coordinate_set2[0]-coordinate_set1[0])**2 + (coordinate_set2[1]-coordinate_set1[1])**2 + (coordinate_set2[2]-coordinate_set1[2])**2)
    return distance

def inputs ():
    x1 = float(input("Enter the first x value: "))
    y1 = float(input("Enter the first y value: "))
    z1 = float(input("Enter the first z value: "))
    coordinate_set1 = (x1, y1, z1)

    x2 = float(input("Enter the second x value: "))
    y2 = float(input("Enter the second y value: "))
    z2 = float(input("Enter the second z value: "))
    coordinate_set2 = (x2, y2, z2)

    distance_calculation(coordinate_set1, coordinate_set2)
