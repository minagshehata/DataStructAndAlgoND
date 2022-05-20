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
# function to collect all the caller and the called numbers in one list.
# O(2n) complexity as the executed instructions increments two unit per 1 unit increse in the input legnth
def makeNumersList(records):
    list=[]
    # gather the frist two columns on calls data in one list 
    for i in records:
        list.append(i[0])
        list.append(i[1])
    return list

# Function to the number with the longest call duration in the month 
# O(n^2+2n+2n+n) = O(n^2+5n) ~ O(n^2)
def searchForTheLongestDuration(calls_):
    # O(2n) complexity
    list_ = makeNumersList(calls_)
    count = 1
    durationDict = {list_[0]:0}
    # construct a dictionary for all numbers in the calls data
    # we have to iterate on the legnth of the input twice to identify if each element is counted and added to the dictionary before or not. 
    # O(n^2) complexity
    for i in range (1,len(list_)):
        for j in range(0,i+1):
            if (list_[i]==list_[j]):
                break; 
        if (i == j ):
            count +=1
            durationDict[list_[i]] = 0
    # iterate ont the constructed dictionary to fill the duration for each number 
    # considering the worst case the complexity would be up to the total legnth of the input(n) : 
    # O(n) complexity
    for key in durationDict:
        for i in calls :
            if i[0] == key or i[1] == key :
                durationDict[key] += int(i[3])
    # get The longest duration 
    # O(2n) ~ O (n) complexity 
    longestDuration = durationDict[list_[0]]
    longestKey = list_[0] 
    for key in durationDict:
        if durationDict[key] > longestDuration:
            longestDuration = durationDict[key]
            longestKey = key
    return longestKey , durationDict[longestKey]

# Function to get the longest duration number and print it in the required format .
def printTheLongestDuration(calls_):
    key , duration = searchForTheLongestDuration(calls_)
    print (key , " spent the longest time, ",duration, "seconds, on the phone during September 2016.")

printTheLongestDuration(calls)