from funclib import pyramidmaker   
pnum = int(input("how many bricks would you like on the bottom floor:"))

if (pnum%2 > 0)   :
    pyramidmaker(pnum)
else:
    print("sorry but you have to enter a odd number, try again later.")