#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    
    beg_str = s[:2]
    end_str = s[6:]
    temp = ''
    letters = ['A','P','M']
    
    if 'PM' in s and int(beg_str) < 12:
        beg_str = int(beg_str) + 12
        
    if 'AM' in s and int(beg_str) == 12:
        beg_str = '00'
        
    for char in end_str:
        if char not in letters:
            temp += char
            
    return str(beg_str) + s[2:6] + temp
    
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
