#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    if(len(arr) > 100):
        return
    totInt = len(arr)
    i=0 
    negInt = 0 
    posInt = 0
    zero = 0
    for items in arr:
        if(items <= -100 | items >= 100):
            return
        if(items < 0):
            negInt += 1 
        elif(items > 0):
            posInt += 1 
        else:
            zero += 1
        i += 1
    if(posInt != 0):
        posFrac = posInt/totInt
        print(format(posFrac, '.6g'))
    else:
        print(0)
    if(negInt != 0):
        negFrac = negInt/totInt
        print(format(negFrac, '.6g'))
    else:
        print(0)
    if(zero != 0):
        zeroFrac = zero/totInt
        print(format(zeroFrac, '.6g'))    
    else:
        print(0)
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
