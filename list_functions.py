# import the library
import random

def random_list(n):
    
    # generate n random numbers and return 
    return random.sample(range(1, 101), n)

def average(lst):
    return round(sum(lst)/len(lst))

def only_odd(lst):
    
    # get list with only odd numbers
    return [i for i in lst if i%2!=0]

def to_string(lst):
    return str(lst)

def contains(lst,a,b):
    
    # check if there is any a directly followed by b
    for i in range(len(lst)-1):
        if lst[i]==a and lst[i+1]==b:
            return True
    return False

def has_duplicates(lst):
    
    # check the count of each element
    # if count is more than 1 ,it means there exists 
    # a duplicate
    for i in lst:
        if lst.count(i)>1:
            return True
    return False

