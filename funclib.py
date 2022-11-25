def generateRandomNumList(length):
     print("Inside generateRandomeNum list")


def buildtower(fnum, bnum, tnum):

    cunt = 1
    while cunt <= fnum:
        
        count = 0
        while count < tnum:
            cont = 0
            while cont < bnum:
                print("#", end="")
                cont = cont+1
            count = count+1
            print(end="          ")
        cunt = cunt + 1
        print("")


def addingnum(mynum1,mynum2):
    
    return mynum2 + mynum1


def findpernum(inputnum):
    stopoint = inputnum / 2
   
    divinum=2
    sumall=1

    while divinum <= stopoint:       
        remainder = inputnum%divinum
        if(remainder == 0):
            sumall=sumall+divinum

        divinum=divinum+1

    if sumall==inputnum:
        return True
    else:
        return False


def numgusser():

  from random import randrange
  anum = randrange(0, 100)
  i = 1
  while i <= 10:
      i = i + 1
      gnum = int(input("i have picked a number between 1 and 100 guess my number:"))    
      if anum == gnum:
         print("that's right")
         break
      elif anum > gnum:
         print("that's too small")
      else:
         print("that's too big")


def numbergiver():
    num_list=[]
    from random import randrange
    for x in range(10):
      rnum = randrange(0,100)
      num_list.append(rnum)
    return num_list


def numleatogresorter(num_list):
    i = 0
    while i in range(9):
        o = 0
        while o in range(9):
            num1 = num_list[o]
            num2 = num_list[o+1]
            if num1 > num2:
                num_list[o] = num2
                num_list[o+1] = num1
            o = o+1
        i=i+1    
    return num_list


def multiplesgetter(mnum,xnum):
    anum = 1
    num=0
    numlist=[]
    for x in range(xnum):
        num=mnum*anum
        numlist.append(num)
        anum=anum+1
    print(numlist)


def pyramidmaker(pnum):
    import math
    snum = pnum/2
    snum = math.floor(snum)
    hnum = 1
    ssnum=snum+1
    for x in range(ssnum):
        for z in range(snum):
           print("",end=" ")
        for y in range(hnum):
                print("#",end="")
        snum=snum-1
        hnum=hnum+2     
        print("")        