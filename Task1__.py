"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from tkinter.tix import Tree
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
full_records=texts+calls
print(len(texts))
print(len(calls))
print(len(full_records))

def getCountOfDifferentNumbersInrecords(records):
    count = 1
    for i in range (1,len(records)):
        not_rebeated_1 = False
        not_rebeated_2 = False
        for j in range( i):
            if not (records[i][0]==records[j][0] or records[i][0]==records[j][1]):
                not_rebeated_1 = True
            else:
                not_rebeated_1 = False
            if not (records[i][1]==records[j][0] or records[i][1]==records[j][1] or records[i][1] == records[i][0]):
                not_rebeated_2= True
            else:
                not_rebeated_2 = False
        if not_rebeated_1 == True:
            count+=1
        if not_rebeated_2 == True:
            count+=1
    return count

print(getCountOfDifferentNumbersInrecords(full_records))