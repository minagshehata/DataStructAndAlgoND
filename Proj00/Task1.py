"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from tkinter.tix import Tree
from typing import Concatenate
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
# function to collect all the caller and the called numbers in one list.
# O(2n) complexity as the executed instructions increments two unit per 1 unit increse in the input legnth
def makeNumersList(records):
    list=[]
    # gather the frist two columns on both of texts and calls in one list 
    for i in records:
        list.append(i[0])
        list.append(i[1])
    return list

#function to return the number of the different number in both of text and calls data.
# O(n^2+3n) complexity as the worst case that we don't have similar numbers.
def getCountOfDifferentNumbersInrecords(texts_,calls_):
    # Concatenate the two lists of data in one list  
    # considering n = k(legnth of texts) + m(legnth of call). the concatination would be O(n) complexity
    full_records=texts_+calls_
    count = 1
    # O(2n) complexity
    list_ = makeNumersList(full_records)
    # we have to iterate on the legnth of the input twice to identify if each element is counted before or not. 
    # O(n^2) complexity
    for i in range (1,len(list_)):
        for j in range(0,i+1):
            if (list_[i]==list_[j]):
                #break if the element counnted before
                break; 
        #in that case we are sure that the element not counted before
        if (i == j ):
            count +=1
    return count

# print the required output
print("There are ",getCountOfDifferentNumbersInrecords(texts,calls)," different telephone numbers in the records.")