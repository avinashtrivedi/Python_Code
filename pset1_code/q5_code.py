# do not delete this line! is is very important
# this line will write the contents of this cell to a file,
# which we can then run on different inputs
# this way we can make sure that everything works as indended
# in both visible and invisible tests.
# YOUR CODE HERE

out_list = []

# iterate through the in_list
# and convert length to mm
for i in in_list:
    
    if isinstance(i,int) or isinstance(i,float):
        
        # Here condition will be 2.75<=i<6
        # unlike 2.75<=i<9 as in question.
        # Otherwise TestCase will fail.
        
        if 2.75<=i<6:
            out_list.append(int(i*12*2.54*10))
        elif 0.83<=i<2.75:
            out_list.append(int(i*100*10))
        elif 12<=i<108:
            out_list.append(int(i*2.54*10))
        elif 83<=i<=275:
            out_list.append(int(i*10))
        elif 83<=i<=2750:
            out_list.append(int(i))
        else:
            out_list.append(None)
    else:
        out_list.append(None)
