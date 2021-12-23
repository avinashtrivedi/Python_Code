# loop to keep prompting for a valid input
while True:
    
    # get the valid height
    get_int = input('Height: ')
    
    # check if input is numeric
    if get_int.isnumeric():
        
        # convert input to integer , as by default
        # the input was in string form.
        get_int = int(get_int)
        
        # check if input is in the range of 1-8
        if 1<= get_int<=8:
            
            # print the half-pyramid
            for i in range(1,get_int+1):
                print((get_int-i)*' '+i*'#')
            
            # exit the loop
            break