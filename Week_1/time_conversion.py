
import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    list_of_time = s.split(":")
    last = list_of_time[-1]
    pm=last[-2:]
    last = last[0:2]
    if(pm=="AM"):
        if(list_of_time[0]=="12"):
            list_of_time[0] = "00"
            time = ":".join(list_of_time)
            return(time[:-2])
        else:
            return(s[:-2])    
    else:
        if(list_of_time[0]=="12"):
            return(s[:-2])
        else:
            list_of_time[0] = str(int(list_of_time[0]) + 12)
            time = ":".join(list_of_time)
            return(time[:-2])

if __name__ == '__main__':
    s = input()

    print(timeConversion(s))

    
    