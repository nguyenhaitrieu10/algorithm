#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decibinaryNumbers' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER x as parameter.
#
from bisect import bisect_left
def decibinaryNumbers(n):
    
    MAX_DIGIT_PLACE = 4
    MAX_VALUE = 10
    
    # Step 1: Precompute ways to form numbers using decibinary representation
    dp = [[0] * MAX_DIGIT_PLACE for _ in range(MAX_VALUE)]
    for i in range(10):
        dp[i][1] = 1
    
    for i in range(2, MAX_VALUE+1):

        for j in range(2, MAX_DIGIT_PLACE + 1):
            for value in range(1, 10):
                base = value * (1 << (j-1))
                if base > value:
                    break
            else:
                
                     

    

if __name__ == '__main__':
    fin = open(os.environ['INPUT_PATH'], 'r')
    fout = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(fin.readline().strip())
    print(f"Number of queries: {q}")
    for _ in range(q):
        x = int(fin.readline().strip())
        print(f"Processing query: {x}")
        result = decibinaryNumbers(x)
        fout.write(str(result) + '\n')

    fin.close()
    fout.close()


