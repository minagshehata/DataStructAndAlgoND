"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from unittest import result

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
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

# Function to list all Different area codes made from Bangalore 
# O(n^2) complexity
def makeListOfDifferentCodes(list_):
    result = [list_[0]]
    # we have to iterate on the legnth of the input twice to identify if each element is listed before or not. 
    # O(n^2) complexity
    for i in range (1,len(list_)):
        for j in range(0,i+1):
            if (list_[i]==list_[j]):
                break; 
        if (i == j ):
            result.append(list_[i])
    return result

# funtion to get sorted list of all Area codes made from Bangalore
# O(n+n^2+n log n) complexity
def getCalledCodes(calls_):
  listOfCodes= []
  allCallsFromBangalore=0
  callsFromBangaloreToBangalore=0
  # iterate on the full legnth input to construct list of all area codes
  # O(n) complexity
  for i in calls_:
        if i[0].startswith("(080)"):
          allCallsFromBangalore +=1
          code = returnCodeOfNumber(i[1])
          listOfCodes.append(code)
          if code == "080":
              callsFromBangaloreToBangalore +=1
  # O(n^2) complexity
  listOfDiffCodes = makeListOfDifferentCodes(listOfCodes)
  # sorted function has O(n log n) complexity
  return sorted(listOfDiffCodes), (callsFromBangaloreToBangalore*100/allCallsFromBangalore)

# Function to print all area codes called from Bangalore in the required format
# O(n+n^2+n log n + n) complexity
def printAllCalledCodesSorted(calls_):
      print("The numbers called by people in Bangalore have codes:")
      # O(n+n^2+n log n) complexity
      list_ , BangolareCallsPercentage=getCalledCodes(calls_)
      # Considering the worst case that all the processed calls were to different area codes:
      # the following print will carry O(n) complexity.
      for i in list_:
            print(i)
      print("%.2f  percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."% float(BangolareCallsPercentage),)
      
printAllCalledCodesSorted(calls)