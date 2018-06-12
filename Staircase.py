#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    space = ' '
    hash = '#'
    for i in range(1,n+1):
        print_str = ''
        for j in range(n-i):
            print_str += space
        for k in range(i):
            print_str += hash
        print(print_str)

if __name__ == '__main__':
    n = int(input())

    staircase(n)
