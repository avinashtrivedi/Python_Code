def common_players(roster):
    """Returns a dictionary containing values along with a corresponding
    list of keys that had that value from the original dictionary.
    >>> full_roster = {"bob": "Team A", "barnum": "Team B", "beatrice": "Team C", "bernice": "Team B", "ben": "Team D", "belle": "Team A", "bill": "Team B", "bernie": "Team B", "baxter": "Team A"}
    >>> common_players(full_roster)
    {'Team A': ['bob', 'belle', 'baxter'], 'Team B': ['barnum', 'bernice', 'bill', 'bernie'], 'Team C': ['beatrice'], 'Team D': ['ben']}
    """
    
    # define a new empty dictionary
    new_dict = {}
    
    # iterate through the items of roster
    for val,key in roster.items():
        
        # add key and value to the new dictionary
        # if key is not present then add the key:value pair
        if key not in new_dict:
            new_dict[key] = [val]
        
        # if key is present then append the value for the corresponding key
        else:
            new_dict[key].append(val)
            
    # finally return the new_dict
    return new_dict