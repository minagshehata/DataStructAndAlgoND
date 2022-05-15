"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
from calendar import month
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts_ = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls_ = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
# Function to parse the input timestamp format and reurn list containing the parameters
# O(1) complexity as the execution is not impacted by the legnth of the input (assuming that the time/date format would never change)
def parseTimestamp(timestamp) : 
    return timestamp.replace("-"," ").replace(":"," ").split(" ")

# compare two timestamps if the first greater than the second shall return False
# O(1) complexity as the execution is not impacted by the legnth of the input (assuming that the time/date format would never change)
def compareTwoTimestamps(timestamp1,timestamp2):
    ts_1 = parseTimestamp(timestamp1)
    ts_2 = parseTimestamp(timestamp2)
    for i in range(len(ts_1)):
        if ts_1[i] < ts_2[i]:
            return True
        elif ts_1[i] > ts_2[i]:
            return False
    return True
            
#Function to get the first record in texts
# O(n) complexity as the execution would grow n times when the input legnth increments n unit.
def getTheFirstRecordOfTexts(texts):   
    record = texts[0]
    firstTimeStamp = texts[0][2]
    # pick the oldest record using O(n) time comlpexity 
    for i in texts:
        if compareTwoTimestamps(i[2],firstTimeStamp):
            firstTimeStamp = i[2]
            record = i         
    return record

#Function to get the last record in calls
# O(n) complexity as the execution would grow n times when the input legnth increments n unit.
def getTheLastRecordOfCalls(calls):   
    record = calls[0]
    lastTimestamp = calls[0][2]
    # pick the most recent record using O(n) time comlpexity 
    for i in calls:
        if compareTwoTimestamps(lastTimestamp,i[2]):
            lastTimestamp = i[2]
            record = i         
    return record

#Function to print first record of texts
def printTheFirstRecordOfTexts(texts):
    #get the first record of texts and print it 
    record=getTheFirstRecordOfTexts(texts)
    print("First record of texts, ",record[0]," texts ",record[1]," at time ",record[2])

#Function to print last record of calls
def printTheLastRecordOfCalls(calls):
    # get the last record of calls and print it
    record=getTheLastRecordOfCalls(calls)
    print("Last record of calls, ",record[0]," calls ",record[1]," at time ",record[2]," lasting ",record[3]," seconds")

# Print the required data assuming that the data in texts and the calls are not ordered 
printTheFirstRecordOfTexts(texts_)
printTheLastRecordOfCalls(calls_)