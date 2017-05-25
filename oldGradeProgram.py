def setup():                                                                    #This will set up the variables and arrays
    name_list = []                                                              #This sets up the variable "name_list" as an array
    score1_list = []
    score2_list = []
    total_list = []
    grade_list = []
    percentages = []
    users = 15                                                                  #This sets the variable "users" to 15
    return name_list, score1_list, score2_list, total_list, grade_list,users, percentages   #This will store all values in the variables

def validate(min,max,v):                                                        #This validates the marks
    while v < min or v > max:
        message = "Enter a score between ",min," and ",max,", please:   "
        v = int(raw_input(message))
        

def getscores(name_list, score1_list, score2_list, users):                      #This will get the scores from the file "Class Marks"
    import csv
    myfile = open("N:\NetBeansProjects\Python_Tasks\Computing Science\Materials\Class Marks.csv", "r")  #These three lines (23-25) will open the file provided in the computer's memory
    reader = csv.reader(myfile)
    for row in reader:
        name_list.append(row[0])                                                #This will add the first row in the table to the array "name_list")                                           
        score1_list.append(int(row[1]))
        score2_list.append(int(row[2]))
    myfile.close()                                                              #This closes the file
     
    return name_list, score1_list, score2_list,users

def calculate(score1_list, score2_list, percentages):                           #This will calculate the total percentage
    for count in range (15):
        percent = (float((score1_list[count] + score2_list[count]))/120 * 100 )
        percentages.append(percent)
    return percentages

def grade(percentages, users):                                                  #This will work out the grades

    for count in range (users):
        if percentages[count] >=70:
            grade = ("A")
        elif percentages[count] >=60 and percentages[count] <= 69:
            grade = ("B")
        elif percentages[count] >=50 and percentages[count] <= 59:
            grade = ("C")
        elif percentages[count] >=40 and percentages[count] <= 49:
            grade = ("D")            
        else:
            grade = ("No Grade")
            
        grade_list.append(grade)
    
    return grade_list


def findmax(percentages):                                                       #This will find the highest percentage
    last = len(percentages)
    max = percentages[0]
    for c in range(1, last):
        if percentages[c] > max:
            max = percentages[c]
    return max
        
def linearsearch(percentages,name_list,max,users,score1_list,score2_list):      #This will show whoever got the highest percentage                
    for c in range(users):
        if percentages[c] >= max:
            maxname = name_list[c]
            output = "The highest scoring student was ", maxname, " who got " ,score1_list[c] + score2_list[c]," marks, and therefore got ","%.0f" % max,"% total."    
    return maxname, output



def countoccurences(grade_list):                                                #This counts the number of A grades achieved
    occurences = 0
    for i in grade_list:
        if i == "A":
            occurences = occurences + 1
    return occurences

def showdata(name_list, score1_list, score2_list,  percentages, grade_list, max, occurences, maxname, users):      #This will display all the information
    print "Student \t Course Mark \t Exam Mark \t Percentage \t Grade"
    for times in range(users):
        if len(name_list[times]) >= 15:
            print name_list[times], "\t", score1_list[times], "\t\t", score2_list[times], "\t    " ,"%.0f" % percentages[times], "%\t   ", grade_list[times] 
        elif len(name_list[times]) <= 6:
            print name_list[times], "\t\t\t", score1_list[times], "\t\t", score2_list[times], "\t    " ,"%.0f" % percentages[times], "%\t   ", grade_list[times]
        else:
            print name_list[times], "\t\t", score1_list[times], "\t\t", score2_list[times], "\t    " ,"%.0f" % percentages[times], "%\t   ", grade_list[times]
    print "The highest scoring student was ", maxname, " who had ","%.0f" % max,"%, and there were ", occurences, " A's." 
    

#MainProgram
name_list,score1_list, score2_list, total_list, grade_list, users, percentages = setup()
getscores(name_list ,score1_list, score2_list,users)
total_list = calculate(score1_list, score2_list,percentages)
grade_list = grade(percentages,users)
max = findmax(total_list)
occurences = countoccurences(grade_list)
maxname,output = linearsearch(total_list,name_list, max, users, score1_list, score2_list)

showdata(name_list, score1_list, score2_list, percentages, grade_list, max, occurences, maxname,users)

text_file = open("BestStudent.txt", "w")
text_file.write(str(output))
text_file.close
