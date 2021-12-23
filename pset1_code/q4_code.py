# do not delete this line! is is very important
# this line will write the contents of this cell to a file,
# which we can then run on different inputs
# this way we can make sure that everything works as indended
# in both visible and invisible tests.
# YOUR CODE HERE

out_list = [1 if isinstance(i,int) or isinstance(i,float) else 0 for i in in_list]
