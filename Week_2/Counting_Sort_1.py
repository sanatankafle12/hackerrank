import math
import os
import random
import re
import sys


def countingSort(arr):
    # Write your code here
    counting_array = []
    for i in range(100):
        counting_array.append(0)
    print(len(counting_array))
    for i in arr:
        counting_array[i] = counting_array[i] + 1
    return(counting_array)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    print(countingSort(arr))

