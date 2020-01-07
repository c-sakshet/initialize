#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    if((n<1) | (n> 100)):
        return False
    for i in range(n-1,-1,-1):
        for j in range(n):
            if(j == n-1):
                print("#")
            # elif(i == 0 & j == n-1):
                # print("#")
            elif(j >= i):                           
                print("#",end="")                
            else:                
                print(" ",end="")
                
if __name__ == '__main__':
    n = int(input())

    staircase(n)


