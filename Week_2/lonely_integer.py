
import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    a = sorted(a)
    j=0
    for i in range(len(a)):
        try:
            if(a[j]==a[j+1]):
                j+=2
                continue
            else:
                return(a[j])
        except:
            return(a[-1])

if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    print(lonelyinteger(a))