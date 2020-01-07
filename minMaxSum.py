#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    n = len(arr)
    minSum = 0 
    maxSum = 0
    # n = len(arr)
    for i in range(0,n):
        if(i != n-1 ):
            minSum += arr[i]
        if(i != 0 ):
            maxSum += arr[i]
    print(minSum , end = " ")
    print(maxSum)
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
