import math
import os
import random
import re
import sys
import itertools
#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    subsets = list(itertools.combinations(ar, 2))
    array_lists = []
    for i in subsets:
        sum_of_tuple = i[0]+i[1]
        if((sum_of_tuple % k) == 0):
            array_lists.append(i)
    return(len(array_lists))


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    print(divisibleSumPairs(n, k, ar))