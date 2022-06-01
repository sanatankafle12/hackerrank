
import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in s.lower():
        if i in alphabets:
            alphabets.remove(i)
    if(len(alphabets)==0):
        print("pangram")
    else:
        print("not pangram.")
if __name__ == '__main__':
    s = input()

    pangrams(s)

