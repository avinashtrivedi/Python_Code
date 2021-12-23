import calendar  # import library
months = calendar.month_name[1:] 
for x in range(len(months)): 
    print(x+1, months[x])