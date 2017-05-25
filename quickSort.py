# quickSort
import random

numbers = [8,1,8,3,6,24,4,3,8,2,7,0,3]
#numLen  = 40

#for i in range(numLen):
#    numbers.append(random.randint(1,300))

def quickSort(numbers, i, listLength):
    if i < listLength:
        pivotPos = partition(numbers, i, listLength)
        quickSort(numbers, i, pivotPos - 1)
        quickSort(numbers, pivotPos + 1, listLength)
    return numbers
    
    
def partition(number,i,listLength):
    for a in range(listLength):
        for numNum in range(len(number)):
            for curNum in range(len(number)-1):
                if number[curNum] > number[curNum + 1]:
                    tempVar = number[curNum + 1]
                    number[curNum + 1] = number[curNum]
                    number[curNum] = tempVar
              
    return i


print(numbers)
quickSort(numbers, 0, 12)
print(numbers)
