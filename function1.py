# A list of key words for depression 
key_words = ['depress', 'sad', 'down']

def get_complaint_type(a_user_complaint):

    '''
    Precondition: a_user_complaint is a string 

    Postcondition:

    EITHER a_user_complaint contains one of key_words

    AND observed_complaint_type is the set consisting of "Depression"

    OR observed_complaint_type is the empty set

    Returns: observed_complaint_type 

    Example: user entered "I've been saddened by world conflicts" 

    and {"Depression"} was returned.

    '''
    # convert complaint to lower case
    a_user_complaint = a_user_complaint.lower()
    
    # define empty set
    set_to_return = set()
    
    # check if any key_words exists in a_user_complaint
    
    for word in key_words:
        if word in a_user_complaint:
            set_to_return.add('Depression')
            
    return set_to_return

print("Thank you for using Eliza300, a fun therapy program.")
print("Please state your complaint:")
user_complaint = input()
observed_complaint_type = get_complaint_type(user_complaint)

# if observed_complaint_type contains something
if len(observed_complaint_type) > 0:
    print("You have depression")