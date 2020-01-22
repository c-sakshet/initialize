#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valley = 0
    seaLev = 0
    for step in s:
        
        if step == 'U':
            seaLev += 1
        elif step == 'D':
            seaLev -= 1
        else:
            print("Invalid Input")
            raise Exception("Invalid Input")
            exit(0)
        if seaLev == 0 and step == 'U':
            valley += 1 
    return valley
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    if n < 2 or n > pow(10,6):
        print("There must be at least 2 steps or less than 10000000 steps!")
        raise Exception("Invalid Input")
        exit(0)
    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
