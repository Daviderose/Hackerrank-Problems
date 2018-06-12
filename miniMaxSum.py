#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min = 0
    max = 0
    min_sum = 0
    max_sum = 0
    
    for i in arr:
        if i >= max:
            max = i
        min = max
        
    for i in arr:
        if i <= min:
            min = i
            
    arr.remove(max)
    min_sum = sum(arr)
    arr.append(max)
    arr.remove(min)
    max_sum = sum(arr)
    arr.append(min)
        
    print(str(min_sum) + " " + str(max_sum))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
