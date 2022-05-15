"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

"""
1- make a alist for all different numbers in calls list. 
2- loop in diffNumbers list and iterate in the calls list if the number is found add call duration in the total duration for the number
3- iterate in the new list to pick the greatest duration.
"""

def makeNumersList(records):
    list=[]
    for i in records:
        list.append(i[0])
        list.append(i[1])
    return list

def searchForTheLongestDuration(calls_):
    list_ = makeNumersList(calls_)
    count = 1
    durationDict = {list_[0]:0}
    for i in range (1,len(list_)):
        for j in range(0,i+1):
            if (list_[i]==list_[j]):
                break; 
        if (i == j ):
            count +=1
            durationDict[list_[i]] = 0
    
    for key in durationDict:
        for i in calls :
            if i[0] == key or i[1] == key :
                durationDict[key] += int(i[3])
    
    longestDuration = durationDict[list_[0]]
    longestKey = list_[0] 
    for key in durationDict:
        if durationDict[key] > longestDuration:
            longestDuration = durationDict[key]
            longestKey = key
    return longestKey , durationDict[longestKey]

def printTheLongestDuration(calls_):
    key , duration = searchForTheLongestDuration(calls_)
    print (key , " spent the longest time, ",duration, "seconds, on the phone during September 2016.")

printTheLongestDuration(calls)