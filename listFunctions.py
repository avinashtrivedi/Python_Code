def swapFirstlast(myList):
    
    # swap first and last element
    myList[0],myList[-1] = myList[-1],myList[0]
    
def shiftRight(myList):
    
    # shift right 
    myList[:] = [myList[-1]] + myList[:-1]
    
def zeroEven(myList):
    
    # replace even with 0
    myList[:] = [0 if i%2==0 else i for i in myList]
    
    