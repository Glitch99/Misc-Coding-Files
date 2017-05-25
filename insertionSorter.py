# Insertion Sort
import random


numbers = [6,1,8,3,2,4,7,6]
#numLen  = 40

#for i in range(numLen):
#    numbers.append(random.randint(1,300))

def bubbleSort(number):
    swaps = 0
    for numNum in range(len(number)): # selects each number
        for curNum in range(numNum - 1): # compares each number to each in front of it
            if number[curNum - 1] > number[curNum]:
                tempVar = number[curNum]
                number[curNum] = number[curNum - 1]
                number[curNum - 1] = tempVar
                swaps = swaps + 1
            print(number)
    return swaps
            
swaps = bubbleSort(numbers)
print(swaps)
end = input("Exit?   ")