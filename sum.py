import sys

def sum(args):
    a = 0
    b = 0
    c = 0
    
    # get the length of args
    n = len(args)
    
    # loop through the arguments
    # compute the Sum1 ,Sum2 and Sum3 
    # as per the question
    # use int() to convert argument from str to int
    for i in range(1, n):
        a = a + int(args[i])
        b = b + int(args[i])**2
        c = c + int(args[i])**3
    return (a, b, c)

# call the function.
a,b,c = sum(sys.argv)
print("Sum1=%d Sum2=%d Sum3=%d" % (a, b, c))


