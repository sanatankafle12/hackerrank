import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    max_value = 0
    min_value = arr[0]
    for i in arr:
        if(max_value<i):
            max_value = i
        if(min_value>i):
            min_value = i
    min_arr = arr
    max_arr = arr
    print(sum(min_arr)-max_value,end=" ")
    print(sum(max_arr)-min_value)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)