from funclib import numbergiver
from funclib import numleasttogreatestsorter
x = input("Do you want to randomly generate numbers or do you want to pick the number? Y for random or N for you pick (Y/N)")
if x == "Y":
    print("Ok")
    list1 = numbergiver()
    print("randomly generated numbesr" , list1)
    print("Sorted numbers" , numleasttogreatestsorter(list1))
else:
    print("Womp Womp you should have picked Y")