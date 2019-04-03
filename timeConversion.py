#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
# example : 12AM -> 00 ; 12PM -> 12
#           input  = hh:mm:ssAM 
#           result = hh:mm:ss
#           01AM -> 01  ; 11AM -> 11
#           09AM -> 09  ; 10AM -> 10 
#           12PM -> 12 ; 01PM -> 13 
#           05PM -> 17 ; 11PM -> 23
#           12AM -> 00 
    myList = convert2List(s) #[hh, mm, ss, shift]

    result = ""
    if myList[3] == "AM":
        if myList[0] == "12":
            result = "00"
        else: 
            result = myList[0]
    else:  #PM
        if myList[0] == "12":
            result = "12"
        else: 
            result = str(int(myList[0]) + 12)
    # result = "hh" --> "hh:mm:ss"
    result = result + ":" + myList[1] + ":" + myList[2]
    return result


def convert2List(myString):
#   input  = "hh:mm:ssAM" 
#             0123456789
    result = []  #[hh, mm, ss, shift]
    result.append(myString[0:2])
    result.append(myString[3:5])
    result.append(myString[6:8])
    result.append(myString[8:10])

    return result





if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
