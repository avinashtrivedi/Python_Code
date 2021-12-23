# do not delete this line! is is very important
# this line will write the contents of this cell to a file,
# which we can then run on different inputs
# this way we can make sure that everything works as indended
# in both visible and invisible tests.
# example for ans_3example
if isinstance(height, int):
    ans_3example = float(height)
elif isinstance(height, float):
    ans_3example = height
elif isinstance(height, str) and height == 'tall':
    ans_3example = 2.0
elif isinstance(height, str) and height == 'short':
    ans_3example = 1.0
else:
    ans_3example = None


# defining the conditions.
if isinstance(height, float):
    ans_3a = 'Float'
else:
    ans_3a = 'No'
    
if isinstance(height, int):
    if height>=18:
        ans_3b = 'voting age'
    elif height<18:
        ans_3b = 'not yet voting'
elif isinstance(height, float):
    ans_3b = "integer years only please"
else:
    ans_3b = "numbers please"
        
if isinstance(height, int) or isinstance(height,float):
    ans_3c = height*4
else:
    ans_3c = None
