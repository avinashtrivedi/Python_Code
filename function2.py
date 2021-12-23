complaint_type = ['Depression', 'Human Relations', 'Substance Abuse']

key_words = [['depress', 'sad', 'down'],

           ['conflict', 'argument', 'mistreat', 'quarrel'],

           ['drug', 'alcohol', 'drink', 'cocaine', 'opioid', 'heroin']]
    
def get_complaint_type(a_user_complaint):

    '''
    Precondition: 

    1. a_user_complaint is a string

    2. complaint_type is a list of strings

    3. key_words is a list of lists of strings

    3. complaint_type and key_words are the same length

    Returns: observed_complaint_type, which consists of the indices in

    complaint_type that correspond to key_words elements partly in a_user_complaint.

    Example: if the user enters "I've been saddened by world conflicts",

    the function returns the set consisting of 0 and 1 because "I've been saddened ..."    

    contains "sad" and "conflict".

    '''
    # convert complaint to lower case
    a_user_complaint = a_user_complaint.lower()
    
    # define empty set
    set_to_return = set()
    
    # get the key_words for Depression and Human Relations
    Depression = key_words[0]
    Human_Relations = key_words[1]
    
    # check if any Depression key_words exists in a_user_complaint
    # then add its index in the set.
    
    for indx in range(len(Depression)):
        if Depression[indx] in a_user_complaint:
            set_to_return.add(indx)
    
    # check if any Human Relations key_words exists in a_user_complaint
    # then add its index in the set.
    
    for indx in range(len(Human_Relations)):
        if Human_Relations[indx] in a_user_complaint:
            set_to_return.add(indx)
            
    return set_to_return

print("Thank you for using Eliza300, a fun therapy program.")
print("Please state your complaint:")
user_complaint = input()
observed_complaint_type = get_complaint_type(user_complaint)
print(observed_complaint_type)