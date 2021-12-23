def assign_agents(list1, list2):
    
    """
    >>> players = ['Yuri', 'James', 'Huy', 'Siddharth']
    >>> agents = ['Jett', 'Sage', 'Reyna', 'Viper']
    >>> assign_agents(players, agents)
    [['Yuri', 'Jett'], ['James', 'Sage'], ['Huy', 'Reyna'], ['Siddharth', 'Viper']]
    >>> players = ['James', 'Yuri', 'Huy']
    >>> agents = ['Jett', 'Jett', 'Viper']
    >>> assign_agents(players, agents)
    [['James', 'Jett'], ['Yuri', 'Viper'], ['Huy', 'SPECTATOR']]
    >>> players = ['James', 'Yuri', 'Huy']
    >>> agents = ['Jett', 'Jett', 'Viper', 'Sage']
    >>> assign_agents(players, agents)
    [['James', 'Jett'], ['Yuri', 'Viper'], ['Huy', 'Sage']]
    """
    
    # get the unique ordered list
    list2 = list(dict.fromkeys(list2))
    
    # if size of list1 and list2 is same
    if len(list1) == len(list2):
        
        # the list with element wise tuple pair
        result = list(zip(list1,list2))
    
    # otherwise
    else:
        
        # add 'SPECTATOR' for the extra players
        list2 = list2 + ['SPECTATOR']* (len(list1)-len(list2))
        
        # the paired list
        result = list(zip(list1,list2))
    
    # get list of list
    result = [list(i) for i in result]
    return result