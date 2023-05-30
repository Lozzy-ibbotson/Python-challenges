#https://www.geeksforgeeks.org/get-current-timestamp-using-python/
#https://www.codespeedy.com/how-to-create-a-stopwatch-in-python/
#https://www.geeksforgeeks.org/create-stopwatch-using-python/
#https://www.programiz.com/python-programming/examples/random-number

import time
import random

def disaplyMessage(overallTime, target):
    if (overallTime > target):
        print("you were ", overallTime - target, " too slow")
    elif (overallTime < target):
        print("you were ", target - overallTime, " too fast")
    else:
        print("bang on target")
    # end if
#end def

def main():
    target = random.randint(0,4)
    print("your target is ", target)
    start = input("press enter to begin: ")

    startTime = time.time()
    stall = input("press enter when you think the time has passed:")

    finishTime = time.time()

    overallTime = finishTime-startTime

    print(overallTime)
    disaplyMessage(overallTime, target)
#end def

main()