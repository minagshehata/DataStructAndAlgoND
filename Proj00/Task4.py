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

""" 
identify all telemarketers making calls
remove numers if sending texts or receiving texts
"""
def returnCodeOfNumber(number):
    code = "undefined"
    # Fixed lines
    if  number.startswith("(0") :
        start = number.find("(") 
        end = number.find(")")
        code = number[start+1:end]
    # Mobile Numbers
    elif not (-1 == number.find(" ")) and (number.startswith("7") or number.startswith("8") or number.startswith("9") ):
        code = number[0:4]
    # Telemarketers 
    elif number.startswith("140"):
        code = "140"
    return code

def addAllCallerTelemarketers(calls_,callerSet):
    for i in calls_:
        if returnCodeOfNumber(i[0]) == "140":
            callerSet.add(i[0])
    return callerSet

def removeCalledTelemarketers(calls_,callerSet):
    for i in calls_:
        if returnCodeOfNumber(i[1]) == "140":
            callerSet.remove(i[1])
    return callerSet

def removeAllTexterTelemarketers(texts_,callerSet):
    for i in texts_:
        if returnCodeOfNumber(i[0]) == "140":
            callerSet.remove(i[0])

        if returnCodeOfNumber(i[1]) == "140":
            callerSet.remove(i[1])    
    return callerSet

def getThePossibleTelemarkters(calls_,texts_):
    callerSet =set()
    callerSet = addAllCallerTelemarketers(calls_,callerSet)
    callerSet = removeCalledTelemarketers(calls_,callerSet)
    callerSet = removeAllTexterTelemarketers(texts_,callerSet)
    callerSet = sorted(callerSet)
    return callerSet
    
def printThePossibleTelemarketers(calls_,texts_):
    print("These numbers could be telemarketers: ")
    set_= getThePossibleTelemarkters(calls_,texts_)
    for i in set_:
        print(i)
    return

printThePossibleTelemarketers(calls,texts)