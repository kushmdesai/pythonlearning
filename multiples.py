from funclib import multiplesgetter


mnum = int(input("please pick a number to check it's multiples:"))
xnum = int(input("how many multiples would you like:"))
if xnum > 0:
    multiplesgetter(mnum,xnum)
else:
    print("sorry the multiples number must be greater than 0, Bye")