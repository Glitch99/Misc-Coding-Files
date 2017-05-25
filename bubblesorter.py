# Bubble Sort Basic #
import random


numbers = []
numLen  = 99

for i in range(numLen):
    numbers.append(random.randint(0,1))

def bubbleSort(number):
    swaps = 0
    for numNum in range(len(number)):
        for curNum in range(len(number)-1):
            if number[curNum] > number[curNum + 1]:
                tempVar = number[curNum + 1]
                number[curNum + 1] = number[curNum]
                number[curNum] = tempVar
                swaps = swaps + 1
                #print(number)
    return swaps, number

           
swaps, numbers = bubbleSort(numbers)
print(numbers)
print(swaps)
end = input("Exit?   ")