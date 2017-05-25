# Unit Assessment

import csv

def setup():
    
    nameList   = []
    carsList   = []
    timesList  = []
    pointList  = []
    megalist   = []
    
    return nameList,carsList,timesList,pointList,megalist

def readData(nameList,carsList,timesList,pointList, megalist):
    
    
    infile = open("racing.csv", "r")  
    reader = csv.reader(infile)
    
    for row in reader:
        nameList.append (""+row[0]+"")                                        
        carsList.append (""+row[1]+"")
        timesList.append(""+row[2]+"") 
        pointList.append(""+row[3]+"")
        
    megalist.append(nameList)     
    megalist.append(carsList)    
    megalist.append(pointList)
    megalist.append(timesList)
    infile.close()    
    
    return megalist

def editData(megalist):
    
    for x in range(6):
        
        # Race Time
        megalist[2][x] = float(input("What time did " + megalist[0][x] + " get?      "))
        
   
    return megalist

def sortData(megalist):
    sort = False
    tempVar = ""


    while sort == False:
        toSort = 6
        swapped = 0
        
        for x in range(toSort - 1):
            if megalist[2][x] > megalist[2][x + 1]:
                for y in range(4):
  
                    tempVar = megalist[y][x]
                 
                    megalist[y][x] = megalist[y][x + 1]
  
                    megalist[y][x + 1] = tempVar
       
                    
                swapped = swapped + 1               
                
        if swapped == 0:
            sort = True
        toSort = toSort - 1

    megalist[3][0] = 25
    megalist[3][1] = 18
    megalist[3][2] = 15
    

    return megalist
        
        
def giveData(megalist):
     
    write = csv.writer(open("racingResults.csv", "w", newline = ""))
    for row in megalist:

        write.writerow(row)

    
nameList,carsList,timesList,pointList, megalist = setup()    
readData(nameList,carsList,timesList,pointList, megalist) 
editData(megalist)
sortData(megalist)
giveData(megalist)

