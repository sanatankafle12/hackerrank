
import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        if(grades[i]<37):
            continue
        else:
            if(grades[i]%5 == 4):
                grades[i] += 1
            if(grades[i]%5 == 3):
                grades[i] += 2
    return(grades)

if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    print(gradingStudents(grades))

