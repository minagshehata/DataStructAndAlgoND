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

def makeNumersList(records):
    list=[]
    for i in records:
        list.append(i[0])
        list.append(i[1])
    return list
        
def getCountOfDifferentNumbersInrecords(texts_,calls_):
    full_records=texts_+calls_
    count = 1
    list_ = makeNumersList(full_records)
    for i in range (1,len(list_)):
        for j in range(0,i+1):
            if (list_[i]==list_[j]):
                break; 
        if (i == j ):
            count +=1
    return count

print("There are ",getCountOfDifferentNumbersInrecords(texts,calls)," different telephone numbers in the records.")