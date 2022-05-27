
import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    binary = bin(n)
    value = binary.index('b')
    binary = binary[value+1:]
    zeros = 32-len(binary)
    new_binary = []
    for i in range(zeros):
        new_binary.append(0)
    for i in binary:
        new_binary.append(i)
    for i in range(len(new_binary)):
        if(new_binary[i]=="1"):
            new_binary[i] = "0"
        else:
            new_binary[i] = "1"
    flipped = "".join(new_binary)
    return(int(flipped,2))


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        print(flippingBits(n))
