
import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    count = 0
    for i in range(len(s)):
        if(i%3==0 and s[i]=='S'):
            continue
        if(i%3==1 and s[i] =='O'):
            continue
        if(i%3==2 and s[i]=='S'):
            continue
        count+=1
    return(count)

if __name__ == '__main__':

    s = input()

    print(marsExploration(s))

