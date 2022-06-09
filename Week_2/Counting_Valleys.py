
import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    valley = 0
    sea_level = 0
    for i in path:
        if(i=="D" and sea_level==0):
            valley+=1
        if(i=="U"):
            sea_level+=1
        else:
            sea_level-=1
    return(valley)

if __name__ == '__main__':
    steps = int(input().strip())

    path = input()

    print(countingValleys(steps, path))