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
    
input_number = int(input("Enter number to be checked: "))    
result=findpernum(input_number)
print(result)