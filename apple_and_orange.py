# s = start point of house
# t = endpoint of house
# a = apple tree
# b = orange tree
# d = fruit distance when falls


import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def count_apples_and_oranges(s, t, a, b, apples, oranges):
    apples_count = 0;
    oranges_count = 0;

    for apple in apples:
        if apple > 0:
            if apple + a >= s and apple + a <= t:
                apples_count += 1;

    print(apples_count)

    for orange in oranges:
        if orange < 0:
            if orange + b >= s and orange + b <= t:
                oranges_count += 1;

    print(oranges_count, end="")


if __name__ == '__main__':

    s = 7
    t = 11

    a = 5
    b = 15

    m = 3
    n = 2

    apples = [-2, 2, 1]
    oranges = [5, -6]

    count_apples_and_oranges(s, t, a, b, apples, oranges)

