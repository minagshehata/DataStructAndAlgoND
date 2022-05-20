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
# Function to return area code of given number
# O(1) complexity 
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

# Function to return set with all the caller telemarketers
# O(n) Complexity
def addAllCallerTelemarketers(calls_,callerSet):
    # iterate on the input to add the telemarketers to the set
    # O(n) complexity
    for i in calls_:
        if returnCodeOfNumber(i[0]) == "140":
            callerSet.add(i[0])
    return callerSet

# Function to remove the called telemarketers from given set
# O(n) Complexity
def removeCalledTelemarketers(calls_,callerSet):
    # iterate on the input to remove the called telemarketers from the set
    # O(n) complexity
    for i in calls_:
        if returnCodeOfNumber(i[1]) == "140":
            callerSet.remove(i[1])
    return callerSet

# Function to remove the texted telemarketers from given set
# O(n) Complexity
def removeAllTexterTelemarketers(texts_,callerSet):
    # iterate on the input to remove the texted or the texter telemarketers from the set
    # O(n) complexity
    for i in texts_:
        if returnCodeOfNumber(i[0]) == "140":
            callerSet.remove(i[0])

        if returnCodeOfNumber(i[1]) == "140":
            callerSet.remove(i[1])    
    return callerSet

# Function to get all the possible telemarketers sorted
# O(3n+ n log n) Complexity
def getThePossibleTelemarkters(calls_,texts_):
    callerSet =set()
    # O(n) Complexity
    callerSet = addAllCallerTelemarketers(calls_,callerSet)
    # O(n) Complexity
    callerSet = removeCalledTelemarketers(calls_,callerSet)
    # O(n) Complexity
    callerSet = removeAllTexterTelemarketers(texts_,callerSet)
    # sorted function has O(n log n) complexity
    callerSet = sorted(callerSet)
    return callerSet

# Function to print all the possible telemarketers sorted in the required format
# O(3n+ n log n +n) Complexity
def printThePossibleTelemarketers(calls_,texts_):
    print("These numbers could be telemarketers: ")
    # O(3n+ n log n) Complexity
    set_= getThePossibleTelemarkters(calls_,texts_)
    # Considering the worst case that all the caller numbers were for telemarketers
    # the following print will carry O(n) complexity.
    for i in set_:
        print(i)
    return

printThePossibleTelemarketers(calls,texts)