def assign_teams(teams, leader_idx):
    """
    >>> list1 = [['Vegetables', 'Potato', 'Carrot'], ['Cars', 'Toyota', 'Volkswagen', 'Mitsubishi']]
    >>> assign_teams(list1, 0)
    {'Vegetables': ['Potato', 'Carrot'], 'Cars': ['Toyota', 'Volkswagen', 'Mitsubishi']}
    >>> list2 = [['Jett', 'Viper', 'Agents'], ['Ascent', 'Haven', 'Maps', 'Bind']]
    >>> assign_teams(list2, 2)
    {'Agents': ['Jett', 'Viper'], 'Maps': ['Ascent', 'Haven', 'Bind']}
    >>> list3 = [[27, 3, 81, 273], [128, 2, 512, 1024, 6834], [77, 11]]
    >>> assign_teams(list3, 1)
    {3: [27, 81, 273], 2: [128, 512, 1024, 6834], 11: [77]}
    """
    team_dict = {}
    
    # loop throught the teams 
    for team in teams:
        
        # remove the element at index leader_idx from each team 
        leader = team.pop(leader_idx)
        
        remaining_player = team
        
        # add items in dictionary
        team_dict[leader] = remaining_player
    return team_dict