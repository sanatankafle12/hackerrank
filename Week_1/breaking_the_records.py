
import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    min_score = scores[0]
    max_score = scores[0]
    scores = scores[1:]
    result = [0,0]
    
    for i in scores:
        if(i>max_score):
            result[0]+=1
            max_score = i
        elif(min_score>i):
            result[1]+=1
            min_score = i
        
    return result

if __name__ == '__main__':

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    print(breakingRecords(scores))
