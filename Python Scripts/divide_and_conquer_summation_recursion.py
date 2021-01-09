# Load your file and cast it to integers here.
with open('random_integers.txt', mode='r') as f:
    random_integers = list(map(int, f.read().split()))

import math

def summation(values):
    length = len(values)
    midpoint = math.ceil(length/2)
    if length == 1:
        return values[0]
    return summation(values[:midpoint]) + summation(values[midpoint:])

divide_and_conquer_sum = summation(random_integers)