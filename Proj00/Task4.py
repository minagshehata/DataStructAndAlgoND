"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# Function to return set with all the caller numbers
# O(n) Complexity
def addAllCallers(calls_,callerSet):
    # iterate on the input to add the caller number to the set
    # O(n) complexity
    for record in calls_:
        callerSet.add(record[0])
    return callerSet

# Function to delete from given set any number received a call or a text or send a text
# Assumiing n = legnth of calls_(k) and legnth of texts(m) -->  O(n) Complexity
def removeNonTelemarketers(calls_,texts_,callerSet):
    # O(k) complexity
    for record in calls_:
        callerSet.discard(record[1])
    # O(m) complexity
    for record in texts_:
        callerSet.discard(record[0])
        callerSet.discard(record[1])
        
    return callerSet

# Function to get all the possible telemarketers sorted
# O(2n+ n log n) Complexity
def getThePossibleTelemarkters(calls_,texts_):
    callerSet =set()
    
    # O(n) Complexity
    callerSet = addAllCallers(calls_,callerSet)
    
    # O(n) Complexity
    callerSet = removeNonTelemarketers(calls_,texts_,callerSet)

    # sorted function has O(n log n) complexity
    callerSet = sorted(callerSet)
    return callerSet

# Function to print all the possible telemarketers sorted in the required format
# O(2n+ n log n +n) Complexity
def printThePossibleTelemarketers(calls_,texts_):
    print("These numbers could be telemarketers: ")
    # O(2n+ n log n) Complexity
    set_= getThePossibleTelemarkters(calls_,texts_)
    # Considering the worst case that all the caller numbers were for telemarketers
    # the following print will carry O(n) complexity.
    for i in set_:
        print(i)
    return

printThePossibleTelemarketers(calls,texts)