from funclib import numbergiver
from funclib import numleatogresorter
from funclib import indexgiver
    
list1 = numbergiver()
print(numleatogresorter(list1))
numa = int(input("which numbers index would you like to know:"))
if numa > 100:
    print("sorry but the number must be less than 100, try again later.")
elif numa < 0:
    print("sorry but the number must be more than 0, try again later.")
else:
    indexgiver(numa,list1)    